// A typed client for the game server hosting API: every call, field and error from the API file (schema.ts is
// generated from it by openapi-typescript; regenerate with oss/clients/generate.sh), on openapi-fetch.
//
//   const gs = createClient({ baseUrl: 'https://studio.survivalservers.com', apiKey: process.env.GS_API_KEY! });
//   const started = await unwrap(gs.POST('/v0/game-servers', {
//     params: { header: { 'Idempotency-Key': matchId } },
//     body: { app: 'breakwire-windows', placement: { regions: ['europe-west'] } },
//   }));
import createFetchClient from 'openapi-fetch';
import type { components, paths } from './schema.js';

export type { components, paths, operations } from './schema.js';
export type Problem = components['schemas']['Problem'];

export interface ClientOptions {
  /** An API key (gsk_live_...). */
  apiKey: string;
  /** The API's address; default the public one. */
  baseUrl?: string;
  /** Another fetch (tests, proxies). */
  fetch?: typeof fetch;
  /** How long each try of a call waits for its answer to start, in milliseconds (default ANSWER_TIMEOUT_MS). */
  timeoutMs?: number;
  /** How a call is tried again when the API did not do it (see RetryOptions); `false`: never. */
  retry?: RetryOptions | false;
}

/** A call is tried again on 429 rate_limited (any call: the API did nothing) and on 503 unavailable (an API location
 * briefly down) for reads and for writes that carry an Idempotency-Key (the same key on every try), waiting the answer's
 * Retry-After (1, then 2 seconds without one). Never on 503 capacity_unavailable: more regions, or later, is the
 * caller's call. An answer asking for a longer wait than maxWaitSeconds comes back at once. */
export interface RetryOptions {
  /** How many times a call is sent in all; default 3. */
  tries?: number;
  /** The longest Retry-After waited for, in seconds; default 30. */
  maxWaitSeconds?: number;
}

/** The package's version, sent as part of the User-Agent (a test checks it against package.json). */
export const VERSION = '0.1.0';

/** How long a call waits for its answer to start: above the API's longest wait of 60 seconds. A body that
 * keeps streaming after that (a followed log, the event stream) is never cut. */
export const ANSWER_TIMEOUT_MS = 70_000;

/** The API's own address, until the public name is chosen (a placeholder, like the docs'). Under a test runner
 * (node --test, Vitest, Jest) or with GS_API_URL_REQUIRED=1 an empty address is refused, so a test always names its own. */
export const DEFAULT_BASE_URL = 'https://studio.survivalservers.com';

/** Whether this runs under a test runner, where the default address is refused (no Node types: process is optional). */
function underTest(): boolean {
  const env = (globalThis as { process?: { env?: Record<string, string | undefined> } }).process?.env;
  return !!env && !!(env.NODE_TEST_CONTEXT || env.VITEST || env.JEST_WORKER_ID || env.NODE_ENV === 'test' || env.GS_API_URL_REQUIRED === '1');
}

export function createClient(opts: ClientOptions) {
  if (!opts.apiKey) throw new Error('@survivalservers/studio: an API key is required');
  if (!opts.baseUrl && underTest()) throw new Error('@survivalservers/studio: no API address given: tests must set one');
  const headers: Record<string, string> = { Authorization: `Bearer ${opts.apiKey}` };
  // Which client and version is calling. Not in a browser, which sends its own (and would ask the API first).
  if (!('document' in globalThis) && !('WorkerGlobalScope' in globalThis)) headers['User-Agent'] = `@survivalservers/studio/${VERSION}`;
  return createFetchClient<paths>({
    baseUrl: (opts.baseUrl || DEFAULT_BASE_URL).replace(/\/+$/, ''),
    headers,
    // Each try has its own time limit; the waits between tries never count against it.
    fetch: retrying(answerWithin(opts.fetch ?? ((input, init) => globalThis.fetch(input, init)), opts.timeoutMs ?? ANSWER_TIMEOUT_MS), opts.retry),
  });
}

/** fetch that tries a call again as RetryOptions says. */
function retrying(send: typeof fetch, opts: RetryOptions | false | undefined): typeof fetch {
  const tries = opts === false ? 1 : Math.max(1, Math.floor(opts?.tries ?? 3));
  const maxWait = opts === false ? 0 : Math.max(0, opts?.maxWaitSeconds ?? 30);
  if (tries === 1) return send;
  return async (input, init) => {
    const first = new Request(input, init); // never sent itself: each try sends a copy, body and all
    const method = first.method.toUpperCase();
    const keyed = first.headers.has('Idempotency-Key');
    for (let attempt = 1; ; attempt++) {
      const res = await send(first.clone());
      if (attempt >= tries || !(await tryAgain(method, keyed, res))) return res;
      const wait = retryWait(res.headers.get('Retry-After'), attempt);
      if (wait > maxWait || !(await pause(wait * 1000, first.signal))) return res;
      await res.body?.cancel();
    }
  };
}

async function tryAgain(method: string, keyed: boolean, res: Response): Promise<boolean> {
  if (res.status === 429) return true;
  if (res.status !== 503 || (!keyed && (method === 'POST' || method === 'PATCH'))) return false;
  const problem = await res.clone().json().catch(() => undefined);
  return (problem as Problem | undefined)?.code === 'unavailable';
}

function retryWait(retryAfter: string | null, attempt: number): number {
  const n = retryAfter === null || retryAfter.trim() === '' ? NaN : Number(retryAfter.trim());
  return Number.isInteger(n) ? Math.max(0, n) : attempt;
}

/** Waits ms; false when the caller gave up (its signal) first. */
function pause(ms: number, signal: AbortSignal): Promise<boolean> {
  return new Promise((resolve) => {
    if (signal.aborted) return resolve(false);
    const stop = () => {
      clearTimeout(timer);
      resolve(false);
    };
    const timer = setTimeout(() => {
      signal.removeEventListener('abort', stop);
      resolve(true);
    }, ms);
    signal.addEventListener('abort', stop, { once: true });
  });
}

/** fetch, given up when no answer has started within ms; the caller's own signal still stops it at any time. */
function answerWithin(base: typeof fetch, ms: number): typeof fetch {
  return async (input, init) => {
    const request = new Request(input, init);
    const stop = new AbortController();
    const own = request.signal;
    if (own.aborted) stop.abort(own.reason);
    else own.addEventListener('abort', () => stop.abort(own.reason), { once: true });
    const timer = setTimeout(() => stop.abort(new DOMException(`no answer within ${ms} ms`, 'TimeoutError')), ms);
    try {
      return await base(new Request(request, { signal: stop.signal }));
    } finally {
      clearTimeout(timer);
    }
  };
}

export type GsClient = ReturnType<typeof createClient>;

/** An answer that is not a success: the API's problem details, with the request ID to quote to support. */
export class ApiError extends Error {
  readonly status: number;
  readonly code?: string;
  readonly problem?: Problem;
  readonly requestId?: string;
  readonly retryAfter?: number;
  constructor(status: number, problem: Problem | undefined, response: Response) {
    super(problem?.detail ?? problem?.title ?? `HTTP ${status}`);
    this.name = 'ApiError';
    this.status = status;
    this.problem = problem;
    this.code = problem?.code;
    this.requestId = response.headers.get('Request-Id') ?? undefined;
    const ra = response.headers.get('Retry-After');
    this.retryAfter = ra === null ? undefined : Number(ra);
  }
}

/** The answer's data, or an ApiError. */
export async function unwrap<T>(call: Promise<{ data?: T; error?: unknown; response: Response }>): Promise<T> {
  const { data, error, response } = await call;
  if (!response.ok) throw new ApiError(response.status, error as Problem | undefined, response);
  return data as T;
}

/** A fresh Idempotency-Key, for a write you may retry. */
export function idempotencyKey(): string {
  return globalThis.crypto.randomUUID();
}

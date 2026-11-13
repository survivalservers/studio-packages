// Every call says which client is calling, and waits a limited time for its answer to start, but never cuts a body
// that keeps streaming after that.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import { ANSWER_TIMEOUT_MS, VERSION, createClient } from '../dist/index.js';

const json = (body) => new Response(JSON.stringify(body), { headers: { 'content-type': 'application/json' } });

test('the User-Agent names the package and its version', async () => {
  assert.equal(VERSION, JSON.parse(readFileSync(new URL('../package.json', import.meta.url))).version);
  assert.ok(ANSWER_TIMEOUT_MS > 60_000, 'above the API longest wait of 60 seconds');
  let ua;
  const gs = createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key', baseUrl: 'http://127.0.0.1:1', fetch: async (req) => {
    ua = req.headers.get('user-agent');
    return json({ data: [], next_cursor: null });
  } });
  await gs.GET('/v0/regions');
  assert.equal(ua, `@survivalservers/studio/${VERSION}`);
});

test('no answer within the limit gives up', async () => {
  const gs = createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key', baseUrl: 'http://127.0.0.1:1', timeoutMs: 50, fetch: (req) =>
    new Promise((_, reject) => req.signal.addEventListener('abort', () => reject(req.signal.reason))) });
  await assert.rejects(gs.GET('/v0/regions'), { name: 'TimeoutError' });
});

test('a body that streams past the limit is not cut', async () => {
  const gs = createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key', baseUrl: 'http://127.0.0.1:1', timeoutMs: 50, fetch: async (req) =>
    new Response(new ReadableStream({
      async start(c) {
        c.enqueue(new TextEncoder().encode('line 1\n'));
        await new Promise((r) => setTimeout(r, 150));
        if (!req.signal.aborted) c.enqueue(new TextEncoder().encode('line 2\n'));
        c.close();
      },
    }), { headers: { 'content-type': 'text/plain' } }) });
  const { data, error } = await gs.GET('/v0/game-servers/{id}/logs/stream', {
    params: { path: { id: 'gs_1' }, query: { follow: true } }, parseAs: 'text' });
  assert.equal(error, undefined);
  assert.equal(data, 'line 1\nline 2\n');
});

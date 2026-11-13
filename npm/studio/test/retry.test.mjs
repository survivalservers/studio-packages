// A call is tried again, up to 3 times in all, on 429 (any call: the API did nothing) and on 503 unavailable (a
// read, or a write with its Idempotency-Key, the same key and body on every try), waiting Retry-After up to the cap.
// Never on 503 capacity_unavailable, never past the cap, and never with retry: false. A fake fetch answers.
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiError, createClient, unwrap } from '../dist/index.js';

function fake(answers) {
  const sent = [];
  const fetch = async (req) => {
    sent.push({ method: req.method, key: req.headers.get('Idempotency-Key'), body: await req.text() });
    const a = answers.shift();
    if (!a) return new Response('{"id":"gs_1"}', { status: 201, headers: { 'content-type': 'application/json' } });
    const headers = { 'content-type': 'application/problem+json' };
    if (a.after !== undefined) headers['Retry-After'] = a.after;
    const problem = { type: `https://studio.survivalservers.com/docs/reference/errors/#${a.code}`, title: 'Refused', status: a.status, code: a.code, request_id: 'req_test' };
    return new Response(JSON.stringify(problem), { status: a.status, headers });
  };
  return { sent, fetch };
}

const client = (f, retry) => createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key', baseUrl: 'http://127.0.0.1:1', fetch: f.fetch, retry });
const start = (gs, key) => gs.POST('/v0/game-servers', {
  params: key ? { header: { 'Idempotency-Key': key } } : {},
  body: { app: 'brawl' },
});

test('429 is tried again, with the same body', async () => {
  const f = fake([{ status: 429, code: 'rate_limited', after: '0' }, { status: 429, code: 'rate_limited', after: '0' }]);
  const started = await unwrap(start(client(f)));
  assert.equal(started.id, 'gs_1');
  assert.equal(f.sent.length, 3);
  assert.ok(f.sent.every((s) => s.body === '{"app":"brawl"}'), JSON.stringify(f.sent));
});

test('three 429s: the third answer comes back', async () => {
  const f = fake([0, 1, 2].map(() => ({ status: 429, code: 'rate_limited', after: '0' })));
  await assert.rejects(unwrap(start(client(f))), (e) => e instanceof ApiError && e.status === 429 && e.retryAfter === 0);
  assert.equal(f.sent.length, 3);
});

test('503 unavailable: a write with its Idempotency-Key, the same key on every try', async () => {
  const f = fake([{ status: 503, code: 'unavailable', after: '0' }]);
  await unwrap(start(client(f), 'match-42'));
  assert.deepEqual(f.sent.map((s) => s.key), ['match-42', 'match-42']);
});

test('503 unavailable without a Retry-After waits a second', async () => {
  const f = fake([{ status: 503, code: 'unavailable' }]);
  const t0 = Date.now();
  await unwrap(client(f).GET('/v0/regions'));
  assert.equal(f.sent.length, 2);
  assert.ok(Date.now() - t0 >= 900, 'waited about a second');
});

test('503 unavailable: a write without an Idempotency-Key is not tried again', async () => {
  const f = fake([{ status: 503, code: 'unavailable', after: '0' }]);
  await assert.rejects(unwrap(start(client(f))), (e) => e.code === 'unavailable');
  assert.equal(f.sent.length, 1);
});

test('capacity_unavailable is the caller\'s call', async () => {
  const f = fake([{ status: 503, code: 'capacity_unavailable', after: '0' }]);
  await assert.rejects(unwrap(start(client(f), 'match-43')), (e) => e.code === 'capacity_unavailable');
  assert.equal(f.sent.length, 1);
});

test('a wait over the cap comes back at once', async () => {
  const f = fake([{ status: 429, code: 'rate_limited', after: '120' }]);
  await assert.rejects(unwrap(start(client(f))), (e) => e.retryAfter === 120);
  assert.equal(f.sent.length, 1);
});

test('retry: false never tries again', async () => {
  const f = fake([{ status: 429, code: 'rate_limited', after: '0' }]);
  await assert.rejects(unwrap(start(client(f, false))), (e) => e.status === 429);
  assert.equal(f.sent.length, 1);
});

test('a caller that gives up during the wait gets the answer, and nothing more is sent', async () => {
  const f = fake([{ status: 429, code: 'rate_limited', after: '5' }]);
  const ac = new AbortController();
  setTimeout(() => ac.abort(), 50);
  const t0 = Date.now();
  const { response } = await client(f).GET('/v0/regions', { signal: ac.signal });
  assert.equal(response.status, 429);
  assert.equal(f.sent.length, 1);
  assert.ok(Date.now() - t0 < 2000, 'did not wait the 5 seconds');
});

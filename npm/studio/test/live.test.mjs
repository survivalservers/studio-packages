// Against a running API: GS_API_URL and GS_API_KEY, and
// GS_TEST_APP naming an app with a version live in GS_TEST_REGION (default us-central) on a machine. Skipped without GS_API_URL.
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { ApiError, createClient, idempotencyKey, unwrap } from '../dist/index.js';

const url = process.env.GS_API_URL;
const region = process.env.GS_TEST_REGION ?? 'us-central';
const opts = { skip: !url && 'GS_API_URL is not set' };

test('studio, apps, a refused call and a game server, through the TypeScript client', opts, async () => {
  const gs = createClient({ apiKey: process.env.GS_API_KEY, baseUrl: url });
  const studio = await unwrap(gs.GET('/v0/studio'));
  assert.match(studio.id, /^std_/);

  const key = idempotencyKey();
  const name = `client-ts-${Date.now()}`;
  const made = await unwrap(gs.POST('/v0/apps', { params: { header: { 'Idempotency-Key': key } }, body: { name, os: 'windows' } }));
  const again = await unwrap(gs.POST('/v0/apps', { params: { header: { 'Idempotency-Key': key } }, body: { name, os: 'windows' } }));
  assert.equal(again.id, made.id, 'the repeat with the same Idempotency-Key made a second app');
  const read = await unwrap(gs.GET('/v0/apps/{app}', { params: { path: { app: made.slug } } }));
  assert.equal(read.id, made.id);
  const list = await unwrap(gs.GET('/v0/apps', { params: { query: { limit: 500 } } }));
  assert.ok(list.data.some((a) => a.id === made.id));

  // A start for an app with no version: refused, as a typed problem.
  await assert.rejects(
    unwrap(gs.POST('/v0/game-servers', { body: { app: made.slug, placement: { regions: [region] } } })),
    (e) => e instanceof ApiError && e.status >= 400 && e.status < 500 && typeof e.code === 'string' && !!e.requestId,
  );
  await assert.rejects(unwrap(gs.GET('/v0/apps/{app}', { params: { path: { app: 'no-such-app' } } })),
    (e) => e instanceof ApiError && e.status === 404 && e.code === 'not_found');
  const del = await gs.DELETE('/v0/apps/{app}', { params: { path: { app: made.id } } });
  assert.equal(del.response.status, 204);

  const app = process.env.GS_TEST_APP;
  if (!app) return;
  const started = await unwrap(gs.POST('/v0/game-servers', {
    params: { header: { 'Idempotency-Key': idempotencyKey() } },
    body: { app, start_mode: 'cold', placement: { regions: [region] }, labels: { client: 'typescript' } },
  }));
  assert.match(started.id, /^gs_/);
  assert.ok(Object.keys(started.address.ports).length > 0, 'no ports in the start answer');
  const got = await unwrap(gs.GET('/v0/game-servers/{id}', { params: { path: { id: started.id } } }));
  assert.equal(got.id, started.id);
  const found = await unwrap(gs.GET('/v0/game-servers', { params: { query: { label: ['client:typescript'] } } }));
  assert.ok(found.data.some((g) => g.id === started.id));
  const stop = await gs.POST('/v0/game-servers/{id}/stop', { params: { path: { id: started.id } } });
  assert.ok(stop.response.status === 202 || stop.response.status === 200, `stop answered ${stop.response.status}`);
});

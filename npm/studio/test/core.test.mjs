// The core path against a running API with a real machine: a Windows zip uploaded in parts as a build, a version
// staged in a region, the event stream followed, a game server of it started, listed and stopped, and its running and
// stopped events read. Needs GS_API_URL, GS_API_KEY, GS_TEST_ZIP (the zip), GS_TEST_VERSION (a JSON file: the
// version's settings without name and build) and GS_TEST_REGION; skipped without GS_TEST_ZIP. Storage links are
// fetched with Node's fetch, so a proxy for them comes from HTTP_PROXY with NODE_USE_ENV_PROXY=1.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { basename } from 'node:path';
import { test } from 'node:test';
import { createClient, idempotencyKey, unwrap } from '../dist/index.js';

const zip = process.env.GS_TEST_ZIP;
const opts = { skip: !zip && 'GS_TEST_ZIP is not set', timeout: 30 * 60 * 1000 };
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function until(what, read, done, seconds) {
  const end = Date.now() + seconds * 1000;
  for (;;) {
    const v = await read();
    if (done(v)) return v;
    if (Date.now() > end) throw new Error(`gave up waiting for ${what}: ${JSON.stringify(v).slice(0, 400)}`);
    await sleep(2000);
  }
}

// follow reads the event stream into `seen` until stop() is called.
function follow(gs, seen) {
  const ac = new AbortController();
  const done = (async () => {
    const { data, response } = await gs.GET('/v0/events/stream', {
      params: { query: { types: ['game_server.*'] } }, parseAs: 'stream', signal: ac.signal,
    });
    assert.equal(response.status, 200, 'the event stream answered');
    const reader = data.pipeThrough(new TextDecoderStream()).getReader();
    let buf = '';
    try {
      for (;;) {
        const { value, done: end } = await reader.read();
        if (end) return;
        buf += value;
        let i;
        while ((i = buf.indexOf('\n\n')) >= 0) {
          const block = buf.slice(0, i);
          buf = buf.slice(i + 2);
          const line = block.split('\n').find((l) => l.startsWith('data:'));
          if (line) seen.push(JSON.parse(line.slice(5).trim()));
        }
      }
    } catch (e) {
      if (e.name !== 'AbortError') throw e;
    }
  })();
  return { stop: () => { ac.abort(); return done.catch(() => {}); } };
}

test('core path: zip build, version, start, list, stop and events, through the TypeScript client', opts, async () => {
  const gs = createClient({ apiKey: process.env.GS_API_KEY, baseUrl: process.env.GS_API_URL });
  const region = process.env.GS_TEST_REGION ?? 'us-central';
  const settings = JSON.parse(readFileSync(process.env.GS_TEST_VERSION, 'utf8'));
  const slug = `core-ts-${Date.now()}`;
  const app = await unwrap(gs.POST('/v0/apps', { params: { header: { 'Idempotency-Key': idempotencyKey() } },
    body: { name: slug, slug, os: 'windows' } }));

  // The build: the API hands out a storage link per part; each part goes with its exact length.
  const bytes = readFileSync(zip);
  const build = await unwrap(gs.POST('/v0/apps/{app}/builds', { params: { path: { app: app.slug }, header: { 'Idempotency-Key': idempotencyKey() } },
    body: { os: 'windows', source: { type: 'upload', filename: basename(zip), bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') } } }));
  const size = build.upload.part_bytes;
  const parts = [];
  for (const p of build.upload.parts) {
    const r = await fetch(p.url, { method: 'PUT', body: bytes.subarray((p.number - 1) * size, p.number * size) });
    assert.equal(r.status, 200, `part ${p.number} upload answered ${r.status}`);
    parts.push({ number: p.number, etag: r.headers.get('etag') });
  }
  await unwrap(gs.POST('/v0/builds/{id}/complete', { params: { path: { id: build.id } }, body: { parts } }));
  const ready = await until('the build', () => unwrap(gs.GET('/v0/builds/{id}', { params: { path: { id: build.id } } })),
    (b) => b.status === 'ready' || b.status === 'failed', 600);
  assert.equal(ready.status, 'ready', JSON.stringify(ready.failure ?? ready));

  const version = await unwrap(gs.POST('/v0/apps/{app}/versions', { params: { path: { app: app.slug } },
    body: { ...settings, name: '1.0.0', build: build.id, regions: [region] } }));
  const staged = await until('the version in ' + region, () => unwrap(gs.GET('/v0/apps/{app}/versions/{version}', { params: { path: { app: app.slug, version: version.name } } })),
    (v) => v.regions.some((c) => c.status === 'ready' || c.status === 'failed'), 900);
  assert.ok(staged.regions.some((c) => c.region === region && c.status === 'ready'), JSON.stringify(staged.regions));

  const seen = [];
  const stream = follow(gs, seen);
  await sleep(1000);
  const started = await unwrap(gs.POST('/v0/game-servers', { params: { header: { 'Idempotency-Key': idempotencyKey() } },
    body: { app: app.slug, version: version.name, start_mode: 'cold', placement: { regions: [region] }, labels: { client: 'typescript-core' } } }));
  const active = await until('the game server', () => unwrap(gs.GET('/v0/game-servers/{id}', { params: { path: { id: started.id } } })),
    (g) => g.status !== 'starting', 300);
  assert.equal(active.status, 'running', JSON.stringify(active));
  const listed = await unwrap(gs.GET('/v0/game-servers', { params: { query: { label: ['client:typescript-core'] } } }));
  assert.ok(listed.data.some((g) => g.id === started.id), 'listed by its label');
  const stop = await gs.POST('/v0/game-servers/{id}/stop', { params: { path: { id: started.id } } });
  assert.ok(stop.response.status === 202 || stop.response.status === 200, `stop answered ${stop.response.status}`);
  const stopped = await until('the stop', () => unwrap(gs.GET('/v0/game-servers/{id}', { params: { path: { id: started.id } } })),
    (g) => g.status === 'stopped' || g.status === 'failed', 300);
  assert.equal(stopped.status, 'stopped');
  await until('its events', async () => seen.filter((e) => e.data?.id === started.id).map((e) => e.type),
    (types) => types.includes('game_server.running') && types.includes('game_server.stopped'), 60);
  await stream.stop();
  console.log(`core path passed: app ${app.slug}, build ${build.id} (${parts.length} parts), version ${version.name} in ${region}, game server ${started.id} running and stopped, events ${seen.filter((e) => e.data?.id === started.id).map((e) => e.type).join(', ')}`);
});

// A test always names the address it calls: under the test runner, createClient with no address is refused,
// and an address the test names is used as given.
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { createClient } from '../dist/index.js';

test('a test must name its own address', async () => {
  assert.throws(() => createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key' }), /no API address given: tests must set one/);
  let asked;
  const gs = createClient({ apiKey: 'gsk_live_EXAMPLE_not_a_real_key', baseUrl: 'http://127.0.0.1:1/', fetch: async (req) => {
    asked = req.url;
    return new Response('{"data":[],"next_cursor":null}', { headers: { 'content-type': 'application/json' } });
  } });
  await gs.GET('/v0/regions');
  assert.equal(asked, 'http://127.0.0.1:1/v0/regions');
});

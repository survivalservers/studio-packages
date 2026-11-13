# @survivalservers/studio (TypeScript)

```ts
import { createClient, idempotencyKey, unwrap, ApiError } from '@survivalservers/studio';

const gs = createClient({ baseUrl: 'https://studio.survivalservers.com', apiKey: process.env.GS_API_KEY! });
const server = await unwrap(gs.POST('/v0/game-servers', {
  params: { header: { 'Idempotency-Key': idempotencyKey() } },
  body: { app: 'breakwire-windows', placement: { regions: ['europe-west'] } },
}));
console.log(server.address.ipv4, server.address.ports);
```

A bulk action, dry run first (`.plan`), then for real (`.bulk_action`):

```ts
const body = { selector: { target: 'persistent_servers' as const, app: 'brinewatch-linux' }, command: { type: 'console' as const, line: 'save' } };
const { plan } = await unwrap(gs.POST('/v0/bulk-actions/commands', {
  params: { header: { 'Idempotency-Key': idempotencyKey() } }, body: { ...body, dry_run: true } }));
console.log(plan.total, 'persistent servers,', plan.skipped.length, 'skipped');
const { bulk_action } = await unwrap(gs.POST('/v0/bulk-actions/commands', {
  params: { header: { 'Idempotency-Key': idempotencyKey() } }, body }));
```

Following events live (server-sent events: `id:`, `event:` and `data:` lines, one blank line after each event):

```ts
const { data } = await gs.GET('/v0/events/stream', { params: { query: { types: ['game_server.*'] } }, parseAs: 'stream' });
const reader = data!.pipeThrough(new TextDecoderStream()).getReader();
for (let r = await reader.read(); !r.done; r = await reader.read()) console.log(r.value);
```

Every path, body and answer is typed from the API file (`src/schema.ts`). `unwrap` returns the answer or throws an
`ApiError` with the API's problem details (`code`, `problem`, `requestId`, `retryAfter`). A call the API did not do is
tried again, 3 times in all: on `429 rate_limited` (any call), and on `503 unavailable` for reads and for writes that
carry an `Idempotency-Key`, waiting `Retry-After` up to 30 seconds. Never on `503 capacity_unavailable`, which is yours
to answer (more regions, or later). `createClient({ ..., retry: { tries, maxWaitSeconds } })` changes it, and
`retry: false` turns it off. Each try gives up when its answer has not started within 70 seconds (`timeoutMs` changes it; a body
that keeps streaming is never cut), and outside a browser every call sends the package's name and version as the
User-Agent. Apache-2.0.

"""The core path against a running API with a real machine: a Windows zip uploaded in parts as a build, a version
staged in a region, the event stream followed, a game server of it started, listed and stopped, and its running and
stopped events read. Needs GS_API_URL, GS_API_KEY, GS_TEST_ZIP (the zip), GS_TEST_VERSION (a JSON file: the
version's settings without name and build) and GS_TEST_REGION; skipped without GS_TEST_ZIP. Storage links are sent
with httpx, which takes a proxy for them from HTTP_PROXY."""

import hashlib
import json
import os
import threading
import time
import uuid

import httpx
import pytest

from survivalservers_studio import AuthenticatedClient
from survivalservers_studio.api.apps import create_app
from survivalservers_studio.api.builds import complete_build, create_build, get_build
from survivalservers_studio.api.game_servers import get_game_server, list_game_servers, start_game_server, stop_game_server
from survivalservers_studio.api.versions import create_version, get_version
from survivalservers_studio.models import AppCreate, BuildComplete, BuildCreate, GameServer, GameServerCreate, Os, VersionCreate

ZIP = os.environ.get("GS_TEST_ZIP")
pytestmark = pytest.mark.skipif(not ZIP, reason="GS_TEST_ZIP is not set")


def until(what, read, done, seconds):
    end = time.time() + seconds
    while True:
        v = read()
        if done(v):
            return v
        if time.time() > end:
            raise AssertionError(f"gave up waiting for {what}: {v}")
        time.sleep(2)


def follow(gs: AuthenticatedClient, seen: list, stop: threading.Event):
    """Reads the event stream (server-sent events) with the client's own httpx client until stop is set."""
    with gs.get_httpx_client().stream("GET", "/v0/events/stream", params={"types": "game_server.*"},
                                      timeout=httpx.Timeout(10, read=None)) as r:
        assert r.status_code == 200, r.status_code
        for line in r.iter_lines():
            if line.startswith("data:"):
                seen.append(json.loads(line[5:].strip()))
            if stop.is_set():
                return


def test_core_path():
    gs = AuthenticatedClient(base_url=os.environ["GS_API_URL"], token=os.environ["GS_API_KEY"], raise_on_unexpected_status=True)
    region = os.environ.get("GS_TEST_REGION", "us-central")
    settings = json.load(open(os.environ["GS_TEST_VERSION"]))
    slug = f"core-py-{int(time.time() * 1000)}"
    app = create_app.sync(client=gs, body=AppCreate(name=slug, slug=slug, os=Os.WINDOWS), idempotency_key=str(uuid.uuid4()))

    data = open(ZIP, "rb").read()
    build = create_build.sync(client=gs, app=app.slug, idempotency_key=str(uuid.uuid4()), body=BuildCreate.from_dict({
        "os": "windows", "source": {"type": "upload", "filename": os.path.basename(ZIP), "bytes": len(data),
                                    "sha256": hashlib.sha256(data).hexdigest()}}))
    size = build.upload.part_bytes
    parts = []
    with httpx.Client(timeout=900) as storage:  # never the API client: storage links carry their own signature
        for p in build.upload.parts:
            r = storage.put(p.url, content=data[(p.number - 1) * size:p.number * size])
            assert r.status_code == 200, f"part {p.number}: {r.status_code} {r.text[:200]}"
            parts.append({"number": p.number, "etag": r.headers["etag"]})
    complete_build.sync(client=gs, id=build.id, body=BuildComplete.from_dict({"parts": parts}))
    ready = until("the build", lambda: get_build.sync(client=gs, id=build.id), lambda b: str(b.status) in ("ready", "failed"), 600)
    assert str(ready.status) == "ready", ready

    version = create_version.sync(client=gs, app=app.slug, body=VersionCreate.from_dict({**settings, "name": "1.0.0", "build": build.id, "regions": [region]}))
    staged = until("the version", lambda: get_version.sync(client=gs, app=app.slug, version=version.name),
                   lambda v: any(str(c.status) in ("ready", "failed") for c in v.regions), 900)
    assert any(c.region == region and str(c.status) == "ready" for c in staged.regions), staged.regions

    seen, stop = [], threading.Event()
    t = threading.Thread(target=follow, args=(gs, seen, stop), daemon=True)
    t.start()
    time.sleep(1)
    started = start_game_server.sync(client=gs, idempotency_key=str(uuid.uuid4()), body=GameServerCreate.from_dict({
        "app": app.slug, "version": version.name, "start_mode": "cold", "placement": {"regions": [region]}, "labels": {"client": "python-core"}}))
    assert isinstance(started, GameServer), started
    active = until("the game server", lambda: get_game_server.sync(client=gs, id=started.id), lambda g: str(g.status) != "starting", 300)
    assert str(active.status) == "running", active
    assert any(g.id == started.id for g in list_game_servers.sync(client=gs, label=["client:python-core"]).data)
    assert stop_game_server.sync_detailed(client=gs, id=started.id).status_code in (200, 202)
    stopped = until("the stop", lambda: get_game_server.sync(client=gs, id=started.id), lambda g: str(g.status) in ("stopped", "failed"), 300)
    assert str(stopped.status) == "stopped"
    types = until("its events", lambda: [e["type"] for e in seen if (e.get("data") or {}).get("id") == started.id],
                  lambda ts: "game_server.running" in ts and "game_server.stopped" in ts, 60)
    stop.set()
    print(f"core path passed: app {app.slug}, build {build.id} ({len(parts)} parts), version {version.name} in {region}, "
          f"game server {started.id} running and stopped, events {', '.join(types)}")

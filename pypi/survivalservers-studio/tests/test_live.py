"""Against a running API: GS_API_URL and GS_API_KEY, and
GS_TEST_APP naming an app with a version live in GS_TEST_REGION (default us-central) on a machine. Skipped without GS_API_URL."""

import os
import time
import uuid

import pytest

from survivalservers_studio import AuthenticatedClient
from survivalservers_studio.api.apps import create_app, delete_app, get_app, list_apps
from survivalservers_studio.api.game_servers import get_game_server, list_game_servers, start_game_server, stop_game_server
from survivalservers_studio.api.studio import get_studio
from survivalservers_studio.models import App, AppCreate, GameServer, GameServerCreate, Os, Placement, Problem

URL = os.environ.get("GS_API_URL")
REGION = os.environ.get("GS_TEST_REGION", "us-central")
pytestmark = pytest.mark.skipif(not URL, reason="GS_API_URL is not set")


def client() -> AuthenticatedClient:
    return AuthenticatedClient(base_url=URL, token=os.environ["GS_API_KEY"], raise_on_unexpected_status=True)


def test_studio_apps_refusals_and_a_game_server():
    gs = client()
    studio = get_studio.sync(client=gs)
    assert studio.id.startswith("std_")

    key = str(uuid.uuid4())
    name = f"client-py-{int(time.time() * 1000)}"
    made = create_app.sync(client=gs, body=AppCreate(name=name, os=Os.WINDOWS), idempotency_key=key)
    assert isinstance(made, App), made
    again = create_app.sync(client=gs, body=AppCreate(name=name, os=Os.WINDOWS), idempotency_key=key)
    assert again.id == made.id, "the repeat with the same Idempotency-Key made a second app"
    assert get_app.sync(client=gs, app=made.slug).id == made.id
    assert any(a.id == made.id for a in list_apps.sync(client=gs, limit=500).data)

    # A start for an app with no version: refused, as a typed problem.
    refused = start_game_server.sync_detailed(client=gs, body=GameServerCreate(app=made.slug,
                                              placement=Placement(regions=[REGION])))
    assert 400 <= refused.status_code < 500
    assert isinstance(refused.parsed, Problem) and refused.parsed.code and refused.parsed.request_id
    missing = get_app.sync_detailed(client=gs, app="no-such-app")
    assert missing.status_code == 404 and missing.parsed.code == "not_found"
    assert delete_app.sync_detailed(client=gs, app=made.id).status_code == 204

    app = os.environ.get("GS_TEST_APP")
    if not app:
        return
    started = start_game_server.sync(client=gs, body=GameServerCreate.from_dict({
        "app": app, "start_mode": "cold", "placement": {"regions": [REGION]}, "labels": {"client": "python"}}),
        idempotency_key=str(uuid.uuid4()))
    assert isinstance(started, GameServer), started
    assert started.id.startswith("gs_")
    assert get_game_server.sync(client=gs, id=started.id).id == started.id
    found = list_game_servers.sync(client=gs, label=["client:python"])
    assert any(g.id == started.id for g in found.data)
    assert stop_game_server.sync_detailed(client=gs, id=started.id).status_code in (200, 202)

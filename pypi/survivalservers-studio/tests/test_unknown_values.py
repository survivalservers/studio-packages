"""The API adds values at any time (its Stability section: "clients must ... tolerate new enum values"): a status,
error code or other value this version does not know is read as it came, never refused. Runs with no API:
the answers come from httpx's mock transport."""

import httpx

from survivalservers_studio import AuthenticatedClient
from survivalservers_studio.api.game_servers import get_game_server
from survivalservers_studio.models import ErrorCode, GameServer, GameServerStatus, Problem

# The API file's GameServer example, with values no version of this client knows yet.
SERVER = {
    "id": "gs_a01JA8X9K2Q7M3T5V6W8Y0Z1B2", "status": "draining", "start_mode": "warm",
    "app": "app_a01JA7ZQ4W8E2R6T0Y4U8I2O6P", "version": "2.3.1", "persistent_server": None, "region": "europe-west",
    "continent": "europe", "tier": "a-tier-added-later", "os": "windows", "size": {"cpu": 2, "memory_gb": 4},
    "address": {"ipv4": "203.0.113.24", "ipv6": None,
                "ports": {"game": {"port": 31042, "protocol": "quic"}, "query": {"port": 31043, "protocol": "udp"}}},
    "labels": {"match_id": "88231"}, "players": {"count": 0}, "created_at": "2026-10-09T18:22:04.512Z",
}
PROBLEM = {"type": "https://studio.survivalservers.com/docs/reference/errors/#a_code_added_next_month",
           "title": "Something new", "status": 404, "code": "a_code_added_next_month", "request_id": "req_test"}


def answering(status: int, body: dict) -> AuthenticatedClient:
    return AuthenticatedClient(base_url="http://127.0.0.1:1", token="gsk_live_EXAMPLE_not_a_real_key", httpx_args={
        "transport": httpx.MockTransport(lambda request: httpx.Response(status, json=body))})


def test_a_new_status_is_read_as_it_came():
    gs = get_game_server.sync(client=answering(200, SERVER), id=SERVER["id"])
    assert isinstance(gs, GameServer), gs
    assert gs.status == "draining" and str(gs.status) == "draining"
    assert isinstance(gs.status, GameServerStatus)
    assert gs.to_dict()["status"] == "draining" and gs.to_dict()["tier"] == "a-tier-added-later"
    assert gs.to_dict()["address"]["ports"]["game"]["protocol"] == "quic"
    # Known values are still the members themselves.
    assert GameServerStatus("running") is GameServerStatus.RUNNING


def test_a_new_error_code_keeps_the_refusal():
    p = get_game_server.sync(client=answering(404, PROBLEM), id=SERVER["id"])
    assert isinstance(p, Problem), p
    assert p.code == "a_code_added_next_month" and p.status == 404 and p.request_id == "req_test"
    assert ErrorCode("not_found") is ErrorCode.NOT_FOUND

"""A call is tried again, up to 3 times in all, on 429 (any call: the API did nothing) and on 503 unavailable (a read, or
a write with its Idempotency-Key, the same key and body on every try), waiting Retry-After up to the cap; never on 503
capacity_unavailable, never past the cap, never with Retry(tries=1). Runs with no API: the answers come from
httpx's mock transport."""

import asyncio
import time

import httpx

from survivalservers_studio import AuthenticatedClient
from survivalservers_studio.api.game_servers import start_game_server
from survivalservers_studio.api.regions import list_regions
from survivalservers_studio.client import Retry
from survivalservers_studio.models import GameServerCreate

SERVER = {
    "id": "gs_a01JA8X9K2Q7M3T5V6W8Y0Z1B2", "status": "starting", "start_mode": "cold",
    "app": "app_a01JA7ZQ4W8E2R6T0Y4U8I2O6P", "version": "2.3.1", "persistent_server": None, "region": "europe-west",
    "continent": "europe", "tier": "standard", "os": "windows", "size": {"cpu": 2, "memory_gb": 4},
    "address": {"ipv4": "203.0.113.24", "ipv6": None, "ports": {"game": {"port": 31042, "protocol": "udp"}}},
    "labels": {}, "players": {"count": 0}, "created_at": "2026-10-09T18:22:04.512Z",
}
REGIONS = {"data": [], "next_cursor": None}


def fake(answers: list, ok: dict, retry: Retry | None = None):
    """A client whose API answers each call with the next of answers ((status, code, Retry-After)), then ok."""
    sent = []

    def handle(request: httpx.Request) -> httpx.Response:
        sent.append((request.method, request.headers.get("Idempotency-Key"), request.content))
        if not answers:
            return httpx.Response(201 if request.method == "POST" else 200, json=ok)
        status, code, after = answers.pop(0)
        headers = {"Retry-After": after} if after is not None else {}
        problem = {"type": f"https://studio.survivalservers.com/docs/reference/errors/#{code}", "title": "Refused",
                   "status": status, "code": code, "request_id": "req_test"}
        return httpx.Response(status, json=problem, headers=headers)

    kw = {"retry": retry} if retry else {}
    client = AuthenticatedClient(base_url="http://127.0.0.1:1", token="gsk_live_EXAMPLE_not_a_real_key",
                                 httpx_args={"transport": httpx.MockTransport(handle)}, **kw)
    return client, sent


def start(client, key=None):
    kw = {"idempotency_key": key} if key else {}
    return start_game_server.sync_detailed(client=client, body=GameServerCreate(app="brawl"), **kw)


def test_429_is_tried_again_with_the_same_body():
    gs, sent = fake([(429, "rate_limited", "0"), (429, "rate_limited", "0")], SERVER)
    assert start(gs).status_code == 201
    assert len(sent) == 3
    assert all(s[2] == sent[0][2] and s[1] == sent[0][1] for s in sent)


def test_three_429s_the_third_answer_comes_back():
    gs, sent = fake([(429, "rate_limited", "0")] * 3, SERVER)
    assert start(gs).status_code == 429
    assert len(sent) == 3


def test_503_unavailable_a_write_with_its_key_the_same_key_every_try():
    gs, sent = fake([(503, "unavailable", "0")], SERVER)
    assert start(gs, "match-42").status_code == 201
    assert [s[1] for s in sent] == ["match-42", "match-42"]


def test_503_unavailable_without_retry_after_waits_a_second():
    gs, sent = fake([(503, "unavailable", None)], REGIONS)
    t0 = time.monotonic()
    assert list_regions.sync_detailed(client=gs).status_code == 200
    assert len(sent) == 2 and time.monotonic() - t0 >= 0.9


def test_503_unavailable_a_write_without_a_key_is_not_tried_again():
    gs, sent = fake([(503, "unavailable", "0")], SERVER)
    assert start(gs).status_code == 503
    assert len(sent) == 1


def test_capacity_unavailable_is_the_callers_call():
    gs, sent = fake([(503, "capacity_unavailable", "0")], SERVER)
    assert start(gs, "match-43").status_code == 503
    assert len(sent) == 1


def test_a_wait_over_the_cap_comes_back_at_once():
    gs, sent = fake([(429, "rate_limited", "120")], SERVER)
    assert start(gs).status_code == 429
    assert len(sent) == 1


def test_tries_1_never_tries_again():
    gs, sent = fake([(429, "rate_limited", "0")], SERVER, Retry(tries=1))
    assert start(gs).status_code == 429
    assert len(sent) == 1


def test_async_calls_are_tried_again_too():
    gs, sent = fake([(503, "unavailable", "0"), (429, "rate_limited", "0")], SERVER)
    r = asyncio.run(start_game_server.asyncio_detailed(client=gs, body=GameServerCreate(app="brawl"), idempotency_key="match-44"))
    assert r.status_code == 201
    assert [s[1] for s in sent] == ["match-44"] * 3

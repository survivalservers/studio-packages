"""A client prints without its API key: repr(), str(), an f-string and pprint of a client, before and after its first
call (which copies the key into its headers), and of the copies with_headers, with_cookies and with_timeout make, show
no part of it. Runs with no API: the answer comes from httpx's mock transport."""

import pprint

import httpx

from survivalservers_studio import AuthenticatedClient, Client, connect
from survivalservers_studio.api.regions import list_regions

KEY = "gsk_live_EXAMPLE_not_a_real_key"
REGIONS = {"data": [], "next_cursor": None}


def printouts(client) -> list[str]:
    return [repr(client), str(client), f"{client}", f"{client!r}", pprint.pformat(client)]


def answer(request: httpx.Request) -> httpx.Response:
    assert request.headers["authorization"] == f"Bearer {KEY}"
    return httpx.Response(200, json=REGIONS)


def test_a_printed_client_shows_no_key():
    mock = {"transport": httpx.MockTransport(answer)}
    for gs in [AuthenticatedClient(base_url="http://127.0.0.1:1", token=KEY, httpx_args=mock),
               connect(KEY, "http://127.0.0.1:1", httpx_args=mock)]:
        before = [gs, gs.with_headers({"X-Trace": "t1"}), gs.with_cookies({"c": "1"}), gs.with_timeout(httpx.Timeout(5.0))]
        for printed in [p for c in before for p in printouts(c)]:
            assert KEY not in printed, printed
            assert printed.startswith("AuthenticatedClient("), printed
        list_regions.sync(client=gs)  # the first call puts "Bearer <key>" in the client's headers
        assert gs._headers["Authorization"] == f"Bearer {KEY}"
        for printed in [p for c in [gs, gs.with_headers({"X-Trace": "t2"})] for p in printouts(c)]:
            assert KEY not in printed, printed
            assert "'Authorization': '***'" in printed, printed


def test_headers_and_cookies_print_by_name_only():
    # A plain Client carries what the caller gives it, a sign-in header or a session cookie included.
    plain = Client(base_url="http://127.0.0.1:1", headers={"Authorization": f"Bearer {KEY}"}, cookies={"session": KEY})
    for printed in printouts(plain):
        assert KEY not in printed, printed
        assert "'Authorization': '***'" in printed and "'session': '***'" in printed, printed

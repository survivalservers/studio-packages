"""What the published package carries beside its code and connect()'s defaults. Runs with no API: the answers come from httpx's mock
transport."""

import pathlib

import httpx
import pytest

import survivalservers_studio
from survivalservers_studio import DEFAULT_TIMEOUT, AuthenticatedClient, connect
from survivalservers_studio.api.branding import get_image
from survivalservers_studio.types import File

PICTURE = b"RIFF\x1a\x00\x00\x00WEBPVP8L\x0d\x00\x00\x00/\x00\x00\x00\x10\x07\x10\x11\x11\x88\x88\xfe\x07\x00"


def test_the_package_says_it_is_typed():
    # PEP 561: without this marker a type checker treats the whole client as untyped.
    assert (pathlib.Path(survivalservers_studio.__file__).parent / "py.typed").is_file()


def test_a_picture_is_read_as_a_file():
    client = AuthenticatedClient(base_url="http://127.0.0.1:1", token="gsk_live_EXAMPLE_not_a_real_key", httpx_args={
        "transport": httpx.MockTransport(
            lambda request: httpx.Response(200, content=PICTURE, headers={"Content-Type": "image/webp"}))})
    picture = get_image.sync(name="icon_a01JA8X9K2Q7M3T5V6W8Y0Z1B2.webp", client=client,
                             expires="1767225600", signature="test")
    assert isinstance(picture, File), picture
    assert picture.payload.read() == PICTURE


def test_connect_has_a_time_limit_and_says_who_is_calling():
    seen = {}

    def answer(request: httpx.Request) -> httpx.Response:
        seen.update(request.headers)
        return httpx.Response(200, content=PICTURE, headers={"Content-Type": "image/webp"})

    gs = connect("gsk_live_EXAMPLE_not_a_real_key", "http://127.0.0.1:1/", httpx_args={"transport": httpx.MockTransport(answer)})
    get_image.sync(name="icon_a01JA8X9K2Q7M3T5V6W8Y0Z1B2.webp", client=gs, expires="1767225600", signature="test")
    assert seen["user-agent"].startswith("survivalservers-studio") and seen["authorization"] == "Bearer gsk_live_EXAMPLE_not_a_real_key"
    assert gs.get_httpx_client().timeout == DEFAULT_TIMEOUT and DEFAULT_TIMEOUT.read == 70.0
    with pytest.raises(ValueError):
        connect("gsk_live_EXAMPLE_not_a_real_key", "")
    with pytest.raises(ValueError):
        connect("", "https://studio.survivalservers.com")

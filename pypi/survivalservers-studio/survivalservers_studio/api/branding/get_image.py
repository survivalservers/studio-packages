from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, File, Response


def _get_kwargs(
    name: str,
    *,
    expires: str,
    signature: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expires"] = expires

    params["signature"] = signature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/images/{name}".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | Problem:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[File | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    expires: str,
    signature: str,
) -> Response[File | Problem]:
    """Get an icon or banner picture

     The picture at an icon's address (`image/webp`) or a banner's (`image/jpeg`). Each address is a
    signed URL that expires: it needs no key and no sign-in, so a web page can show it in an `<img>`,
    but it works only as we handed it out, and only until `expires`, 12 to 24 hours after the answer
    that carried it (the picture's `expires_at`). Read the studio or app again for a fresh address;
    answers in the same 12 hours carry the same one. An address with a changed signature or expiry, or
    after it expires, answers `404`, as a picture that was never there does; one without them answers
    `400`. The name carries a random version that never changes, so the answer may be kept by the
    browser that asked until the address expires (`Cache-Control: private, immutable`), never by a
    shared cache.

    Args:
        name (str):
        expires (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        expires=expires,
        signature=signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    expires: str,
    signature: str,
) -> File | Problem | None:
    """Get an icon or banner picture

     The picture at an icon's address (`image/webp`) or a banner's (`image/jpeg`). Each address is a
    signed URL that expires: it needs no key and no sign-in, so a web page can show it in an `<img>`,
    but it works only as we handed it out, and only until `expires`, 12 to 24 hours after the answer
    that carried it (the picture's `expires_at`). Read the studio or app again for a fresh address;
    answers in the same 12 hours carry the same one. An address with a changed signature or expiry, or
    after it expires, answers `404`, as a picture that was never there does; one without them answers
    `400`. The name carries a random version that never changes, so the answer may be kept by the
    browser that asked until the address expires (`Cache-Control: private, immutable`), never by a
    shared cache.

    Args:
        name (str):
        expires (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Problem
    """

    return sync_detailed(
        name=name,
        client=client,
        expires=expires,
        signature=signature,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    expires: str,
    signature: str,
) -> Response[File | Problem]:
    """Get an icon or banner picture

     The picture at an icon's address (`image/webp`) or a banner's (`image/jpeg`). Each address is a
    signed URL that expires: it needs no key and no sign-in, so a web page can show it in an `<img>`,
    but it works only as we handed it out, and only until `expires`, 12 to 24 hours after the answer
    that carried it (the picture's `expires_at`). Read the studio or app again for a fresh address;
    answers in the same 12 hours carry the same one. An address with a changed signature or expiry, or
    after it expires, answers `404`, as a picture that was never there does; one without them answers
    `400`. The name carries a random version that never changes, so the answer may be kept by the
    browser that asked until the address expires (`Cache-Control: private, immutable`), never by a
    shared cache.

    Args:
        name (str):
        expires (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Problem]
    """

    kwargs = _get_kwargs(
        name=name,
        expires=expires,
        signature=signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    expires: str,
    signature: str,
) -> File | Problem | None:
    """Get an icon or banner picture

     The picture at an icon's address (`image/webp`) or a banner's (`image/jpeg`). Each address is a
    signed URL that expires: it needs no key and no sign-in, so a web page can show it in an `<img>`,
    but it works only as we handed it out, and only until `expires`, 12 to 24 hours after the answer
    that carried it (the picture's `expires_at`). Read the studio or app again for a fresh address;
    answers in the same 12 hours carry the same one. An address with a changed signature or expiry, or
    after it expires, answers `404`, as a picture that was never there does; one without them answers
    `400`. The name carries a random version that never changes, so the answer may be kept by the
    browser that asked until the address expires (`Cache-Control: private, immutable`), never by a
    shared cache.

    Args:
        name (str):
        expires (str):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Problem
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            expires=expires,
            signature=signature,
        )
    ).parsed

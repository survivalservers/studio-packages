from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    token: str,
    *,
    gs_crash_dump: str | Unset = UNSET,
) -> dict[str, Any]:

    cookies = {}
    if gs_crash_dump is not UNSET:
        cookies["gs_crash_dump"] = gs_crash_dump

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/crash-dump-downloads/{token}".format(
            token=quote(str(token), safe=""),
        ),
        "cookies": cookies,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | Problem:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

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
    token: str,
    *,
    client: AuthenticatedClient | Client,
    gs_crash_dump: str | Unset = UNSET,
) -> Response[File | Problem]:
    """Download a crash dump

     The crash dump the link was made for, as the game left it. It needs no key; it needs the cookie its
    link set, so it works only in the browser that asked for it, once, within 2 minutes, while the
    person who asked is still an owner or admin of an active studio with the crash-dump permission and
    two-step sign-in (or the studio's company sign-in). A download from another address than the link's
    answers `403 link_address_changed`: make a new link. Each download is recorded in the audit log with
    that person's name and both addresses. A link that is changed, expired, used or no longer allowed
    answers `404`, as a dump that was never there does. Any refusal of a link in its time (no or a wrong
    cookie, another address, the permission or two-step sign-in gone, a second try) uses it up at once
    and is recorded in the audit log (`crash_dump.download_refused`) with the person it was made for,
    the dump, the address that asked for it, the address refused and the reason. Every answer clears the
    cookie.

    Args:
        token (str):
        gs_crash_dump (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Problem]
    """

    kwargs = _get_kwargs(
        token=token,
        gs_crash_dump=gs_crash_dump,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    gs_crash_dump: str | Unset = UNSET,
) -> File | Problem | None:
    """Download a crash dump

     The crash dump the link was made for, as the game left it. It needs no key; it needs the cookie its
    link set, so it works only in the browser that asked for it, once, within 2 minutes, while the
    person who asked is still an owner or admin of an active studio with the crash-dump permission and
    two-step sign-in (or the studio's company sign-in). A download from another address than the link's
    answers `403 link_address_changed`: make a new link. Each download is recorded in the audit log with
    that person's name and both addresses. A link that is changed, expired, used or no longer allowed
    answers `404`, as a dump that was never there does. Any refusal of a link in its time (no or a wrong
    cookie, another address, the permission or two-step sign-in gone, a second try) uses it up at once
    and is recorded in the audit log (`crash_dump.download_refused`) with the person it was made for,
    the dump, the address that asked for it, the address refused and the reason. Every answer clears the
    cookie.

    Args:
        token (str):
        gs_crash_dump (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Problem
    """

    return sync_detailed(
        token=token,
        client=client,
        gs_crash_dump=gs_crash_dump,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    gs_crash_dump: str | Unset = UNSET,
) -> Response[File | Problem]:
    """Download a crash dump

     The crash dump the link was made for, as the game left it. It needs no key; it needs the cookie its
    link set, so it works only in the browser that asked for it, once, within 2 minutes, while the
    person who asked is still an owner or admin of an active studio with the crash-dump permission and
    two-step sign-in (or the studio's company sign-in). A download from another address than the link's
    answers `403 link_address_changed`: make a new link. Each download is recorded in the audit log with
    that person's name and both addresses. A link that is changed, expired, used or no longer allowed
    answers `404`, as a dump that was never there does. Any refusal of a link in its time (no or a wrong
    cookie, another address, the permission or two-step sign-in gone, a second try) uses it up at once
    and is recorded in the audit log (`crash_dump.download_refused`) with the person it was made for,
    the dump, the address that asked for it, the address refused and the reason. Every answer clears the
    cookie.

    Args:
        token (str):
        gs_crash_dump (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Problem]
    """

    kwargs = _get_kwargs(
        token=token,
        gs_crash_dump=gs_crash_dump,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient | Client,
    gs_crash_dump: str | Unset = UNSET,
) -> File | Problem | None:
    """Download a crash dump

     The crash dump the link was made for, as the game left it. It needs no key; it needs the cookie its
    link set, so it works only in the browser that asked for it, once, within 2 minutes, while the
    person who asked is still an owner or admin of an active studio with the crash-dump permission and
    two-step sign-in (or the studio's company sign-in). A download from another address than the link's
    answers `403 link_address_changed`: make a new link. Each download is recorded in the audit log with
    that person's name and both addresses. A link that is changed, expired, used or no longer allowed
    answers `404`, as a dump that was never there does. Any refusal of a link in its time (no or a wrong
    cookie, another address, the permission or two-step sign-in gone, a second try) uses it up at once
    and is recorded in the audit log (`crash_dump.download_refused`) with the person it was made for,
    the dump, the address that asked for it, the address refused and the reason. Every answer clears the
    cookie.

    Args:
        token (str):
        gs_crash_dump (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Problem
    """

    return (
        await asyncio_detailed(
            token=token,
            client=client,
            gs_crash_dump=gs_crash_dump,
        )
    ).parsed

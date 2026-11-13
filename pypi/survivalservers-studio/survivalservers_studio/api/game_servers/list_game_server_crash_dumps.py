from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.crash_dump_list import CrashDumpList
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/crash-dumps".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CrashDumpList | Problem:
    if response.status_code == 200:
        response_200 = CrashDumpList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CrashDumpList | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CrashDumpList | Problem]:
    """List crash dumps

     The crash dumps kept for a game server, newest first, one for each run that crashed and left one. A
    dump holds the game's whole memory, so only owners and admins who have the crash-dump permission
    (`crash_dumps` on their membership, set with `PATCH /v0/members/{user}`) can list or download one,
    from the panel; no API key can. Anyone else gets `403 missing_scope`. Each was sealed on its machine
    before it left it and is kept for the studio's `crash_dump_retention_hours` (72 by default), then
    deleted; lowering that shortens the dumps already kept too. It goes sooner when its persistent
    server is deleted or the studio closes.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrashDumpList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> CrashDumpList | Problem | None:
    """List crash dumps

     The crash dumps kept for a game server, newest first, one for each run that crashed and left one. A
    dump holds the game's whole memory, so only owners and admins who have the crash-dump permission
    (`crash_dumps` on their membership, set with `PATCH /v0/members/{user}`) can list or download one,
    from the panel; no API key can. Anyone else gets `403 missing_scope`. Each was sealed on its machine
    before it left it and is kept for the studio's `crash_dump_retention_hours` (72 by default), then
    deleted; lowering that shortens the dumps already kept too. It goes sooner when its persistent
    server is deleted or the studio closes.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrashDumpList | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CrashDumpList | Problem]:
    """List crash dumps

     The crash dumps kept for a game server, newest first, one for each run that crashed and left one. A
    dump holds the game's whole memory, so only owners and admins who have the crash-dump permission
    (`crash_dumps` on their membership, set with `PATCH /v0/members/{user}`) can list or download one,
    from the panel; no API key can. Anyone else gets `403 missing_scope`. Each was sealed on its machine
    before it left it and is kept for the studio's `crash_dump_retention_hours` (72 by default), then
    deleted; lowering that shortens the dumps already kept too. It goes sooner when its persistent
    server is deleted or the studio closes.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrashDumpList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> CrashDumpList | Problem | None:
    """List crash dumps

     The crash dumps kept for a game server, newest first, one for each run that crashed and left one. A
    dump holds the game's whole memory, so only owners and admins who have the crash-dump permission
    (`crash_dumps` on their membership, set with `PATCH /v0/members/{user}`) can list or download one,
    from the panel; no API key can. Anyone else gets `403 missing_scope`. Each was sealed on its machine
    before it left it and is kept for the studio's `crash_dump_retention_hours` (72 by default), then
    deleted; lowering that shortens the dumps already kept too. It goes sooner when its persistent
    server is deleted or the studio closes.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrashDumpList | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed

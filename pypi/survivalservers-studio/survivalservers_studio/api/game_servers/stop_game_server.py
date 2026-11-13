from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_server import GameServer
from ...models.game_server_stop import GameServerStop
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: GameServerStop | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/game-servers/{id}/stop".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GameServer | Problem:
    if response.status_code == 202:
        response_202 = GameServer.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GameServer | Problem]:
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
    body: GameServerStop | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GameServer | Problem]:
    """Stop a game server

     Sends the shutdown notice on the local API, then the version's stop method. A game that has asked
    for the notice during its run (`GET /v0/self/shutdown`, as the SDKs and engine add-ons do) gets a
    stop signal only if it is still running halfway through `shutdown_time`; any other game gets it at
    once. After `shutdown_time` (default the version's) the whole process tree is killed, files and
    crash dumps are collected and `game_server.stopped` fires. Already ended - `409 already_stopped`.

    Args:
        id (str): Game server ID.
        idempotency_key (str | Unset):
        body (GameServerStop | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServer | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: GameServerStop | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GameServer | Problem | None:
    """Stop a game server

     Sends the shutdown notice on the local API, then the version's stop method. A game that has asked
    for the notice during its run (`GET /v0/self/shutdown`, as the SDKs and engine add-ons do) gets a
    stop signal only if it is still running halfway through `shutdown_time`; any other game gets it at
    once. After `shutdown_time` (default the version's) the whole process tree is killed, files and
    crash dumps are collected and `game_server.stopped` fires. Already ended - `409 already_stopped`.

    Args:
        id (str): Game server ID.
        idempotency_key (str | Unset):
        body (GameServerStop | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServer | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: GameServerStop | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GameServer | Problem]:
    """Stop a game server

     Sends the shutdown notice on the local API, then the version's stop method. A game that has asked
    for the notice during its run (`GET /v0/self/shutdown`, as the SDKs and engine add-ons do) gets a
    stop signal only if it is still running halfway through `shutdown_time`; any other game gets it at
    once. After `shutdown_time` (default the version's) the whole process tree is killed, files and
    crash dumps are collected and `game_server.stopped` fires. Already ended - `409 already_stopped`.

    Args:
        id (str): Game server ID.
        idempotency_key (str | Unset):
        body (GameServerStop | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServer | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: GameServerStop | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GameServer | Problem | None:
    """Stop a game server

     Sends the shutdown notice on the local API, then the version's stop method. A game that has asked
    for the notice during its run (`GET /v0/self/shutdown`, as the SDKs and engine add-ons do) gets a
    stop signal only if it is still running halfway through `shutdown_time`; any other game gets it at
    once. After `shutdown_time` (default the version's) the whole process tree is killed, files and
    crash dumps are collected and `game_server.stopped` fires. Already ended - `409 already_stopped`.

    Args:
        id (str): Game server ID.
        idempotency_key (str | Unset):
        body (GameServerStop | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServer | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

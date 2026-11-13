from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_server import GameServer
from ...models.game_server_create import GameServerCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GameServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/game-servers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GameServer | Problem:
    if response.status_code == 201:
        response_201 = GameServer.from_dict(response.json())

        return response_201

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

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
    *,
    client: AuthenticatedClient,
    body: GameServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[GameServer | Problem]:
    """Start a game server

     Picks the best region (pings, preferences, readiness), takes a warm game server or launches a new
    one, and
    replies only after the machine has confirmed it, with the final address. A start from a ready server
    is `running` (joinable
    now); a fresh start is `starting` with the address, and `game_server.running` fires when its ready
    check
    passes. A matchmaker's match ID makes a good `Idempotency-Key`.

    Args:
        idempotency_key (str | Unset):
        body (GameServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServer | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GameServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> GameServer | Problem | None:
    """Start a game server

     Picks the best region (pings, preferences, readiness), takes a warm game server or launches a new
    one, and
    replies only after the machine has confirmed it, with the final address. A start from a ready server
    is `running` (joinable
    now); a fresh start is `starting` with the address, and `game_server.running` fires when its ready
    check
    passes. A matchmaker's match ID makes a good `Idempotency-Key`.

    Args:
        idempotency_key (str | Unset):
        body (GameServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServer | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GameServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[GameServer | Problem]:
    """Start a game server

     Picks the best region (pings, preferences, readiness), takes a warm game server or launches a new
    one, and
    replies only after the machine has confirmed it, with the final address. A start from a ready server
    is `running` (joinable
    now); a fresh start is `starting` with the address, and `game_server.running` fires when its ready
    check
    passes. A matchmaker's match ID makes a good `Idempotency-Key`.

    Args:
        idempotency_key (str | Unset):
        body (GameServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServer | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GameServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> GameServer | Problem | None:
    """Start a game server

     Picks the best region (pings, preferences, readiness), takes a warm game server or launches a new
    one, and
    replies only after the machine has confirmed it, with the final address. A start from a ready server
    is `running` (joinable
    now); a fresh start is `starting` with the address, and `game_server.running` fires when its ready
    check
    passes. A matchmaker's match ID makes a good `Idempotency-Key`.

    Args:
        idempotency_key (str | Unset):
        body (GameServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServer | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

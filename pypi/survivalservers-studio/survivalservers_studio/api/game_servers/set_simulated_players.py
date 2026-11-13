from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.simulated_players import SimulatedPlayers
from ...models.simulated_players_set import SimulatedPlayersSet
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SimulatedPlayersSet,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/game-servers/{id}/simulated-players".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SimulatedPlayers:
    if response.status_code == 200:
        response_200 = SimulatedPlayers.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

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
) -> Response[Problem | SimulatedPlayers]:
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
    body: SimulatedPlayersSet,
) -> Response[Problem | SimulatedPlayers]:
    """Set simulated players (our own test setup only)

     Our own test setup only: sets a running game server's simulated player count, for showing a launch
    day on a game no test player can join. The count is labelled simulated in its own data everywhere:
    `simulated_count` beside `players.count` (never in it), a `simulated_players_changed` step, and the
    history's `simulated_players_online`. It never reaches a players event, a webhook, a status card or
    the bill. Anywhere else the call answers `403 lab_only`, whatever its settings, and logs the
    refusal.

    Args:
        id (str): Game server ID.
        body (SimulatedPlayersSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SimulatedPlayers]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SimulatedPlayersSet,
) -> Problem | SimulatedPlayers | None:
    """Set simulated players (our own test setup only)

     Our own test setup only: sets a running game server's simulated player count, for showing a launch
    day on a game no test player can join. The count is labelled simulated in its own data everywhere:
    `simulated_count` beside `players.count` (never in it), a `simulated_players_changed` step, and the
    history's `simulated_players_online`. It never reaches a players event, a webhook, a status card or
    the bill. Anywhere else the call answers `403 lab_only`, whatever its settings, and logs the
    refusal.

    Args:
        id (str): Game server ID.
        body (SimulatedPlayersSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SimulatedPlayers
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SimulatedPlayersSet,
) -> Response[Problem | SimulatedPlayers]:
    """Set simulated players (our own test setup only)

     Our own test setup only: sets a running game server's simulated player count, for showing a launch
    day on a game no test player can join. The count is labelled simulated in its own data everywhere:
    `simulated_count` beside `players.count` (never in it), a `simulated_players_changed` step, and the
    history's `simulated_players_online`. It never reaches a players event, a webhook, a status card or
    the bill. Anywhere else the call answers `403 lab_only`, whatever its settings, and logs the
    refusal.

    Args:
        id (str): Game server ID.
        body (SimulatedPlayersSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SimulatedPlayers]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SimulatedPlayersSet,
) -> Problem | SimulatedPlayers | None:
    """Set simulated players (our own test setup only)

     Our own test setup only: sets a running game server's simulated player count, for showing a launch
    day on a game no test player can join. The count is labelled simulated in its own data everywhere:
    `simulated_count` beside `players.count` (never in it), a `simulated_players_changed` step, and the
    history's `simulated_players_online`. It never reaches a players event, a webhook, a status card or
    the bill. Anywhere else the call answers `403 lab_only`, whatever its settings, and logs the
    refusal.

    Args:
        id (str): Game server ID.
        body (SimulatedPlayersSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SimulatedPlayers
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.log_sources import LogSources
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/logs".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LogSources | Problem:
    if response.status_code == 200:
        response_200 = LogSources.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogSources | Problem]:
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
) -> Response[LogSources | Problem]:
    """List log sources

     The console plus every file in the version's `log_paths`, with the bytes kept. While the server
    runs, what it has sent so far (about every 15 minutes), marked `live`; the console's `bytes` is
    `null` until its first part arrives, though it may already have lines (read them with
    `logs/stream`). Kept 90 days.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogSources | Problem]
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
) -> LogSources | Problem | None:
    """List log sources

     The console plus every file in the version's `log_paths`, with the bytes kept. While the server
    runs, what it has sent so far (about every 15 minutes), marked `live`; the console's `bytes` is
    `null` until its first part arrives, though it may already have lines (read them with
    `logs/stream`). Kept 90 days.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogSources | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[LogSources | Problem]:
    """List log sources

     The console plus every file in the version's `log_paths`, with the bytes kept. While the server
    runs, what it has sent so far (about every 15 minutes), marked `live`; the console's `bytes` is
    `null` until its first part arrives, though it may already have lines (read them with
    `logs/stream`). Kept 90 days.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogSources | Problem]
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
) -> LogSources | Problem | None:
    """List log sources

     The console plus every file in the version's `log_paths`, with the bytes kept. While the server
    runs, what it has sent so far (about every 15 minutes), marked `live`; the console's `bytes` is
    `null` until its first part arrives, though it may already have lines (read them with
    `logs/stream`). Kept 90 days.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogSources | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed

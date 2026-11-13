from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.download_link import DownloadLink
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/logs/archive".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DownloadLink | Problem:
    if response.status_code == 200:
        response_200 = DownloadLink.from_dict(response.json())

        return response_200

    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DownloadLink | Problem]:
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
) -> Response[Any | DownloadLink | Problem]:
    """Download every log as a zip

     Redirects to a zip of every source (while the server runs, the logs kept so far); the link is valid
    15 minutes. A request that accepts JSON (`Accept: application/json`, which generated clients send)
    gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DownloadLink | Problem]
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
) -> Any | DownloadLink | Problem | None:
    """Download every log as a zip

     Redirects to a zip of every source (while the server runs, the logs kept so far); the link is valid
    15 minutes. A request that accepts JSON (`Accept: application/json`, which generated clients send)
    gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DownloadLink | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DownloadLink | Problem]:
    """Download every log as a zip

     Redirects to a zip of every source (while the server runs, the logs kept so far); the link is valid
    15 minutes. A request that accepts JSON (`Accept: application/json`, which generated clients send)
    gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DownloadLink | Problem]
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
) -> Any | DownloadLink | Problem | None:
    """Download every log as a zip

     Redirects to a zip of every source (while the server runs, the logs kept so far); the link is valid
    15 minutes. A request that accepts JSON (`Accept: application/json`, which generated clients send)
    gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Game server ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DownloadLink | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed

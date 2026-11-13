from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.pool import Pool
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    app: str,
    region: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/apps/{app}/pools/{region}".format(
            app=quote(str(app), safe=""),
            region=quote(str(region), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Pool | Problem:
    if response.status_code == 200:
        response_200 = Pool.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Pool | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
) -> Response[Pool | Problem]:
    """Get a region's pool

     The pool's settings and live state.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pool | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
) -> Pool | Problem | None:
    """Get a region's pool

     The pool's settings and live state.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Pool | Problem
    """

    return sync_detailed(
        app=app,
        region=region,
        client=client,
    ).parsed


async def asyncio_detailed(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
) -> Response[Pool | Problem]:
    """Get a region's pool

     The pool's settings and live state.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pool | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
) -> Pool | Problem | None:
    """Get a region's pool

     The pool's settings and live state.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Pool | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            region=region,
            client=client,
        )
    ).parsed

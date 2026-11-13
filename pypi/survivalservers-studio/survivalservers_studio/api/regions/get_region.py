from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.region import Region
from ...types import Response


def _get_kwargs(
    region: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/regions/{region}".format(
            region=quote(str(region), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Region:
    if response.status_code == 200:
        response_200 = Region.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | Region]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | Region]:
    """Get a region

     One region by ID. Region IDs never change.

    Args:
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Region]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: str,
    *,
    client: AuthenticatedClient,
) -> Problem | Region | None:
    """Get a region

     One region by ID. Region IDs never change.

    Args:
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Region
    """

    return sync_detailed(
        region=region,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | Region]:
    """Get a region

     One region by ID. Region IDs never change.

    Args:
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Region]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: str,
    *,
    client: AuthenticatedClient,
) -> Problem | Region | None:
    """Get a region

     One region by ID. Region IDs never change.

    Args:
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Region
    """

    return (
        await asyncio_detailed(
            region=region,
            client=client,
        )
    ).parsed

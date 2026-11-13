from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.pool import Pool
from ...models.pool_put import PoolPut
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    app: str,
    region: str,
    *,
    body: PoolPut,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/apps/{app}/pools/{region}".format(
            app=quote(str(app), safe=""),
            region=quote(str(region), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

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
    body: PoolPut,
) -> Response[Pool | Problem]:
    """Set a region's pool

     `fixed` keeps exactly `min` ready. `auto` sizes the pool from the allocation rate times the build's
    boot time with a safety margin, between `min` and `max`. Saving a pool again, as it is or changed,
    ends a hold (`status.held`): it tries its version again and counts failed starts from zero.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        body (PoolPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pool | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        region=region,
        body=body,
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
    body: PoolPut,
) -> Pool | Problem | None:
    """Set a region's pool

     `fixed` keeps exactly `min` ready. `auto` sizes the pool from the allocation rate times the build's
    boot time with a safety margin, between `min` and `max`. Saving a pool again, as it is or changed,
    ends a hold (`status.held`): it tries its version again and counts failed starts from zero.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        body (PoolPut):

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
        body=body,
    ).parsed


async def asyncio_detailed(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
    body: PoolPut,
) -> Response[Pool | Problem]:
    """Set a region's pool

     `fixed` keeps exactly `min` ready. `auto` sizes the pool from the allocation rate times the build's
    boot time with a safety margin, between `min` and `max`. Saving a pool again, as it is or changed,
    ends a hold (`status.held`): it tries its version again and counts failed starts from zero.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        body (PoolPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pool | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        region=region,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    region: str,
    *,
    client: AuthenticatedClient,
    body: PoolPut,
) -> Pool | Problem | None:
    """Set a region's pool

     `fixed` keeps exactly `min` ready. `auto` sizes the pool from the allocation rate times the build's
    boot time with a safety margin, between `min` and `max`. Saving a pool again, as it is or changed,
    ends a hold (`status.held`): it tries its version again and counts failed starts from zero.

    Args:
        app (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-
            west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        body (PoolPut):

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
            body=body,
        )
    ).parsed

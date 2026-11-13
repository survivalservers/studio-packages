from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.os import Os
from ...models.problem import Problem
from ...models.region_list import RegionList
from ...models.tier import Tier
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    tier: Tier | Unset = UNSET,
    os: Os | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["continent"] = continent

    json_tier: str | Unset = UNSET
    if not isinstance(tier, Unset):
        json_tier = tier.value

    params["tier"] = json_tier

    json_os: str | Unset = UNSET
    if not isinstance(os, Unset):
        json_os = os.value

    params["os"] = json_os

    params["app"] = app

    params["version"] = version

    params["branch"] = branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/regions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RegionList:
    if response.status_code == 200:
        response_200 = RegionList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | RegionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    tier: Tier | Unset = UNSET,
    os: Os | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Response[Problem | RegionList]:
    """List regions

     Every region we list, with what it offers and its ping beacon, when it has one. Add `app` with
    `version` or `branch` to get `version_ready` per region. Needs any valid key and no scope.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        tier (Tier | Unset): Public hardware tier.
        os (Os | Unset):
        app (str | Unset):
        version (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegionList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        continent=continent,
        tier=tier,
        os=os,
        app=app,
        version=version,
        branch=branch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    tier: Tier | Unset = UNSET,
    os: Os | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Problem | RegionList | None:
    """List regions

     Every region we list, with what it offers and its ping beacon, when it has one. Add `app` with
    `version` or `branch` to get `version_ready` per region. Needs any valid key and no scope.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        tier (Tier | Unset): Public hardware tier.
        os (Os | Unset):
        app (str | Unset):
        version (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegionList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        continent=continent,
        tier=tier,
        os=os,
        app=app,
        version=version,
        branch=branch,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    tier: Tier | Unset = UNSET,
    os: Os | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Response[Problem | RegionList]:
    """List regions

     Every region we list, with what it offers and its ping beacon, when it has one. Add `app` with
    `version` or `branch` to get `version_ready` per region. Needs any valid key and no scope.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        tier (Tier | Unset): Public hardware tier.
        os (Os | Unset):
        app (str | Unset):
        version (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegionList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        continent=continent,
        tier=tier,
        os=os,
        app=app,
        version=version,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    tier: Tier | Unset = UNSET,
    os: Os | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Problem | RegionList | None:
    """List regions

     Every region we list, with what it offers and its ping beacon, when it has one. Add `app` with
    `version` or `branch` to get `version_ready` per region. Needs any valid key and no scope.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        tier (Tier | Unset): Public hardware tier.
        os (Os | Unset):
        app (str | Unset):
        version (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegionList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            continent=continent,
            tier=tier,
            os=os,
            app=app,
            version=version,
            branch=branch,
        )
    ).parsed

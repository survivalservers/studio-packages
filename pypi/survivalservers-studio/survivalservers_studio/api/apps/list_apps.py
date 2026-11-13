from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.app_list import AppList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    include_deleted: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/apps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppList | Problem:
    if response.status_code == 200:
        response_200 = AppList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppList | Problem]:
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
    include_deleted: bool | Unset = False,
) -> Response[AppList | Problem]:
    """List apps

     Lists the studio's apps, newest first. With `include_deleted=true` it also lists apps that were
    deleted, each with its `deleted_at`, so a game server, persistent server or usage row that names one
    can still show its name.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        include_deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        include_deleted=include_deleted,
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
    include_deleted: bool | Unset = False,
) -> AppList | Problem | None:
    """List apps

     Lists the studio's apps, newest first. With `include_deleted=true` it also lists apps that were
    deleted, each with its `deleted_at`, so a game server, persistent server or usage row that names one
    can still show its name.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        include_deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    include_deleted: bool | Unset = False,
) -> Response[AppList | Problem]:
    """List apps

     Lists the studio's apps, newest first. With `include_deleted=true` it also lists apps that were
    deleted, each with its `deleted_at`, so a game server, persistent server or usage row that names one
    can still show its name.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        include_deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        include_deleted=include_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    include_deleted: bool | Unset = False,
) -> AppList | Problem | None:
    """List apps

     Lists the studio's apps, newest first. With `include_deleted=true` it also lists apps that were
    deleted, each with its `deleted_at`, so a game server, persistent server or usage row that names one
    can still show its name.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        include_deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            include_deleted=include_deleted,
        )
    ).parsed

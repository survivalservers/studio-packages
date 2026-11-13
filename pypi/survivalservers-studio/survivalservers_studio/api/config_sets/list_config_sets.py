from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.config_set_list import ConfigSetList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["app"] = app

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/config-sets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigSetList | Problem:
    if response.status_code == 200:
        response_200 = ConfigSetList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConfigSetList | Problem]:
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
    app: str | Unset = UNSET,
) -> Response[ConfigSetList | Problem]:
    """List config sets

     Newest first, with how many persistent servers use each.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSetList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
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
    app: str | Unset = UNSET,
) -> ConfigSetList | Problem | None:
    """List config sets

     Newest first, with how many persistent servers use each.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSetList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        app=app,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
) -> Response[ConfigSetList | Problem]:
    """List config sets

     Newest first, with how many persistent servers use each.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSetList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
) -> ConfigSetList | Problem | None:
    """List config sets

     Newest first, with how many persistent servers use each.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSetList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            app=app,
        )
    ).parsed

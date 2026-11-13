from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.version_list import VersionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["deprecated"] = deprecated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/apps/{app}/versions".format(
            app=quote(str(app), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | VersionList:
    if response.status_code == 200:
        response_200 = VersionList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | VersionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
) -> Response[Problem | VersionList]:
    """List versions

     Lists the app's versions, newest first.

    Args:
        app (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        deprecated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionList]
    """

    kwargs = _get_kwargs(
        app=app,
        limit=limit,
        cursor=cursor,
        deprecated=deprecated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
) -> Problem | VersionList | None:
    """List versions

     Lists the app's versions, newest first.

    Args:
        app (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        deprecated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VersionList
    """

    return sync_detailed(
        app=app,
        client=client,
        limit=limit,
        cursor=cursor,
        deprecated=deprecated,
    ).parsed


async def asyncio_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
) -> Response[Problem | VersionList]:
    """List versions

     Lists the app's versions, newest first.

    Args:
        app (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        deprecated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionList]
    """

    kwargs = _get_kwargs(
        app=app,
        limit=limit,
        cursor=cursor,
        deprecated=deprecated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
) -> Problem | VersionList | None:
    """List versions

     Lists the app's versions, newest first.

    Args:
        app (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        deprecated (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VersionList
    """

    return (
        await asyncio_detailed(
            app=app,
            client=client,
            limit=limit,
            cursor=cursor,
            deprecated=deprecated,
        )
    ).parsed

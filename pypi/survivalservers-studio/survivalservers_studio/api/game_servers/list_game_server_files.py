from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_list import FileList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    path: str | Unset = "",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/files".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileList | Problem:
    if response.status_code == 200:
        response_200 = FileList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileList | Problem]:
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
    path: str | Unset = "",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[FileList | Problem]:
    """List files

     While running, a live read-only listing of the game server's folder. After exit, the collected
    files.

    Args:
        id (str): Game server ID.
        path (str | Unset):  Default: ''.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset = "",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> FileList | Problem | None:
    """List files

     While running, a live read-only listing of the game server's folder. After exit, the collected
    files.

    Args:
        id (str): Game server ID.
        path (str | Unset):  Default: ''.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileList | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        path=path,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset = "",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[FileList | Problem]:
    """List files

     While running, a live read-only listing of the game server's folder. After exit, the collected
    files.

    Args:
        id (str): Game server ID.
        path (str | Unset):  Default: ''.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset = "",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> FileList | Problem | None:
    """List files

     While running, a live read-only listing of the game server's folder. After exit, the collected
    files.

    Args:
        id (str): Game server ID.
        path (str | Unset):  Default: ''.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileList | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            path=path,
            limit=limit,
            cursor=cursor,
        )
    ).parsed

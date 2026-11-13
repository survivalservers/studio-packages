from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.download_link import DownloadLink
from ...models.problem import Problem
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    path: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/persistent-servers/{id}/files/download".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
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

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

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
    path: str,
) -> Response[Any | DownloadLink | Problem]:
    """Download a file

     Redirects to a download link valid 15 minutes. A crash dump (a `.dmp`, `.mdmp` or core file) is
    never downloaded as a file (403). A request that accepts JSON (`Accept: application/json`, which
    generated clients send) gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Persistent server ID.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DownloadLink | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Any | DownloadLink | Problem | None:
    """Download a file

     Redirects to a download link valid 15 minutes. A crash dump (a `.dmp`, `.mdmp` or core file) is
    never downloaded as a file (403). A request that accepts JSON (`Accept: application/json`, which
    generated clients send) gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Persistent server ID.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DownloadLink | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Response[Any | DownloadLink | Problem]:
    """Download a file

     Redirects to a download link valid 15 minutes. A crash dump (a `.dmp`, `.mdmp` or core file) is
    never downloaded as a file (403). A request that accepts JSON (`Accept: application/json`, which
    generated clients send) gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Persistent server ID.
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DownloadLink | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Any | DownloadLink | Problem | None:
    """Download a file

     Redirects to a download link valid 15 minutes. A crash dump (a `.dmp`, `.mdmp` or core file) is
    never downloaded as a file (403). A request that accepts JSON (`Accept: application/json`, which
    generated clients send) gets the link as JSON; one that does not (a browser, curl) is redirected.

    Args:
        id (str): Persistent server ID.
        path (str):

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
            path=path,
        )
    ).parsed

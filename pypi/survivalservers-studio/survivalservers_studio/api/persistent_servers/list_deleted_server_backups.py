from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.list_deleted_server_backups_response_200 import (
    ListDeletedServerBackupsResponse200,
)
from ...models.problem import Problem
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/backups/deleted",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListDeletedServerBackupsResponse200 | Problem:
    if response.status_code == 200:
        response_200 = ListDeletedServerBackupsResponse200.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListDeletedServerBackupsResponse200 | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListDeletedServerBackupsResponse200 | Problem]:
    """List backups of deleted servers

     A deleted persistent server's last backup is kept for 90 days, and storage counts while it is.
    Delete one with `DELETE /v0/backups/{id}` to stop paying for it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDeletedServerBackupsResponse200 | Problem]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ListDeletedServerBackupsResponse200 | Problem | None:
    """List backups of deleted servers

     A deleted persistent server's last backup is kept for 90 days, and storage counts while it is.
    Delete one with `DELETE /v0/backups/{id}` to stop paying for it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDeletedServerBackupsResponse200 | Problem
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListDeletedServerBackupsResponse200 | Problem]:
    """List backups of deleted servers

     A deleted persistent server's last backup is kept for 90 days, and storage counts while it is.
    Delete one with `DELETE /v0/backups/{id}` to stop paying for it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDeletedServerBackupsResponse200 | Problem]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ListDeletedServerBackupsResponse200 | Problem | None:
    """List backups of deleted servers

     A deleted persistent server's last backup is kept for 90 days, and storage counts while it is.
    Delete one with `DELETE /v0/backups/{id}` to stop paying for it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDeletedServerBackupsResponse200 | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

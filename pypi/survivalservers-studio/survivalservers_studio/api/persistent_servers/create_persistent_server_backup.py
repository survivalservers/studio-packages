from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup import Backup
from ...models.backup_update import BackupUpdate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: BackupUpdate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers/{id}/backups".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Backup | Problem:
    if response.status_code == 202:
        response_202 = Backup.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Backup | Problem]:
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
    body: BackupUpdate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Backup | Problem]:
    """Take a backup now

     The persistent server must be running (a stopped persistent server's last backup is from its stop).
    `persistent_server.backup_created` fires when it finishes.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Backup | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BackupUpdate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Backup | Problem | None:
    """Take a backup now

     The persistent server must be running (a stopped persistent server's last backup is from its stop).
    `persistent_server.backup_created` fires when it finishes.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Backup | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BackupUpdate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Backup | Problem]:
    """Take a backup now

     The persistent server must be running (a stopped persistent server's last backup is from its stop).
    `persistent_server.backup_created` fires when it finishes.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Backup | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: BackupUpdate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Backup | Problem | None:
    """Take a backup now

     The persistent server must be running (a stopped persistent server's last backup is from its stop).
    `persistent_server.backup_created` fires when it finishes.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Backup | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

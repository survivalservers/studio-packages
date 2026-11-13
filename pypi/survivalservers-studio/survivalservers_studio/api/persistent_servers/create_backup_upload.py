from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_upload import BackupUpload
from ...models.backup_upload_create import BackupUploadCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: BackupUploadCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers/{id}/backups/uploads".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupUpload | Problem:
    if response.status_code == 201:
        response_201 = BackupUpload.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BackupUpload | Problem]:
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
    body: BackupUploadCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BackupUpload | Problem]:
    """Upload a save

     Brings your own saves in as an `imported` backup. `PUT` a zip to `url`, then call complete. Entries
    go under the persistent server's save paths: by their own names, or with one save path, inside it.
    This does not touch the server: restore the backup when you want it, with the usual undo. At most 5
    GiB.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUploadCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
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
    body: BackupUploadCreate,
    idempotency_key: str | Unset = UNSET,
) -> BackupUpload | Problem | None:
    """Upload a save

     Brings your own saves in as an `imported` backup. `PUT` a zip to `url`, then call complete. Entries
    go under the persistent server's save paths: by their own names, or with one save path, inside it.
    This does not touch the server: restore the backup when you want it, with the usual undo. At most 5
    GiB.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUploadCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupUpload | Problem
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
    body: BackupUploadCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BackupUpload | Problem]:
    """Upload a save

     Brings your own saves in as an `imported` backup. `PUT` a zip to `url`, then call complete. Entries
    go under the persistent server's save paths: by their own names, or with one save path, inside it.
    This does not touch the server: restore the backup when you want it, with the usual undo. At most 5
    GiB.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUploadCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
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
    body: BackupUploadCreate,
    idempotency_key: str | Unset = UNSET,
) -> BackupUpload | Problem | None:
    """Upload a save

     Brings your own saves in as an `imported` backup. `PUT` a zip to `url`, then call complete. Entries
    go under the persistent server's save paths: by their own names, or with one save path, inside it.
    This does not touch the server: restore the backup when you want it, with the usual undo. At most 5
    GiB.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (BackupUploadCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupUpload | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

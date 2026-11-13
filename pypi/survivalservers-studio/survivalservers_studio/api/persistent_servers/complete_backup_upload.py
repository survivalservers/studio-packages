from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_upload import BackupUpload
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    upload_id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers/{id}/backups/uploads/{upload_id}/complete".format(
            id=quote(str(id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupUpload | Problem:
    if response.status_code == 202:
        response_202 = BackupUpload.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
    upload_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[BackupUpload | Problem]:
    """Finish an upload

     The zip is up. We check it and cut it into the server's backups; a zip that leaves the save paths is
    refused whole.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        upload_id=upload_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> BackupUpload | Problem | None:
    """Finish an upload

     The zip is up. We check it and cut it into the server's backups; a zip that leaves the save paths is
    refused whole.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupUpload | Problem
    """

    return sync_detailed(
        id=id,
        upload_id=upload_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[BackupUpload | Problem]:
    """Finish an upload

     The zip is up. We check it and cut it into the server's backups; a zip that leaves the save paths is
    refused whole.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        upload_id=upload_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> BackupUpload | Problem | None:
    """Finish an upload

     The zip is up. We check it and cut it into the server's backups; a zip that leaves the save paths is
    refused whole.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupUpload | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            upload_id=upload_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_upload import BackupUpload
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    id: str,
    upload_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/persistent-servers/{id}/backups/uploads/{upload_id}".format(
            id=quote(str(id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupUpload | Problem:
    if response.status_code == 200:
        response_200 = BackupUpload.from_dict(response.json())

        return response_200

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
) -> Response[BackupUpload | Problem]:
    """Read an upload

     How it stands; once `done` it names the backup it became.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        upload_id=upload_id,
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
) -> BackupUpload | Problem | None:
    """Read an upload

     How it stands; once `done` it names the backup it became.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.

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
    ).parsed


async def asyncio_detailed(
    id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BackupUpload | Problem]:
    """Read an upload

     How it stands; once `done` it names the backup it became.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupUpload | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        upload_id=upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> BackupUpload | Problem | None:
    """Read an upload

     How it stands; once `done` it names the backup it became.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.

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
        )
    ).parsed

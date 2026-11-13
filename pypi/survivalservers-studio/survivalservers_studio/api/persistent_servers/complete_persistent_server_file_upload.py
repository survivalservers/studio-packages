from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.persistent_server_file_upload import PersistentServerFileUpload
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
        "url": "/v0/persistent-servers/{id}/files/uploads/{upload_id}/complete".format(
            id=quote(str(id), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PersistentServerFileUpload | Problem:
    if response.status_code == 202:
        response_202 = PersistentServerFileUpload.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PersistentServerFileUpload | Problem]:
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
) -> Response[PersistentServerFileUpload | Problem]:
    """Finish a file upload

     Checks the checksum and puts the file in place. `429` while the machine copies another file of this
    folder (try again in a few seconds), `503` when the machine does not answer.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerFileUpload | Problem]
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
) -> PersistentServerFileUpload | Problem | None:
    """Finish a file upload

     Checks the checksum and puts the file in place. `429` while the machine copies another file of this
    folder (try again in a few seconds), `503` when the machine does not answer.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerFileUpload | Problem
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
) -> Response[PersistentServerFileUpload | Problem]:
    """Finish a file upload

     Checks the checksum and puts the file in place. `429` while the machine copies another file of this
    folder (try again in a few seconds), `503` when the machine does not answer.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerFileUpload | Problem]
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
) -> PersistentServerFileUpload | Problem | None:
    """Finish a file upload

     Checks the checksum and puts the file in place. `429` while the machine copies another file of this
    folder (try again in a few seconds), `503` when the machine does not answer.

    Args:
        id (str): Persistent server ID.
        upload_id (str): Persistent server file upload ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerFileUpload | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            upload_id=upload_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed

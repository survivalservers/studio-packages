from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action import BulkAction
from ...models.bulk_action_resume import BulkActionResume
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: BulkActionResume | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/{id}/resume".format(
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
) -> BulkAction | Problem:
    if response.status_code == 202:
        response_202 = BulkAction.from_dict(response.json())

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
) -> Response[BulkAction | Problem]:
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
    body: BulkActionResume | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkAction | Problem]:
    """Resume a bulk action

     A paused or stopped bulk action goes on with its next step; the failures so far still count against
    `max_failures` unless `reset_failures` is set.

    Args:
        id (str): Bulk action ID.
        idempotency_key (str | Unset):
        body (BulkActionResume | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkAction | Problem]
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
    body: BulkActionResume | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BulkAction | Problem | None:
    """Resume a bulk action

     A paused or stopped bulk action goes on with its next step; the failures so far still count against
    `max_failures` unless `reset_failures` is set.

    Args:
        id (str): Bulk action ID.
        idempotency_key (str | Unset):
        body (BulkActionResume | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkAction | Problem
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
    body: BulkActionResume | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkAction | Problem]:
    """Resume a bulk action

     A paused or stopped bulk action goes on with its next step; the failures so far still count against
    `max_failures` unless `reset_failures` is set.

    Args:
        id (str): Bulk action ID.
        idempotency_key (str | Unset):
        body (BulkActionResume | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkAction | Problem]
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
    body: BulkActionResume | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BulkAction | Problem | None:
    """Resume a bulk action

     A paused or stopped bulk action goes on with its next step; the failures so far still count against
    `max_failures` unless `reset_failures` is set.

    Args:
        id (str): Bulk action ID.
        idempotency_key (str | Unset):
        body (BulkActionResume | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkAction | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

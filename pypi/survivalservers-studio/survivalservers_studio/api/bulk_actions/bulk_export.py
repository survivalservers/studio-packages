from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_export_create import BulkActionExportCreate
from ...models.bulk_action_result import BulkActionResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkActionExportCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/exports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkActionResult | Problem:
    if response.status_code == 200:
        response_200 = BulkActionResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = BulkActionResult.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkActionResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkActionExportCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Export backups

     Builds one zip per persistent server, of its newest backup, or its newest from before `at`. Nothing
    about the servers changes. Each target of the bulk action carries its link once its zip is ready;
    zips are kept for 24 hours. With `dry_run` the answer is what it would export.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionExportCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionResult | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BulkActionExportCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Export backups

     Builds one zip per persistent server, of its newest backup, or its newest from before `at`. Nothing
    about the servers changes. Each target of the bulk action carries its link once its zip is ready;
    zips are kept for 24 hours. With `dry_run` the answer is what it would export.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionExportCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionResult | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkActionExportCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Export backups

     Builds one zip per persistent server, of its newest backup, or its newest from before `at`. Nothing
    about the servers changes. Each target of the bulk action carries its link once its zip is ready;
    zips are kept for 24 hours. With `dry_run` the answer is what it would export.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionExportCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionResult | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkActionExportCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Export backups

     Builds one zip per persistent server, of its newest backup, or its newest from before `at`. Nothing
    about the servers changes. Each target of the bulk action carries its link once its zip is ready;
    zips are kept for 24 hours. With `dry_run` the answer is what it would export.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionExportCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionResult | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

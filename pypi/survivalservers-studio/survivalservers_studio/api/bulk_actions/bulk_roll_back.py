from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_result import BulkActionResult
from ...models.bulk_action_rollback_create import BulkActionRollbackCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkActionRollbackCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/rollbacks",
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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

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
    body: BulkActionRollbackCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Roll back persistent servers

     Goes back to before a time, or to before a rollout's update, on many persistent servers at once.
    Send the selector and `at` (or `before_update`) for a preview, which names the backup each server
    would go back to, how much play it would lose and what would be left out, and carries an `id`. Send
    that `id` as `plan` within 15 minutes to run exactly that preview; if a server or a backup changed
    since, the answer is `409 plan_changed`. Each server is saved and stopped, its current state is
    backed up, then it is restored, started and checked. Undo puts every server back to how it was just
    before.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRollbackCreate): Send `selector` and `at` (or `before_update`) for a
            preview; send the preview's `id` as `plan` to run it.

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
    body: BulkActionRollbackCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Roll back persistent servers

     Goes back to before a time, or to before a rollout's update, on many persistent servers at once.
    Send the selector and `at` (or `before_update`) for a preview, which names the backup each server
    would go back to, how much play it would lose and what would be left out, and carries an `id`. Send
    that `id` as `plan` within 15 minutes to run exactly that preview; if a server or a backup changed
    since, the answer is `409 plan_changed`. Each server is saved and stopped, its current state is
    backed up, then it is restored, started and checked. Undo puts every server back to how it was just
    before.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRollbackCreate): Send `selector` and `at` (or `before_update`) for a
            preview; send the preview's `id` as `plan` to run it.

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
    body: BulkActionRollbackCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Roll back persistent servers

     Goes back to before a time, or to before a rollout's update, on many persistent servers at once.
    Send the selector and `at` (or `before_update`) for a preview, which names the backup each server
    would go back to, how much play it would lose and what would be left out, and carries an `id`. Send
    that `id` as `plan` within 15 minutes to run exactly that preview; if a server or a backup changed
    since, the answer is `409 plan_changed`. Each server is saved and stopped, its current state is
    backed up, then it is restored, started and checked. Undo puts every server back to how it was just
    before.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRollbackCreate): Send `selector` and `at` (or `before_update`) for a
            preview; send the preview's `id` as `plan` to run it.

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
    body: BulkActionRollbackCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Roll back persistent servers

     Goes back to before a time, or to before a rollout's update, on many persistent servers at once.
    Send the selector and `at` (or `before_update`) for a preview, which names the backup each server
    would go back to, how much play it would lose and what would be left out, and carries an `id`. Send
    that `id` as `plan` within 15 minutes to run exactly that preview; if a server or a backup changed
    since, the answer is `409 plan_changed`. Each server is saved and stopped, its current state is
    backed up, then it is restored, started and checked. Undo puts every server back to how it was just
    before.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRollbackCreate): Send `selector` and `at` (or `before_update`) for a
            preview; send the preview's `id` as `plan` to run it.

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

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_result import BulkActionResult
from ...models.bulk_action_rollout_create import BulkActionRolloutCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkActionRolloutCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/rollouts",
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

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

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
    body: BulkActionRolloutCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Roll out a version

     Puts every persistent server or pool the selector matches on a version (or a branch). Persistent
    servers take it at their next restart, or with `apply` `now` a few at a time, stopping on failures
    like a restart. Pools replace their waiting game servers, in batches like a restart: a pool counts
    as done once as many ready servers as it keeps (at least one) are ready on the new version and have
    run `healthy_for`. Its first game server on the new version that ends on its own before a start
    takes it fails the pool (`boot_failed`, or `crashed` after its ready check): the pool goes back to
    its earlier version at once, its old ready servers kept, and that failure counts toward
    `max_failures`. Every target's previous version is kept, so `POST /v0/bulk-actions/{id}/undo` moves
    them back. Targeting pools also needs `apps:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRolloutCreate):

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
    body: BulkActionRolloutCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Roll out a version

     Puts every persistent server or pool the selector matches on a version (or a branch). Persistent
    servers take it at their next restart, or with `apply` `now` a few at a time, stopping on failures
    like a restart. Pools replace their waiting game servers, in batches like a restart: a pool counts
    as done once as many ready servers as it keeps (at least one) are ready on the new version and have
    run `healthy_for`. Its first game server on the new version that ends on its own before a start
    takes it fails the pool (`boot_failed`, or `crashed` after its ready check): the pool goes back to
    its earlier version at once, its old ready servers kept, and that failure counts toward
    `max_failures`. Every target's previous version is kept, so `POST /v0/bulk-actions/{id}/undo` moves
    them back. Targeting pools also needs `apps:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRolloutCreate):

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
    body: BulkActionRolloutCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Roll out a version

     Puts every persistent server or pool the selector matches on a version (or a branch). Persistent
    servers take it at their next restart, or with `apply` `now` a few at a time, stopping on failures
    like a restart. Pools replace their waiting game servers, in batches like a restart: a pool counts
    as done once as many ready servers as it keeps (at least one) are ready on the new version and have
    run `healthy_for`. Its first game server on the new version that ends on its own before a start
    takes it fails the pool (`boot_failed`, or `crashed` after its ready check): the pool goes back to
    its earlier version at once, its old ready servers kept, and that failure counts toward
    `max_failures`. Every target's previous version is kept, so `POST /v0/bulk-actions/{id}/undo` moves
    them back. Targeting pools also needs `apps:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRolloutCreate):

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
    body: BulkActionRolloutCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Roll out a version

     Puts every persistent server or pool the selector matches on a version (or a branch). Persistent
    servers take it at their next restart, or with `apply` `now` a few at a time, stopping on failures
    like a restart. Pools replace their waiting game servers, in batches like a restart: a pool counts
    as done once as many ready servers as it keeps (at least one) are ready on the new version and have
    run `healthy_for`. Its first game server on the new version that ends on its own before a start
    takes it fails the pool (`boot_failed`, or `crashed` after its ready check): the pool goes back to
    its earlier version at once, its old ready servers kept, and that failure counts toward
    `max_failures`. Every target's previous version is kept, so `POST /v0/bulk-actions/{id}/undo` moves
    them back. Targeting pools also needs `apps:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRolloutCreate):

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

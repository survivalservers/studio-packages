from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_restart_create import BulkActionRestartCreate
from ...models.bulk_action_result import BulkActionResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkActionRestartCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/restarts",
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
    body: BulkActionRestartCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Restart many persistent servers

     Restarts every running persistent server the selector matches in rolling batches: each one saves
    (the version's save command), takes its stop backup and starts again on the same machine and
    address. A batch is done when its persistent servers are running again and stayed up for
    `rollout.healthy_for`; the action stops once more persistent servers failed than
    `rollout.max_failures` allows. `at` starts it later.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRestartCreate):

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
    body: BulkActionRestartCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Restart many persistent servers

     Restarts every running persistent server the selector matches in rolling batches: each one saves
    (the version's save command), takes its stop backup and starts again on the same machine and
    address. A batch is done when its persistent servers are running again and stayed up for
    `rollout.healthy_for`; the action stops once more persistent servers failed than
    `rollout.max_failures` allows. `at` starts it later.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRestartCreate):

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
    body: BulkActionRestartCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Restart many persistent servers

     Restarts every running persistent server the selector matches in rolling batches: each one saves
    (the version's save command), takes its stop backup and starts again on the same machine and
    address. A batch is done when its persistent servers are running again and stayed up for
    `rollout.healthy_for`; the action stops once more persistent servers failed than
    `rollout.max_failures` allows. `at` starts it later.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRestartCreate):

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
    body: BulkActionRestartCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Restart many persistent servers

     Restarts every running persistent server the selector matches in rolling batches: each one saves
    (the version's save command), takes its stop backup and starts again on the same machine and
    address. A batch is done when its persistent servers are running again and stayed up for
    `rollout.healthy_for`; the action stops once more persistent servers failed than
    `rollout.max_failures` allows. `at` starts it later.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionRestartCreate):

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

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_command_create import BulkActionCommandCreate
from ...models.bulk_action_result import BulkActionResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkActionCommandCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/bulk-actions/commands",
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
    body: BulkActionCommandCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Send a command to many

     Sends one console line, RCON command or HTTP call to every running persistent server or game server
    the selector matches, in batches. With `dry_run` nothing is sent: the answer is the plan (targets,
    batches, skipped ones and why). Targeting game servers also needs `game_servers:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionCommandCreate): Give one of `command`, a saved command's `command_id` with
            its `args`, or a `line` sent through a connection (`via`). A saved command or a connection
            is read from each target's own version, so targets on different versions can run it
            differently. Targets whose version has no such command or connection are skipped
            (`no_command`).

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
    body: BulkActionCommandCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Send a command to many

     Sends one console line, RCON command or HTTP call to every running persistent server or game server
    the selector matches, in batches. With `dry_run` nothing is sent: the answer is the plan (targets,
    batches, skipped ones and why). Targeting game servers also needs `game_servers:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionCommandCreate): Give one of `command`, a saved command's `command_id` with
            its `args`, or a `line` sent through a connection (`via`). A saved command or a connection
            is read from each target's own version, so targets on different versions can run it
            differently. Targets whose version has no such command or connection are skipped
            (`no_command`).

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
    body: BulkActionCommandCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Send a command to many

     Sends one console line, RCON command or HTTP call to every running persistent server or game server
    the selector matches, in batches. With `dry_run` nothing is sent: the answer is the plan (targets,
    batches, skipped ones and why). Targeting game servers also needs `game_servers:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionCommandCreate): Give one of `command`, a saved command's `command_id` with
            its `args`, or a `line` sent through a connection (`via`). A saved command or a connection
            is read from each target's own version, so targets on different versions can run it
            differently. Targets whose version has no such command or connection are skipped
            (`no_command`).

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
    body: BulkActionCommandCreate,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Send a command to many

     Sends one console line, RCON command or HTTP call to every running persistent server or game server
    the selector matches, in batches. With `dry_run` nothing is sent: the answer is the plan (targets,
    batches, skipped ones and why). Targeting game servers also needs `game_servers:write`.

    Args:
        idempotency_key (str | Unset):
        body (BulkActionCommandCreate): Give one of `command`, a saved command's `command_id` with
            its `args`, or a `line` sent through a connection (`via`). A saved command or a connection
            is read from each target's own version, so targets on different versions can run it
            differently. Targets whose version has no such command or connection are skipped
            (`no_command`).

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

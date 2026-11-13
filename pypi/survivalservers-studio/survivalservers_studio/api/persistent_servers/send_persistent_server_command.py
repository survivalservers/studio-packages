from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.command_result import CommandResult
from ...models.command_send import CommandSend
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CommandSend,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers/{id}/command".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommandResult | Problem:
    if response.status_code == 200:
        response_200 = CommandResult.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[CommandResult | Problem]:
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
    body: CommandSend,
    idempotency_key: str | Unset = UNSET,
) -> Response[CommandResult | Problem]:
    """Send a game command

     Sends a console line, an RCON command or an HTTP call to the persistent server's running game and
    answers with what came back: the RCON reply, the HTTP status and body, or the console lines written
    within `capture`. `409 invalid_state` when the persistent server is not running (or is paused).
    Recorded in the audit log.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (CommandSend): Give one of `command`, a saved command's `command_id` with its `args`,
            or a `line` sent through a connection (`via`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommandResult | Problem]
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
    body: CommandSend,
    idempotency_key: str | Unset = UNSET,
) -> CommandResult | Problem | None:
    """Send a game command

     Sends a console line, an RCON command or an HTTP call to the persistent server's running game and
    answers with what came back: the RCON reply, the HTTP status and body, or the console lines written
    within `capture`. `409 invalid_state` when the persistent server is not running (or is paused).
    Recorded in the audit log.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (CommandSend): Give one of `command`, a saved command's `command_id` with its `args`,
            or a `line` sent through a connection (`via`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommandResult | Problem
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
    body: CommandSend,
    idempotency_key: str | Unset = UNSET,
) -> Response[CommandResult | Problem]:
    """Send a game command

     Sends a console line, an RCON command or an HTTP call to the persistent server's running game and
    answers with what came back: the RCON reply, the HTTP status and body, or the console lines written
    within `capture`. `409 invalid_state` when the persistent server is not running (or is paused).
    Recorded in the audit log.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (CommandSend): Give one of `command`, a saved command's `command_id` with its `args`,
            or a `line` sent through a connection (`via`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommandResult | Problem]
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
    body: CommandSend,
    idempotency_key: str | Unset = UNSET,
) -> CommandResult | Problem | None:
    """Send a game command

     Sends a console line, an RCON command or an HTTP call to the persistent server's running game and
    answers with what came back: the RCON reply, the HTTP status and body, or the console lines written
    within `capture`. `409 invalid_state` when the persistent server is not running (or is paused).
    Recorded in the audit log.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (CommandSend): Give one of `command`, a saved command's `command_id` with its `args`,
            or a `line` sent through a connection (`via`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommandResult | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

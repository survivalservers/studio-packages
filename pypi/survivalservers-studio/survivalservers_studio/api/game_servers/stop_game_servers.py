from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_stop_result import BulkStopResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Any,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/game-servers/stop",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkStopResult | Problem:
    if response.status_code == 202:
        response_202 = BulkStopResult.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkStopResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Any,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkStopResult | Problem]:
    """Stop many game servers

     Stops every running game server that matches all the given filters (at least one of `app`,
    `version`, `region`, `labels`). Returns how many were asked to stop. Each call writes one audit
    line, `game_servers.stop`, with the count in `details.count`.

    Args:
        idempotency_key (str | Unset):
        body (Any): At least one of `app`, `version`, `region`, `labels`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkStopResult | Problem]
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
    body: Any,
    idempotency_key: str | Unset = UNSET,
) -> BulkStopResult | Problem | None:
    """Stop many game servers

     Stops every running game server that matches all the given filters (at least one of `app`,
    `version`, `region`, `labels`). Returns how many were asked to stop. Each call writes one audit
    line, `game_servers.stop`, with the count in `details.count`.

    Args:
        idempotency_key (str | Unset):
        body (Any): At least one of `app`, `version`, `region`, `labels`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkStopResult | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Any,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkStopResult | Problem]:
    """Stop many game servers

     Stops every running game server that matches all the given filters (at least one of `app`,
    `version`, `region`, `labels`). Returns how many were asked to stop. Each call writes one audit
    line, `game_servers.stop`, with the count in `details.count`.

    Args:
        idempotency_key (str | Unset):
        body (Any): At least one of `app`, `version`, `region`, `labels`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkStopResult | Problem]
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
    body: Any,
    idempotency_key: str | Unset = UNSET,
) -> BulkStopResult | Problem | None:
    """Stop many game servers

     Stops every running game server that matches all the given filters (at least one of `app`,
    `version`, `region`, `labels`). Returns how many were asked to stop. Each call writes one audit
    line, `game_servers.stop`, with the count in `details.count`.

    Args:
        idempotency_key (str | Unset):
        body (Any): At least one of `app`, `version`, `region`, `labels`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkStopResult | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

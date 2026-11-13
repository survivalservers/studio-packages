from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.webhook_endpoint_create import WebhookEndpointCreate
from ...models.webhook_endpoint_with_secret import WebhookEndpointWithSecret
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WebhookEndpointCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/webhook-endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEndpointWithSecret:
    if response.status_code == 201:
        response_201 = WebhookEndpointWithSecret.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | WebhookEndpointWithSecret]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | WebhookEndpointWithSecret]:
    """Add a webhook endpoint

     The signing secret is in this reply only. Mark one endpoint `default`; its secret also signs per-
    request `webhook_url` deliveries. Set `format` to `slack` or `discord` to send short messages to a
    channel instead: repeats of one kind fold into one summary every 10 minutes. A key limited to some
    apps makes endpoints for its own apps only (its apps when `apps` is left out), never the default,
    and never one that takes billing or bulk action events (its endpoints take every other event type
    unless `events` says less).

    Args:
        idempotency_key (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointWithSecret]
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
    body: WebhookEndpointCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | WebhookEndpointWithSecret | None:
    """Add a webhook endpoint

     The signing secret is in this reply only. Mark one endpoint `default`; its secret also signs per-
    request `webhook_url` deliveries. Set `format` to `slack` or `discord` to send short messages to a
    channel instead: repeats of one kind fold into one summary every 10 minutes. A key limited to some
    apps makes endpoints for its own apps only (its apps when `apps` is left out), never the default,
    and never one that takes billing or bulk action events (its endpoints take every other event type
    unless `events` says less).

    Args:
        idempotency_key (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointWithSecret
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | WebhookEndpointWithSecret]:
    """Add a webhook endpoint

     The signing secret is in this reply only. Mark one endpoint `default`; its secret also signs per-
    request `webhook_url` deliveries. Set `format` to `slack` or `discord` to send short messages to a
    channel instead: repeats of one kind fold into one summary every 10 minutes. A key limited to some
    apps makes endpoints for its own apps only (its apps when `apps` is left out), never the default,
    and never one that takes billing or bulk action events (its endpoints take every other event type
    unless `events` says less).

    Args:
        idempotency_key (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpointWithSecret]
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
    body: WebhookEndpointCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | WebhookEndpointWithSecret | None:
    """Add a webhook endpoint

     The signing secret is in this reply only. Mark one endpoint `default`; its secret also signs per-
    request `webhook_url` deliveries. Set `format` to `slack` or `discord` to send short messages to a
    channel instead: repeats of one kind fold into one summary every 10 minutes. A key limited to some
    apps makes endpoints for its own apps only (its apps when `apps` is left out), never the default,
    and never one that takes billing or bulk action events (its endpoints take every other event type
    unless `events` says less).

    Args:
        idempotency_key (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpointWithSecret
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

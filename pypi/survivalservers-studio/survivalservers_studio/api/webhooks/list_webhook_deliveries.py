from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delivery_status import DeliveryStatus
from ...models.event_type import EventType
from ...models.problem import Problem
from ...models.webhook_delivery_list import WebhookDeliveryList
from ...models.webhook_format import WebhookFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    endpoint: str | Unset = UNSET,
    event: str | Unset = UNSET,
    status: DeliveryStatus | Unset = UNSET,
    type_: EventType | Unset = UNSET,
    format_: list[WebhookFormat] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["endpoint"] = endpoint

    params["event"] = event

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_format_: list[str] | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = []
        for format_item_data in format_:
            format_item = format_item_data.value
            json_format_.append(format_item)

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/webhook-deliveries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookDeliveryList:
    if response.status_code == 200:
        response_200 = WebhookDeliveryList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | WebhookDeliveryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    endpoint: str | Unset = UNSET,
    event: str | Unset = UNSET,
    status: DeliveryStatus | Unset = UNSET,
    type_: EventType | Unset = UNSET,
    format_: list[WebhookFormat] | Unset = UNSET,
) -> Response[Problem | WebhookDeliveryList]:
    """List delivery attempts

     Every attempt with HTTP status, timing and the start of the response, newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        endpoint (str | Unset): Webhook endpoint ID.
        event (str | Unset): Event ID; also the `webhook-id` of its webhooks.
        status (DeliveryStatus | Unset):
        type_ (EventType | Unset): `game_server.starting`, `game_server.stopping`,
            `game_server.players_changed`, `persistent_server.starting`, `persistent_server.stopping`,
            `persistent_server.paused`, `persistent_server.resuming`, `persistent_server.resumed` and
            `bulk_action.progress` are for watching: in the event stream only, never sent to webhook
            endpoints (so never among deliveries). New types may be added (section 1.1).
        format_ (list[WebhookFormat] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookDeliveryList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        endpoint=endpoint,
        event=event,
        status=status,
        type_=type_,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    endpoint: str | Unset = UNSET,
    event: str | Unset = UNSET,
    status: DeliveryStatus | Unset = UNSET,
    type_: EventType | Unset = UNSET,
    format_: list[WebhookFormat] | Unset = UNSET,
) -> Problem | WebhookDeliveryList | None:
    """List delivery attempts

     Every attempt with HTTP status, timing and the start of the response, newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        endpoint (str | Unset): Webhook endpoint ID.
        event (str | Unset): Event ID; also the `webhook-id` of its webhooks.
        status (DeliveryStatus | Unset):
        type_ (EventType | Unset): `game_server.starting`, `game_server.stopping`,
            `game_server.players_changed`, `persistent_server.starting`, `persistent_server.stopping`,
            `persistent_server.paused`, `persistent_server.resuming`, `persistent_server.resumed` and
            `bulk_action.progress` are for watching: in the event stream only, never sent to webhook
            endpoints (so never among deliveries). New types may be added (section 1.1).
        format_ (list[WebhookFormat] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookDeliveryList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        endpoint=endpoint,
        event=event,
        status=status,
        type_=type_,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    endpoint: str | Unset = UNSET,
    event: str | Unset = UNSET,
    status: DeliveryStatus | Unset = UNSET,
    type_: EventType | Unset = UNSET,
    format_: list[WebhookFormat] | Unset = UNSET,
) -> Response[Problem | WebhookDeliveryList]:
    """List delivery attempts

     Every attempt with HTTP status, timing and the start of the response, newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        endpoint (str | Unset): Webhook endpoint ID.
        event (str | Unset): Event ID; also the `webhook-id` of its webhooks.
        status (DeliveryStatus | Unset):
        type_ (EventType | Unset): `game_server.starting`, `game_server.stopping`,
            `game_server.players_changed`, `persistent_server.starting`, `persistent_server.stopping`,
            `persistent_server.paused`, `persistent_server.resuming`, `persistent_server.resumed` and
            `bulk_action.progress` are for watching: in the event stream only, never sent to webhook
            endpoints (so never among deliveries). New types may be added (section 1.1).
        format_ (list[WebhookFormat] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookDeliveryList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        endpoint=endpoint,
        event=event,
        status=status,
        type_=type_,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    endpoint: str | Unset = UNSET,
    event: str | Unset = UNSET,
    status: DeliveryStatus | Unset = UNSET,
    type_: EventType | Unset = UNSET,
    format_: list[WebhookFormat] | Unset = UNSET,
) -> Problem | WebhookDeliveryList | None:
    """List delivery attempts

     Every attempt with HTTP status, timing and the start of the response, newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        endpoint (str | Unset): Webhook endpoint ID.
        event (str | Unset): Event ID; also the `webhook-id` of its webhooks.
        status (DeliveryStatus | Unset):
        type_ (EventType | Unset): `game_server.starting`, `game_server.stopping`,
            `game_server.players_changed`, `persistent_server.starting`, `persistent_server.stopping`,
            `persistent_server.paused`, `persistent_server.resuming`, `persistent_server.resumed` and
            `bulk_action.progress` are for watching: in the event stream only, never sent to webhook
            endpoints (so never among deliveries). New types may be added (section 1.1).
        format_ (list[WebhookFormat] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookDeliveryList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            endpoint=endpoint,
            event=event,
            status=status,
            type_=type_,
            format_=format_,
        )
    ).parsed

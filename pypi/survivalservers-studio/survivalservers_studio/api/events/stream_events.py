from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    types: list[str] | Unset = UNSET,
    last_event_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id

    params: dict[str, Any] = {}

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/events/stream",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | str:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    types: list[str] | Unset = UNSET,
    last_event_id: str | Unset = UNSET,
) -> Response[Problem | str]:
    """Follow events live

     Server-sent events with the same payloads as webhooks, from every location, no retries. Each
    message's `id`
    is the event ID and its `event` is the type; send `Last-Event-ID` to resume after a short break
    (events are
    kept 24 hours for this; after a longer break the stream starts from the oldest event it still has).
    After a
    resume, events from the few seconds before `Last-Event-ID` may come again: drop repeats by event ID.
    You only get event types your
    scopes can read, and a key limited to some apps gets only those apps' events (plus studio-wide ones
    such as a
    region's status), bulk action events only for bulk actions inside its apps, and never billing
    events. A browser's `EventSource` cannot send the `Authorization` header: read the stream with
    `fetch()`
    and a stream reader instead.

    Args:
        types (list[str] | Unset):
        last_event_id (str | Unset): Event ID; also the `webhook-id` of its webhooks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        types=types,
        last_event_id=last_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    types: list[str] | Unset = UNSET,
    last_event_id: str | Unset = UNSET,
) -> Problem | str | None:
    """Follow events live

     Server-sent events with the same payloads as webhooks, from every location, no retries. Each
    message's `id`
    is the event ID and its `event` is the type; send `Last-Event-ID` to resume after a short break
    (events are
    kept 24 hours for this; after a longer break the stream starts from the oldest event it still has).
    After a
    resume, events from the few seconds before `Last-Event-ID` may come again: drop repeats by event ID.
    You only get event types your
    scopes can read, and a key limited to some apps gets only those apps' events (plus studio-wide ones
    such as a
    region's status), bulk action events only for bulk actions inside its apps, and never billing
    events. A browser's `EventSource` cannot send the `Authorization` header: read the stream with
    `fetch()`
    and a stream reader instead.

    Args:
        types (list[str] | Unset):
        last_event_id (str | Unset): Event ID; also the `webhook-id` of its webhooks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return sync_detailed(
        client=client,
        types=types,
        last_event_id=last_event_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    types: list[str] | Unset = UNSET,
    last_event_id: str | Unset = UNSET,
) -> Response[Problem | str]:
    """Follow events live

     Server-sent events with the same payloads as webhooks, from every location, no retries. Each
    message's `id`
    is the event ID and its `event` is the type; send `Last-Event-ID` to resume after a short break
    (events are
    kept 24 hours for this; after a longer break the stream starts from the oldest event it still has).
    After a
    resume, events from the few seconds before `Last-Event-ID` may come again: drop repeats by event ID.
    You only get event types your
    scopes can read, and a key limited to some apps gets only those apps' events (plus studio-wide ones
    such as a
    region's status), bulk action events only for bulk actions inside its apps, and never billing
    events. A browser's `EventSource` cannot send the `Authorization` header: read the stream with
    `fetch()`
    and a stream reader instead.

    Args:
        types (list[str] | Unset):
        last_event_id (str | Unset): Event ID; also the `webhook-id` of its webhooks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        types=types,
        last_event_id=last_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    types: list[str] | Unset = UNSET,
    last_event_id: str | Unset = UNSET,
) -> Problem | str | None:
    """Follow events live

     Server-sent events with the same payloads as webhooks, from every location, no retries. Each
    message's `id`
    is the event ID and its `event` is the type; send `Last-Event-ID` to resume after a short break
    (events are
    kept 24 hours for this; after a longer break the stream starts from the oldest event it still has).
    After a
    resume, events from the few seconds before `Last-Event-ID` may come again: drop repeats by event ID.
    You only get event types your
    scopes can read, and a key limited to some apps gets only those apps' events (plus studio-wide ones
    such as a
    region's status), bulk action events only for bulk actions inside its apps, and never billing
    events. A browser's `EventSource` cannot send the `Authorization` header: read the stream with
    `fetch()`
    and a stream reader instead.

    Args:
        types (list[str] | Unset):
        last_event_id (str | Unset): Event ID; also the `webhook-id` of its webhooks.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return (
        await asyncio_detailed(
            client=client,
            types=types,
            last_event_id=last_event_id,
        )
    ).parsed

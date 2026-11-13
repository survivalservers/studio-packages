from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.status_card import StatusCard
from ...models.status_card_create import StatusCardCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StatusCardCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/status-cards",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | StatusCard:
    if response.status_code == 201:
        response_201 = StatusCard.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | StatusCard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StatusCardCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | StatusCard]:
    """Add a status card

     Posts one message to a Discord channel for your players and keeps it current by editing it: region
    status, maintenance, the version on a branch and the persistent servers you choose. It never shows a
    link, an ID or an address. Use a channel only your team can post in.

    Args:
        idempotency_key (str | Unset):
        body (StatusCardCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatusCard]
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
    body: StatusCardCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | StatusCard | None:
    """Add a status card

     Posts one message to a Discord channel for your players and keeps it current by editing it: region
    status, maintenance, the version on a branch and the persistent servers you choose. It never shows a
    link, an ID or an address. Use a channel only your team can post in.

    Args:
        idempotency_key (str | Unset):
        body (StatusCardCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatusCard
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StatusCardCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | StatusCard]:
    """Add a status card

     Posts one message to a Discord channel for your players and keeps it current by editing it: region
    status, maintenance, the version on a branch and the persistent servers you choose. It never shows a
    link, an ID or an address. Use a channel only your team can post in.

    Args:
        idempotency_key (str | Unset):
        body (StatusCardCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatusCard]
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
    body: StatusCardCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | StatusCard | None:
    """Add a status card

     Posts one message to a Discord channel for your players and keeps it current by editing it: region
    status, maintenance, the version on a branch and the persistent servers you choose. It never shows a
    link, an ID or an address. Use a channel only your team can post in.

    Args:
        idempotency_key (str | Unset):
        body (StatusCardCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatusCard
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

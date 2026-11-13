from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.status_card import StatusCard
from ...models.status_card_update import StatusCardUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: StatusCardUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/status-cards/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | StatusCard:
    if response.status_code == 200:
        response_200 = StatusCard.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
    id: str,
    *,
    client: AuthenticatedClient,
    body: StatusCardUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | StatusCard]:
    """Change a status card

     A new `url` reconnects a card that was turned off, with its settings. The card is edited at once.

    Args:
        id (str): Status card ID.
        idempotency_key (str | Unset):
        body (StatusCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatusCard]
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
    body: StatusCardUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | StatusCard | None:
    """Change a status card

     A new `url` reconnects a card that was turned off, with its settings. The card is edited at once.

    Args:
        id (str): Status card ID.
        idempotency_key (str | Unset):
        body (StatusCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatusCard
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
    body: StatusCardUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | StatusCard]:
    """Change a status card

     A new `url` reconnects a card that was turned off, with its settings. The card is edited at once.

    Args:
        id (str): Status card ID.
        idempotency_key (str | Unset):
        body (StatusCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatusCard]
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
    body: StatusCardUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | StatusCard | None:
    """Change a status card

     A new `url` reconnects a card that was turned off, with its settings. The card is edited at once.

    Args:
        id (str): Status card ID.
        idempotency_key (str | Unset):
        body (StatusCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatusCard
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.billing_portal_session import BillingPortalSession
from ...models.billing_portal_session_create import BillingPortalSessionCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BillingPortalSessionCreate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/billing/portal-session",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingPortalSession | Problem:
    if response.status_code == 201:
        response_201 = BillingPortalSession.from_dict(response.json())

        return response_201

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BillingPortalSession | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingPortalSessionCreate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BillingPortalSession | Problem]:
    """Open the card and billing page

     Returns a short-lived link to the payment provider's page for adding a card and billing details.
    Owners and the billing role only. A suspended studio can still open it, so it can pay whatever the
    reason; a closed one cannot (`403 studio_closed`).

    Args:
        idempotency_key (str | Unset):
        body (BillingPortalSessionCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingPortalSession | Problem]
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
    body: BillingPortalSessionCreate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BillingPortalSession | Problem | None:
    """Open the card and billing page

     Returns a short-lived link to the payment provider's page for adding a card and billing details.
    Owners and the billing role only. A suspended studio can still open it, so it can pay whatever the
    reason; a closed one cannot (`403 studio_closed`).

    Args:
        idempotency_key (str | Unset):
        body (BillingPortalSessionCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingPortalSession | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BillingPortalSessionCreate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[BillingPortalSession | Problem]:
    """Open the card and billing page

     Returns a short-lived link to the payment provider's page for adding a card and billing details.
    Owners and the billing role only. A suspended studio can still open it, so it can pay whatever the
    reason; a closed one cannot (`403 studio_closed`).

    Args:
        idempotency_key (str | Unset):
        body (BillingPortalSessionCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingPortalSession | Problem]
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
    body: BillingPortalSessionCreate | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> BillingPortalSession | Problem | None:
    """Open the card and billing page

     Returns a short-lived link to the payment provider's page for adding a card and billing details.
    Owners and the billing role only. A suspended studio can still open it, so it can pay whatever the
    reason; a closed one cannot (`403 studio_closed`).

    Args:
        idempotency_key (str | Unset):
        body (BillingPortalSessionCreate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingPortalSession | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

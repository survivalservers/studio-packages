from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.budget_alerts import BudgetAlerts
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: BudgetAlerts,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/budget-alerts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BudgetAlerts | Problem:
    if response.status_code == 200:
        response_200 = BudgetAlerts.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BudgetAlerts | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BudgetAlerts,
) -> Response[BudgetAlerts | Problem]:
    """Set budget alerts

     Each threshold alerts once a month when the projected month total passes it. Alerts never stop
    anything. An address that is not a member's sign-in email gets no alert until it confirms: saving
    the list sends it one email with a link to confirm (at most one a day, counted in the studio's daily
    limit of invitation emails), and it is listed in `unconfirmed` until then. Each alert to a confirmed
    address carries a link its owner can stop them with. Taking an address off the list ends its
    confirmation. A key limited to some apps gets `403 key_restricted`.

    Args:
        body (BudgetAlerts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetAlerts | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BudgetAlerts,
) -> BudgetAlerts | Problem | None:
    """Set budget alerts

     Each threshold alerts once a month when the projected month total passes it. Alerts never stop
    anything. An address that is not a member's sign-in email gets no alert until it confirms: saving
    the list sends it one email with a link to confirm (at most one a day, counted in the studio's daily
    limit of invitation emails), and it is listed in `unconfirmed` until then. Each alert to a confirmed
    address carries a link its owner can stop them with. Taking an address off the list ends its
    confirmation. A key limited to some apps gets `403 key_restricted`.

    Args:
        body (BudgetAlerts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetAlerts | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BudgetAlerts,
) -> Response[BudgetAlerts | Problem]:
    """Set budget alerts

     Each threshold alerts once a month when the projected month total passes it. Alerts never stop
    anything. An address that is not a member's sign-in email gets no alert until it confirms: saving
    the list sends it one email with a link to confirm (at most one a day, counted in the studio's daily
    limit of invitation emails), and it is listed in `unconfirmed` until then. Each alert to a confirmed
    address carries a link its owner can stop them with. Taking an address off the list ends its
    confirmation. A key limited to some apps gets `403 key_restricted`.

    Args:
        body (BudgetAlerts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetAlerts | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BudgetAlerts,
) -> BudgetAlerts | Problem | None:
    """Set budget alerts

     Each threshold alerts once a month when the projected month total passes it. Alerts never stop
    anything. An address that is not a member's sign-in email gets no alert until it confirms: saving
    the list sends it one email with a link to confirm (at most one a day, counted in the studio's daily
    limit of invitation emails), and it is listed in `unconfirmed` until then. Each alert to a confirmed
    address carries a link its owner can stop them with. Taking an address off the list ends its
    confirmation. A key limited to some apps gets `403 key_restricted`.

    Args:
        body (BudgetAlerts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetAlerts | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

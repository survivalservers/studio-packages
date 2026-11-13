from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.webhook_endpoint import WebhookEndpoint
from ...models.webhook_endpoint_update import WebhookEndpointUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: WebhookEndpointUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/webhook-endpoints/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookEndpoint:
    if response.status_code == 200:
        response_200 = WebhookEndpoint.from_dict(response.json())

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
) -> Response[Problem | WebhookEndpoint]:
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
    body: WebhookEndpointUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | WebhookEndpoint]:
    """Change a webhook endpoint

     Change `url`, `events`, `default` or `enabled`. Turning a disabled endpoint back on clears its
    failure streak.

    Args:
        id (str): Webhook endpoint ID.
        idempotency_key (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
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
    body: WebhookEndpointUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | WebhookEndpoint | None:
    """Change a webhook endpoint

     Change `url`, `events`, `default` or `enabled`. Turning a disabled endpoint back on clears its
    failure streak.

    Args:
        id (str): Webhook endpoint ID.
        idempotency_key (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
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
    body: WebhookEndpointUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | WebhookEndpoint]:
    """Change a webhook endpoint

     Change `url`, `events`, `default` or `enabled`. Turning a disabled endpoint back on clears its
    failure streak.

    Args:
        id (str): Webhook endpoint ID.
        idempotency_key (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookEndpoint]
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
    body: WebhookEndpointUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | WebhookEndpoint | None:
    """Change a webhook endpoint

     Change `url`, `events`, `default` or `enabled`. Turning a disabled endpoint back on clears its
    failure streak.

    Args:
        id (str): Webhook endpoint ID.
        idempotency_key (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookEndpoint
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.alert_address_link import AlertAddressLink
from ...models.alert_address_studio import AlertAddressStudio
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AlertAddressLink,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/alert-address-confirmations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertAddressStudio | Problem:
    if response.status_code == 200:
        response_200 = AlertAddressStudio.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertAddressStudio | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAddressLink,
    idempotency_key: str | Unset = UNSET,
) -> Response[AlertAddressStudio | Problem]:
    """Confirm a budget alert address

     The button on the page a budget alert confirm email links to: with the link's token, the studio's
    budget alerts go to that address from now on, and nothing else does. Opening the page sends nothing,
    so a mail scanner that opens links confirms nothing. Needs no key and no sign-in. A link works once,
    for 7 days: an unknown, used or expired token gets the same `404`, and every answer takes the same
    time. Limited per sender address like sign-up (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (AlertAddressLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertAddressStudio | Problem]
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
    client: AuthenticatedClient | Client,
    body: AlertAddressLink,
    idempotency_key: str | Unset = UNSET,
) -> AlertAddressStudio | Problem | None:
    """Confirm a budget alert address

     The button on the page a budget alert confirm email links to: with the link's token, the studio's
    budget alerts go to that address from now on, and nothing else does. Opening the page sends nothing,
    so a mail scanner that opens links confirms nothing. Needs no key and no sign-in. A link works once,
    for 7 days: an unknown, used or expired token gets the same `404`, and every answer takes the same
    time. Limited per sender address like sign-up (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (AlertAddressLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertAddressStudio | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAddressLink,
    idempotency_key: str | Unset = UNSET,
) -> Response[AlertAddressStudio | Problem]:
    """Confirm a budget alert address

     The button on the page a budget alert confirm email links to: with the link's token, the studio's
    budget alerts go to that address from now on, and nothing else does. Opening the page sends nothing,
    so a mail scanner that opens links confirms nothing. Needs no key and no sign-in. A link works once,
    for 7 days: an unknown, used or expired token gets the same `404`, and every answer takes the same
    time. Limited per sender address like sign-up (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (AlertAddressLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertAddressStudio | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AlertAddressLink,
    idempotency_key: str | Unset = UNSET,
) -> AlertAddressStudio | Problem | None:
    """Confirm a budget alert address

     The button on the page a budget alert confirm email links to: with the link's token, the studio's
    budget alerts go to that address from now on, and nothing else does. Opening the page sends nothing,
    so a mail scanner that opens links confirms nothing. Needs no key and no sign-in. A link works once,
    for 7 days: an unknown, used or expired token gets the same `404`, and every answer takes the same
    time. Limited per sender address like sign-up (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (AlertAddressLink):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertAddressStudio | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

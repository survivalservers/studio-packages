from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.contact_request_create import ContactRequestCreate
from ...models.contact_request_received import ContactRequestReceived
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ContactRequestCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/contact",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactRequestReceived | Problem:
    if response.status_code == 202:
        response_202 = ContactRequestReceived.from_dict(response.json())

        return response_202

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
) -> Response[ContactRequestReceived | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ContactRequestCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ContactRequestReceived | Problem]:
    """Ask to talk to us

     The product pages' contact form: a studio leaves its details and the people who run the platform get
    back to it. Needs no key and no sign-in, and answers any web page (`Access-Control-Allow-Origin: *`;
    no cookies are read). What is sent is kept as plain text only: nothing in it is fetched, run, or
    emailed anywhere. Each sender address may send 5 an hour and 20 a day (`429 rate_limited`), and the
    same form sent again from the same address within 24 hours is kept once. Every accepted form answers
    `202` with the same body.

    Args:
        idempotency_key (str | Unset):
        body (ContactRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactRequestReceived | Problem]
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
    body: ContactRequestCreate,
    idempotency_key: str | Unset = UNSET,
) -> ContactRequestReceived | Problem | None:
    """Ask to talk to us

     The product pages' contact form: a studio leaves its details and the people who run the platform get
    back to it. Needs no key and no sign-in, and answers any web page (`Access-Control-Allow-Origin: *`;
    no cookies are read). What is sent is kept as plain text only: nothing in it is fetched, run, or
    emailed anywhere. Each sender address may send 5 an hour and 20 a day (`429 rate_limited`), and the
    same form sent again from the same address within 24 hours is kept once. Every accepted form answers
    `202` with the same body.

    Args:
        idempotency_key (str | Unset):
        body (ContactRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactRequestReceived | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ContactRequestCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ContactRequestReceived | Problem]:
    """Ask to talk to us

     The product pages' contact form: a studio leaves its details and the people who run the platform get
    back to it. Needs no key and no sign-in, and answers any web page (`Access-Control-Allow-Origin: *`;
    no cookies are read). What is sent is kept as plain text only: nothing in it is fetched, run, or
    emailed anywhere. Each sender address may send 5 an hour and 20 a day (`429 rate_limited`), and the
    same form sent again from the same address within 24 hours is kept once. Every accepted form answers
    `202` with the same body.

    Args:
        idempotency_key (str | Unset):
        body (ContactRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactRequestReceived | Problem]
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
    body: ContactRequestCreate,
    idempotency_key: str | Unset = UNSET,
) -> ContactRequestReceived | Problem | None:
    """Ask to talk to us

     The product pages' contact form: a studio leaves its details and the people who run the platform get
    back to it. Needs no key and no sign-in, and answers any web page (`Access-Control-Allow-Origin: *`;
    no cookies are read). What is sent is kept as plain text only: nothing in it is fetched, run, or
    emailed anywhere. Each sender address may send 5 an hour and 20 a day (`429 rate_limited`), and the
    same form sent again from the same address within 24 hours is kept once. Every accepted form answers
    `202` with the same body.

    Args:
        idempotency_key (str | Unset):
        body (ContactRequestCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactRequestReceived | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

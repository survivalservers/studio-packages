from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.sign_up_create import SignUpCreate
from ...models.sign_up_received import SignUpReceived
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/sign-up",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SignUpReceived:
    if response.status_code == 202:
        response_202 = SignUpReceived.from_dict(response.json())

        return response_202

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

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
) -> Response[Problem | SignUpReceived]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Sign up by email

     The panel's sign-up form: only an email. Needs no key and no sign-in. Every accepted request answers
    `202` with the same body whatever the email, and what happens next is said only in an email to that
    address: a link to confirm it and choose a password and a one-time code (no account yet), "you
    already have an account" (one in use), or "sign in through your company" (a domain whose studio
    signs its people in through its own provider). So the form never says whether an email has an
    account. Each sender address may ask 10 times an hour and 50 a day (`429 rate_limited`, the same for
    every email); one email gets at most one email every 15 minutes, and more requests for it are
    answered the same and dropped. `return_to` is where the link's last page leads on the panel (a path,
    `/` when left out), for example an invitation the person was about to accept. While open sign-up is
    closed (before launch), every request is `403 signups_closed`, whatever the email; a person invited
    to a studio signs up with the invitation's link instead (`POST /v0/invitation-sign-up`).

    Args:
        idempotency_key (str | Unset):
        body (SignUpCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SignUpReceived]
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
    body: SignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Sign up by email

     The panel's sign-up form: only an email. Needs no key and no sign-in. Every accepted request answers
    `202` with the same body whatever the email, and what happens next is said only in an email to that
    address: a link to confirm it and choose a password and a one-time code (no account yet), "you
    already have an account" (one in use), or "sign in through your company" (a domain whose studio
    signs its people in through its own provider). So the form never says whether an email has an
    account. Each sender address may ask 10 times an hour and 50 a day (`429 rate_limited`, the same for
    every email); one email gets at most one email every 15 minutes, and more requests for it are
    answered the same and dropped. `return_to` is where the link's last page leads on the panel (a path,
    `/` when left out), for example an invitation the person was about to accept. While open sign-up is
    closed (before launch), every request is `403 signups_closed`, whatever the email; a person invited
    to a studio signs up with the invitation's link instead (`POST /v0/invitation-sign-up`).

    Args:
        idempotency_key (str | Unset):
        body (SignUpCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SignUpReceived
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Sign up by email

     The panel's sign-up form: only an email. Needs no key and no sign-in. Every accepted request answers
    `202` with the same body whatever the email, and what happens next is said only in an email to that
    address: a link to confirm it and choose a password and a one-time code (no account yet), "you
    already have an account" (one in use), or "sign in through your company" (a domain whose studio
    signs its people in through its own provider). So the form never says whether an email has an
    account. Each sender address may ask 10 times an hour and 50 a day (`429 rate_limited`, the same for
    every email); one email gets at most one email every 15 minutes, and more requests for it are
    answered the same and dropped. `return_to` is where the link's last page leads on the panel (a path,
    `/` when left out), for example an invitation the person was about to accept. While open sign-up is
    closed (before launch), every request is `403 signups_closed`, whatever the email; a person invited
    to a studio signs up with the invitation's link instead (`POST /v0/invitation-sign-up`).

    Args:
        idempotency_key (str | Unset):
        body (SignUpCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SignUpReceived]
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
    body: SignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Sign up by email

     The panel's sign-up form: only an email. Needs no key and no sign-in. Every accepted request answers
    `202` with the same body whatever the email, and what happens next is said only in an email to that
    address: a link to confirm it and choose a password and a one-time code (no account yet), "you
    already have an account" (one in use), or "sign in through your company" (a domain whose studio
    signs its people in through its own provider). So the form never says whether an email has an
    account. Each sender address may ask 10 times an hour and 50 a day (`429 rate_limited`, the same for
    every email); one email gets at most one email every 15 minutes, and more requests for it are
    answered the same and dropped. `return_to` is where the link's last page leads on the panel (a path,
    `/` when left out), for example an invitation the person was about to accept. While open sign-up is
    closed (before launch), every request is `403 signups_closed`, whatever the email; a person invited
    to a studio signs up with the invitation's link instead (`POST /v0/invitation-sign-up`).

    Args:
        idempotency_key (str | Unset):
        body (SignUpCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SignUpReceived
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

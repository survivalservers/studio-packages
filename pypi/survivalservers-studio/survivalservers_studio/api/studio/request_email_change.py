from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.email_change_create import EmailChangeCreate
from ...models.problem import Problem
from ...models.sign_up_received import SignUpReceived
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EmailChangeCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/me/email",
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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

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
    client: AuthenticatedClient,
    body: EmailChangeCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Change your sign-in email

     Asks to sign in with another email from now on. Answers `202` the same whatever the address, and
    what happens next is said only in an email to that address: a link to confirm it (it works once, for
    an hour, while you are signed in as yourself), "this address already has an account", or "your
    company manages sign-in for this address". Needs a sign-in with two-factor authentication in the
    last 10 minutes (`403 sign_in_again` otherwise: sign in again). People who sign in through their
    company change it there (`409 invalid_state`). 5 requests an hour (`429 rate_limited`); a new
    request ends the last one's link.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeCreate):

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
    client: AuthenticatedClient,
    body: EmailChangeCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Change your sign-in email

     Asks to sign in with another email from now on. Answers `202` the same whatever the address, and
    what happens next is said only in an email to that address: a link to confirm it (it works once, for
    an hour, while you are signed in as yourself), "this address already has an account", or "your
    company manages sign-in for this address". Needs a sign-in with two-factor authentication in the
    last 10 minutes (`403 sign_in_again` otherwise: sign in again). People who sign in through their
    company change it there (`409 invalid_state`). 5 requests an hour (`429 rate_limited`); a new
    request ends the last one's link.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeCreate):

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
    client: AuthenticatedClient,
    body: EmailChangeCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Change your sign-in email

     Asks to sign in with another email from now on. Answers `202` the same whatever the address, and
    what happens next is said only in an email to that address: a link to confirm it (it works once, for
    an hour, while you are signed in as yourself), "this address already has an account", or "your
    company manages sign-in for this address". Needs a sign-in with two-factor authentication in the
    last 10 minutes (`403 sign_in_again` otherwise: sign in again). People who sign in through their
    company change it there (`409 invalid_state`). 5 requests an hour (`429 rate_limited`); a new
    request ends the last one's link.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeCreate):

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
    client: AuthenticatedClient,
    body: EmailChangeCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Change your sign-in email

     Asks to sign in with another email from now on. Answers `202` the same whatever the address, and
    what happens next is said only in an email to that address: a link to confirm it (it works once, for
    an hour, while you are signed in as yourself), "this address already has an account", or "your
    company manages sign-in for this address". Needs a sign-in with two-factor authentication in the
    last 10 minutes (`403 sign_in_again` otherwise: sign in again). People who sign in through their
    company change it there (`409 invalid_state`). 5 requests an hour (`429 rate_limited`); a new
    request ends the last one's link.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeCreate):

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

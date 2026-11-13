from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.invitation_sign_up_create import InvitationSignUpCreate
from ...models.problem import Problem
from ...models.sign_up_received import SignUpReceived
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InvitationSignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/invitation-sign-up",
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
    body: InvitationSignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Create an account from an invitation

     For the person an invitation was sent to, when they have no account yet: the token from the
    invitation link is all it takes. Needs no key and no sign-in, and works while open sign-up is
    closed. The account is made for the invitation's own email address, never another, by the same email
    link as `POST /v0/sign-up` (confirm the email, choose a password and a one-time code), and the link
    leads back to the invitation. An address that already has an account is emailed "sign in here"
    instead. `404` when the invitation was used, canceled or is past its 7 days. Limited like sign-up
    (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (InvitationSignUpCreate):

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
    body: InvitationSignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Create an account from an invitation

     For the person an invitation was sent to, when they have no account yet: the token from the
    invitation link is all it takes. Needs no key and no sign-in, and works while open sign-up is
    closed. The account is made for the invitation's own email address, never another, by the same email
    link as `POST /v0/sign-up` (confirm the email, choose a password and a one-time code), and the link
    leads back to the invitation. An address that already has an account is emailed "sign in here"
    instead. `404` when the invitation was used, canceled or is past its 7 days. Limited like sign-up
    (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (InvitationSignUpCreate):

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
    body: InvitationSignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SignUpReceived]:
    """Create an account from an invitation

     For the person an invitation was sent to, when they have no account yet: the token from the
    invitation link is all it takes. Needs no key and no sign-in, and works while open sign-up is
    closed. The account is made for the invitation's own email address, never another, by the same email
    link as `POST /v0/sign-up` (confirm the email, choose a password and a one-time code), and the link
    leads back to the invitation. An address that already has an account is emailed "sign in here"
    instead. `404` when the invitation was used, canceled or is past its 7 days. Limited like sign-up
    (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (InvitationSignUpCreate):

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
    body: InvitationSignUpCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SignUpReceived | None:
    """Create an account from an invitation

     For the person an invitation was sent to, when they have no account yet: the token from the
    invitation link is all it takes. Needs no key and no sign-in, and works while open sign-up is
    closed. The account is made for the invitation's own email address, never another, by the same email
    link as `POST /v0/sign-up` (confirm the email, choose a password and a one-time code), and the link
    leads back to the invitation. An address that already has an account is emailed "sign in here"
    instead. `404` when the invitation was used, canceled or is past its 7 days. Limited like sign-up
    (`429 rate_limited`).

    Args:
        idempotency_key (str | Unset):
        body (InvitationSignUpCreate):

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

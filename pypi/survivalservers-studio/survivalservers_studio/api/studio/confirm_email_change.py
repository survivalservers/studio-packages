from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.email_change_confirm import EmailChangeConfirm
from ...models.email_changed import EmailChanged
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EmailChangeConfirm,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/me/email/confirm",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailChanged | Problem:
    if response.status_code == 200:
        response_200 = EmailChanged.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmailChanged | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailChangeConfirm,
    idempotency_key: str | Unset = UNSET,
) -> Response[EmailChanged | Problem]:
    """Confirm your new sign-in email

     The link's token, sent by the person who asked for the change. The address becomes their sign-in
    email, their pending invitations to the old address move to it, their studios' audit logs record it,
    the old address is told, and they are signed out everywhere to sign in again with the new one. A
    token that ran out, was used or was replaced by a newer request is `404 not_found`; one for another
    person is `403 key_restricted`; an address taken in the meantime is `409 invalid_state`.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChanged | Problem]
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
    body: EmailChangeConfirm,
    idempotency_key: str | Unset = UNSET,
) -> EmailChanged | Problem | None:
    """Confirm your new sign-in email

     The link's token, sent by the person who asked for the change. The address becomes their sign-in
    email, their pending invitations to the old address move to it, their studios' audit logs record it,
    the old address is told, and they are signed out everywhere to sign in again with the new one. A
    token that ran out, was used or was replaced by a newer request is `404 not_found`; one for another
    person is `403 key_restricted`; an address taken in the meantime is `409 invalid_state`.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChanged | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmailChangeConfirm,
    idempotency_key: str | Unset = UNSET,
) -> Response[EmailChanged | Problem]:
    """Confirm your new sign-in email

     The link's token, sent by the person who asked for the change. The address becomes their sign-in
    email, their pending invitations to the old address move to it, their studios' audit logs record it,
    the old address is told, and they are signed out everywhere to sign in again with the new one. A
    token that ran out, was used or was replaced by a newer request is `404 not_found`; one for another
    person is `403 key_restricted`; an address taken in the meantime is `409 invalid_state`.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailChanged | Problem]
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
    body: EmailChangeConfirm,
    idempotency_key: str | Unset = UNSET,
) -> EmailChanged | Problem | None:
    """Confirm your new sign-in email

     The link's token, sent by the person who asked for the change. The address becomes their sign-in
    email, their pending invitations to the old address move to it, their studios' audit logs record it,
    the old address is told, and they are signed out everywhere to sign in again with the new one. A
    token that ran out, was used or was replaced by a newer request is `404 not_found`; one for another
    person is `403 key_restricted`; an address taken in the meantime is `409 invalid_state`.

    Args:
        idempotency_key (str | Unset):
        body (EmailChangeConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailChanged | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

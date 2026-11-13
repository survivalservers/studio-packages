from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.me import Me
from ...models.problem import Problem
from ...models.terms_accept import TermsAccept
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TermsAccept,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/me/terms",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Me | Problem:
    if response.status_code == 200:
        response_200 = Me.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Me | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TermsAccept,
    idempotency_key: str | Unset = UNSET,
) -> Response[Me | Problem]:
    """Agree to the terms in effect

     Records that the signed-in person agreed to the version of the terms in effect, for themselves and
    for each studio they belong to, with the time and a keyed hash of the address the call came from
    (never the address). The panel calls it from the box it shows when `me.terms.accepted` is false: a
    new version took effect, or the person signed in without the sign-up form. A version other than the
    one in effect is `422` on `version`; none in effect is `409 invalid_state`. Repeating it changes
    nothing.

    Args:
        idempotency_key (str | Unset):
        body (TermsAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Me | Problem]
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
    body: TermsAccept,
    idempotency_key: str | Unset = UNSET,
) -> Me | Problem | None:
    """Agree to the terms in effect

     Records that the signed-in person agreed to the version of the terms in effect, for themselves and
    for each studio they belong to, with the time and a keyed hash of the address the call came from
    (never the address). The panel calls it from the box it shows when `me.terms.accepted` is false: a
    new version took effect, or the person signed in without the sign-up form. A version other than the
    one in effect is `422` on `version`; none in effect is `409 invalid_state`. Repeating it changes
    nothing.

    Args:
        idempotency_key (str | Unset):
        body (TermsAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Me | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TermsAccept,
    idempotency_key: str | Unset = UNSET,
) -> Response[Me | Problem]:
    """Agree to the terms in effect

     Records that the signed-in person agreed to the version of the terms in effect, for themselves and
    for each studio they belong to, with the time and a keyed hash of the address the call came from
    (never the address). The panel calls it from the box it shows when `me.terms.accepted` is false: a
    new version took effect, or the person signed in without the sign-up form. A version other than the
    one in effect is `422` on `version`; none in effect is `409 invalid_state`. Repeating it changes
    nothing.

    Args:
        idempotency_key (str | Unset):
        body (TermsAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Me | Problem]
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
    body: TermsAccept,
    idempotency_key: str | Unset = UNSET,
) -> Me | Problem | None:
    """Agree to the terms in effect

     Records that the signed-in person agreed to the version of the terms in effect, for themselves and
    for each studio they belong to, with the time and a keyed hash of the address the call came from
    (never the address). The panel calls it from the box it shows when `me.terms.accepted` is false: a
    new version took effect, or the person signed in without the sign-up form. A version other than the
    one in effect is `422` on `version`; none in effect is `409 invalid_state`. Repeating it changes
    nothing.

    Args:
        idempotency_key (str | Unset):
        body (TermsAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Me | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

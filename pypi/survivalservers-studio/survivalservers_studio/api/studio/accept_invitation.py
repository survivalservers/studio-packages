from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.invitation_accept import InvitationAccept
from ...models.membership import Membership
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    token: str,
    *,
    body: InvitationAccept | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/invitations/{token}/accept".format(
            token=quote(str(token), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Membership | Problem:
    if response.status_code == 200:
        response_200 = Membership.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[Membership | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: AuthenticatedClient,
    body: InvitationAccept | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Membership | Problem]:
    """Accept an invitation

     Adds the signed-in person to the studio with the invited role. While a version of the terms is in
    effect that the person has not agreed to yet, `terms_version` must name it (`422` otherwise).

    Args:
        token (str):
        idempotency_key (str | Unset):
        body (InvitationAccept | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Membership | Problem]
    """

    kwargs = _get_kwargs(
        token=token,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token: str,
    *,
    client: AuthenticatedClient,
    body: InvitationAccept | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Membership | Problem | None:
    """Accept an invitation

     Adds the signed-in person to the studio with the invited role. While a version of the terms is in
    effect that the person has not agreed to yet, `terms_version` must name it (`422` otherwise).

    Args:
        token (str):
        idempotency_key (str | Unset):
        body (InvitationAccept | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Membership | Problem
    """

    return sync_detailed(
        token=token,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient,
    body: InvitationAccept | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Membership | Problem]:
    """Accept an invitation

     Adds the signed-in person to the studio with the invited role. While a version of the terms is in
    effect that the person has not agreed to yet, `terms_version` must name it (`422` otherwise).

    Args:
        token (str):
        idempotency_key (str | Unset):
        body (InvitationAccept | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Membership | Problem]
    """

    kwargs = _get_kwargs(
        token=token,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient,
    body: InvitationAccept | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Membership | Problem | None:
    """Accept an invitation

     Adds the signed-in person to the studio with the invited role. While a version of the terms is in
    effect that the person has not agreed to yet, `terms_version` must name it (`422` otherwise).

    Args:
        token (str):
        idempotency_key (str | Unset):
        body (InvitationAccept | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Membership | Problem
    """

    return (
        await asyncio_detailed(
            token=token,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

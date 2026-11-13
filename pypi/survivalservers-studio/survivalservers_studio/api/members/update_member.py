from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.member import Member
from ...models.member_update import MemberUpdate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user: str,
    *,
    body: MemberUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/members/{user}".format(
            user=quote(str(user), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Member | Problem:
    if response.status_code == 200:
        response_200 = Member.from_dict(response.json())

        return response_200

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
) -> Response[Member | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user: str,
    *,
    client: AuthenticatedClient,
    body: MemberUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Member | Problem]:
    """Change a member's role

     A studio always keeps at least one owner.

    Args:
        user (str): Person ID.
        idempotency_key (str | Unset):
        body (MemberUpdate): Send `role`, `crash_dumps` or both (`422` with neither).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member | Problem]
    """

    kwargs = _get_kwargs(
        user=user,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: str,
    *,
    client: AuthenticatedClient,
    body: MemberUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Member | Problem | None:
    """Change a member's role

     A studio always keeps at least one owner.

    Args:
        user (str): Person ID.
        idempotency_key (str | Unset):
        body (MemberUpdate): Send `role`, `crash_dumps` or both (`422` with neither).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member | Problem
    """

    return sync_detailed(
        user=user,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    user: str,
    *,
    client: AuthenticatedClient,
    body: MemberUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Member | Problem]:
    """Change a member's role

     A studio always keeps at least one owner.

    Args:
        user (str): Person ID.
        idempotency_key (str | Unset):
        body (MemberUpdate): Send `role`, `crash_dumps` or both (`422` with neither).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Member | Problem]
    """

    kwargs = _get_kwargs(
        user=user,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: str,
    *,
    client: AuthenticatedClient,
    body: MemberUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Member | Problem | None:
    """Change a member's role

     A studio always keeps at least one owner.

    Args:
        user (str): Person ID.
        idempotency_key (str | Unset):
        body (MemberUpdate): Send `role`, `crash_dumps` or both (`422` with neither).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Member | Problem
    """

    return (
        await asyncio_detailed(
            user=user,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.invitation_list import InvitationList
from ...models.list_invitations_status import ListInvitationsStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/members/invitations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InvitationList | Problem:
    if response.status_code == 200:
        response_200 = InvitationList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InvitationList | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = UNSET,
) -> Response[InvitationList | Problem]:
    """List invitations

     The studio's invitations, newest first, with who sent each; `status=pending` for the ones still
    waiting (a pending one past its time shows as `expired`).

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListInvitationsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = UNSET,
) -> InvitationList | Problem | None:
    """List invitations

     The studio's invitations, newest first, with who sent each; `status=pending` for the ones still
    waiting (a pending one past its time shows as `expired`).

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListInvitationsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = UNSET,
) -> Response[InvitationList | Problem]:
    """List invitations

     The studio's invitations, newest first, with who sent each; `status=pending` for the ones still
    waiting (a pending one past its time shows as `expired`).

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListInvitationsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvitationList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: ListInvitationsStatus | Unset = UNSET,
) -> InvitationList | Problem | None:
    """List invitations

     The studio's invitations, newest first, with who sent each; `status=pending` for the ones still
    waiting (a pending one past its time shows as `expired`).

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (ListInvitationsStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvitationList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
        )
    ).parsed

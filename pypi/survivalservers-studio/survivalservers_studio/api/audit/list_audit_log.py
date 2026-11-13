import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_list import AuditList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    target: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    by_ai: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["actor"] = actor

    params["action"] = action

    params["target"] = target

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["by_ai"] = by_ai

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/audit-log",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditList | Problem:
    if response.status_code == 200:
        response_200 = AuditList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditList | Problem]:
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
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    target: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    by_ai: bool | Unset = UNSET,
) -> Response[AuditList | Problem]:
    """List the audit log

     Every write by any key or member of this studio, newest first, kept one year, with one exception: a
    key's own match starts and stops (a matchmaker makes thousands an hour). Those are on each game
    server instead: its start and stop steps in the timeline name the key and the caller's address and
    are kept a year, and `GET /v0/game-servers?by=key_...` finds every game server a key started or
    stopped. Every start, stop and restart made by a member in the panel or by an AI agent is here, as
    is every persistent server start, stop and restart whoever made it, every stop of many game servers
    at once (`game_servers.stop`, with the count), and a key's stop of a match that someone else
    started. `actor` is a key ID or a member's user ID.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        actor (str | Unset):
        action (str | Unset):
        target (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        by_ai (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        actor=actor,
        action=action,
        target=target,
        from_=from_,
        to=to,
        by_ai=by_ai,
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
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    target: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    by_ai: bool | Unset = UNSET,
) -> AuditList | Problem | None:
    """List the audit log

     Every write by any key or member of this studio, newest first, kept one year, with one exception: a
    key's own match starts and stops (a matchmaker makes thousands an hour). Those are on each game
    server instead: its start and stop steps in the timeline name the key and the caller's address and
    are kept a year, and `GET /v0/game-servers?by=key_...` finds every game server a key started or
    stopped. Every start, stop and restart made by a member in the panel or by an AI agent is here, as
    is every persistent server start, stop and restart whoever made it, every stop of many game servers
    at once (`game_servers.stop`, with the count), and a key's stop of a match that someone else
    started. `actor` is a key ID or a member's user ID.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        actor (str | Unset):
        action (str | Unset):
        target (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        by_ai (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        actor=actor,
        action=action,
        target=target,
        from_=from_,
        to=to,
        by_ai=by_ai,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    target: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    by_ai: bool | Unset = UNSET,
) -> Response[AuditList | Problem]:
    """List the audit log

     Every write by any key or member of this studio, newest first, kept one year, with one exception: a
    key's own match starts and stops (a matchmaker makes thousands an hour). Those are on each game
    server instead: its start and stop steps in the timeline name the key and the caller's address and
    are kept a year, and `GET /v0/game-servers?by=key_...` finds every game server a key started or
    stopped. Every start, stop and restart made by a member in the panel or by an AI agent is here, as
    is every persistent server start, stop and restart whoever made it, every stop of many game servers
    at once (`game_servers.stop`, with the count), and a key's stop of a match that someone else
    started. `actor` is a key ID or a member's user ID.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        actor (str | Unset):
        action (str | Unset):
        target (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        by_ai (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        actor=actor,
        action=action,
        target=target,
        from_=from_,
        to=to,
        by_ai=by_ai,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    action: str | Unset = UNSET,
    target: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    by_ai: bool | Unset = UNSET,
) -> AuditList | Problem | None:
    """List the audit log

     Every write by any key or member of this studio, newest first, kept one year, with one exception: a
    key's own match starts and stops (a matchmaker makes thousands an hour). Those are on each game
    server instead: its start and stop steps in the timeline name the key and the caller's address and
    are kept a year, and `GET /v0/game-servers?by=key_...` finds every game server a key started or
    stopped. Every start, stop and restart made by a member in the panel or by an AI agent is here, as
    is every persistent server start, stop and restart whoever made it, every stop of many game servers
    at once (`game_servers.stop`, with the count), and a key's stop of a match that someone else
    started. `actor` is a key ID or a member's user ID.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        actor (str | Unset):
        action (str | Unset):
        target (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        by_ai (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            actor=actor,
            action=action,
            target=target,
            from_=from_,
            to=to,
            by_ai=by_ai,
        )
    ).parsed

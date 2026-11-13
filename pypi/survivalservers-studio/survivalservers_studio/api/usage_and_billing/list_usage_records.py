import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.usage_record_list import UsageRecordList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["game_server"] = game_server

    params["persistent_server"] = persistent_server

    params["app"] = app

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/usage/records",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UsageRecordList:
    if response.status_code == 200:
        response_200 = UsageRecordList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UsageRecordList]:
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
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Problem | UsageRecordList]:
    """List usage records

     The per-second records behind the totals. A key limited to some apps gets only those apps' records.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UsageRecordList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        game_server=game_server,
        persistent_server=persistent_server,
        app=app,
        from_=from_,
        to=to,
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
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Problem | UsageRecordList | None:
    """List usage records

     The per-second records behind the totals. A key limited to some apps gets only those apps' records.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UsageRecordList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        game_server=game_server,
        persistent_server=persistent_server,
        app=app,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Problem | UsageRecordList]:
    """List usage records

     The per-second records behind the totals. A key limited to some apps gets only those apps' records.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UsageRecordList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        game_server=game_server,
        persistent_server=persistent_server,
        app=app,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Problem | UsageRecordList | None:
    """List usage records

     The per-second records behind the totals. A key limited to some apps gets only those apps' records.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UsageRecordList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            game_server=game_server,
            persistent_server=persistent_server,
            app=app,
            from_=from_,
            to=to,
        )
    ).parsed

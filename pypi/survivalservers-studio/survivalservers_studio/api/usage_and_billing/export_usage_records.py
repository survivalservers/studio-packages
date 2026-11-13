import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/v0/usage/records.csv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | str:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Problem | str]:
    """Export usage records as CSV

     Same filters as the list, one row per record, sent as it is read. One export covers at most 13
    months: `from` defaults to 13 months before `to`, and `to` to now; a longer span is refused (422
    naming the field), so export it in parts. Two exports per studio run at once; a third is refused
    with 429 until one ends.

    Args:
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
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
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Problem | str | None:
    """Export usage records as CSV

     Same filters as the list, one row per record, sent as it is read. One export covers at most 13
    months: `from` defaults to 13 months before `to`, and `to` to now; a longer span is refused (422
    naming the field), so export it in parts. Two exports per studio run at once; a third is refused
    with 429 until one ends.

    Args:
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return sync_detailed(
        client=client,
        game_server=game_server,
        persistent_server=persistent_server,
        app=app,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[Problem | str]:
    """Export usage records as CSV

     Same filters as the list, one row per record, sent as it is read. One export covers at most 13
    months: `from` defaults to 13 months before `to`, and `to` to now; a longer span is refused (422
    naming the field), so export it in parts. Two exports per studio run at once; a third is refused
    with 429 until one ends.

    Args:
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
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
    game_server: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    app: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Problem | str | None:
    """Export usage records as CSV

     Same filters as the list, one row per record, sent as it is read. One export covers at most 13
    months: `from` defaults to 13 months before `to`, and `to` to now; a longer span is refused (422
    naming the field), so export it in parts. Two exports per studio run at once; a third is refused
    with 429 until one ends.

    Args:
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
        app (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return (
        await asyncio_detailed(
            client=client,
            game_server=game_server,
            persistent_server=persistent_server,
            app=app,
            from_=from_,
            to=to,
        )
    ).parsed

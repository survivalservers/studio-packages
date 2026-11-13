import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_start_stats_group_by_item import GetStartStatsGroupByItem
from ...models.problem import Problem
from ...models.start_stats import StartStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    group_by: list[GetStartStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_group_by: list[str] | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = []
        for group_by_item_data in group_by:
            group_by_item = group_by_item_data.value
            json_group_by.append(group_by_item)

    params["group_by"] = json_group_by

    params["app"] = app

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/stats/starts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | StartStats:
    if response.status_code == 200:
        response_200 = StartStats.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | StartStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    group_by: list[GetStartStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
) -> Response[Problem | StartStats]:
    """Get start times

     How many game servers you started and how fast our replies were (p50 and p95 of the successful
    starts, measured at our API edge), for one period of at most 92 days. Group by region, app or start
    mode. Starts refused for your own reasons (validation, limits) are not counted; `failed` counts our
    failures.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        group_by (list[GetStartStatsGroupByItem] | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StartStats]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        group_by=group_by,
        app=app,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    group_by: list[GetStartStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
) -> Problem | StartStats | None:
    """Get start times

     How many game servers you started and how fast our replies were (p50 and p95 of the successful
    starts, measured at our API edge), for one period of at most 92 days. Group by region, app or start
    mode. Starts refused for your own reasons (validation, limits) are not counted; `failed` counts our
    failures.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        group_by (list[GetStartStatsGroupByItem] | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StartStats
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        group_by=group_by,
        app=app,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    group_by: list[GetStartStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
) -> Response[Problem | StartStats]:
    """Get start times

     How many game servers you started and how fast our replies were (p50 and p95 of the successful
    starts, measured at our API edge), for one period of at most 92 days. Group by region, app or start
    mode. Starts refused for your own reasons (validation, limits) are not counted; `failed` counts our
    failures.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        group_by (list[GetStartStatsGroupByItem] | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StartStats]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        group_by=group_by,
        app=app,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    group_by: list[GetStartStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
) -> Problem | StartStats | None:
    """Get start times

     How many game servers you started and how fast our replies were (p50 and p95 of the successful
    starts, measured at our API edge), for one period of at most 92 days. Group by region, app or start
    mode. Starts refused for your own reasons (validation, limits) are not counted; `failed` counts our
    failures.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        group_by (list[GetStartStatsGroupByItem] | Unset):
        app (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StartStats
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            group_by=group_by,
            app=app,
        )
    ).parsed

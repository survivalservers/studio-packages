import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_server_stats import GameServerStats
from ...models.get_game_server_stats_group_by_item import GetGameServerStatsGroupByItem
from ...models.get_game_server_stats_kind import GetGameServerStatsKind
from ...models.problem import Problem
from ...models.stats_step import StatsStep
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: StatsStep | Unset = UNSET,
    group_by: list[GetGameServerStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    kind: GetGameServerStatsKind | Unset = UNSET,
    label: list[str] | Unset = UNSET,
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

    json_step: str | Unset = UNSET
    if not isinstance(step, Unset):
        json_step = step.value

    params["step"] = json_step

    json_group_by: list[str] | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = []
        for group_by_item_data in group_by:
            group_by_item = group_by_item_data.value
            json_group_by.append(group_by_item)

    params["group_by"] = json_group_by

    params["app"] = app

    params["region"] = region

    params["persistent_server"] = persistent_server

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/stats/game-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GameServerStats | Problem:
    if response.status_code == 200:
        response_200 = GameServerStats.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GameServerStats | Problem]:
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
    step: StatsStep | Unset = UNSET,
    group_by: list[GetGameServerStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    kind: GetGameServerStatsKind | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[GameServerStats | Problem]:
    """Get game server history

     Your game servers over time, one bucket per `step`: how many ran, players, vCPUs in use, starts,
    crashes and stops, for one period of at most 92 days. Averages are time-weighted over the bucket;
    peaks are the most at any moment. Buckets start on UTC step boundaries, and a partial last bucket
    covers up to `to`. Every bucket is present for every group, zeros included. Players are what your
    game reports through the SDK. `starts` and `failed_starts` count as in `/v0/stats/starts`.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (StatsStep | Unset): A bucket's length.
        group_by (list[GetGameServerStatsGroupByItem] | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        persistent_server (str | Unset): Persistent server ID.
        kind (GetGameServerStatsKind | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerStats | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        step=step,
        group_by=group_by,
        app=app,
        region=region,
        persistent_server=persistent_server,
        kind=kind,
        label=label,
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
    step: StatsStep | Unset = UNSET,
    group_by: list[GetGameServerStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    kind: GetGameServerStatsKind | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> GameServerStats | Problem | None:
    """Get game server history

     Your game servers over time, one bucket per `step`: how many ran, players, vCPUs in use, starts,
    crashes and stops, for one period of at most 92 days. Averages are time-weighted over the bucket;
    peaks are the most at any moment. Buckets start on UTC step boundaries, and a partial last bucket
    covers up to `to`. Every bucket is present for every group, zeros included. Players are what your
    game reports through the SDK. `starts` and `failed_starts` count as in `/v0/stats/starts`.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (StatsStep | Unset): A bucket's length.
        group_by (list[GetGameServerStatsGroupByItem] | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        persistent_server (str | Unset): Persistent server ID.
        kind (GetGameServerStatsKind | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerStats | Problem
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        step=step,
        group_by=group_by,
        app=app,
        region=region,
        persistent_server=persistent_server,
        kind=kind,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: StatsStep | Unset = UNSET,
    group_by: list[GetGameServerStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    kind: GetGameServerStatsKind | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[GameServerStats | Problem]:
    """Get game server history

     Your game servers over time, one bucket per `step`: how many ran, players, vCPUs in use, starts,
    crashes and stops, for one period of at most 92 days. Averages are time-weighted over the bucket;
    peaks are the most at any moment. Buckets start on UTC step boundaries, and a partial last bucket
    covers up to `to`. Every bucket is present for every group, zeros included. Players are what your
    game reports through the SDK. `starts` and `failed_starts` count as in `/v0/stats/starts`.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (StatsStep | Unset): A bucket's length.
        group_by (list[GetGameServerStatsGroupByItem] | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        persistent_server (str | Unset): Persistent server ID.
        kind (GetGameServerStatsKind | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerStats | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        step=step,
        group_by=group_by,
        app=app,
        region=region,
        persistent_server=persistent_server,
        kind=kind,
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: StatsStep | Unset = UNSET,
    group_by: list[GetGameServerStatsGroupByItem] | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    persistent_server: str | Unset = UNSET,
    kind: GetGameServerStatsKind | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> GameServerStats | Problem | None:
    """Get game server history

     Your game servers over time, one bucket per `step`: how many ran, players, vCPUs in use, starts,
    crashes and stops, for one period of at most 92 days. Averages are time-weighted over the bucket;
    peaks are the most at any moment. Buckets start on UTC step boundaries, and a partial last bucket
    covers up to `to`. Every bucket is present for every group, zeros included. Players are what your
    game reports through the SDK. `starts` and `failed_starts` count as in `/v0/stats/starts`.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (StatsStep | Unset): A bucket's length.
        group_by (list[GetGameServerStatsGroupByItem] | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        persistent_server (str | Unset): Persistent server ID.
        kind (GetGameServerStatsKind | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerStats | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            step=step,
            group_by=group_by,
            app=app,
            region=region,
            persistent_server=persistent_server,
            kind=kind,
            label=label,
        )
    ).parsed

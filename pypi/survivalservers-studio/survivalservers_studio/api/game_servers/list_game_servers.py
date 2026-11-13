import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_server_list import GameServerList
from ...models.game_server_status import GameServerStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    region: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    status: list[GameServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    external_id: str | Unset = UNSET,
    players_below: int | Unset = UNSET,
    players_above: int | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["app"] = app

    params["version"] = version

    params["region"] = region

    params["continent"] = continent

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_label: list[str] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params["external_id"] = external_id

    params["players_below"] = players_below

    params["players_above"] = players_above

    json_created_after: str | Unset = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_before: str | Unset = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    params["by"] = by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GameServerList | Problem:
    if response.status_code == 200:
        response_200 = GameServerList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GameServerList | Problem]:
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
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    region: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    status: list[GameServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    external_id: str | Unset = UNSET,
    players_below: int | Unset = UNSET,
    players_above: int | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    by: str | Unset = UNSET,
) -> Response[GameServerList | Problem]:
    """List game servers

     Newest first. By default only `starting`, `running` and `stopping`; pass `status=stopped,failed` to
    see ended ones (kept 90 days). Warm game servers appear only once allocated.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        version (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        status (list[GameServerStatus] | Unset):
        label (list[str] | Unset):
        external_id (str | Unset):
        players_below (int | Unset):
        players_above (int | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
        version=version,
        region=region,
        continent=continent,
        status=status,
        label=label,
        external_id=external_id,
        players_below=players_below,
        players_above=players_above,
        created_after=created_after,
        created_before=created_before,
        by=by,
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
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    region: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    status: list[GameServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    external_id: str | Unset = UNSET,
    players_below: int | Unset = UNSET,
    players_above: int | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    by: str | Unset = UNSET,
) -> GameServerList | Problem | None:
    """List game servers

     Newest first. By default only `starting`, `running` and `stopping`; pass `status=stopped,failed` to
    see ended ones (kept 90 days). Warm game servers appear only once allocated.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        version (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        status (list[GameServerStatus] | Unset):
        label (list[str] | Unset):
        external_id (str | Unset):
        players_below (int | Unset):
        players_above (int | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        app=app,
        version=version,
        region=region,
        continent=continent,
        status=status,
        label=label,
        external_id=external_id,
        players_below=players_below,
        players_above=players_above,
        created_after=created_after,
        created_before=created_before,
        by=by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    region: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    status: list[GameServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    external_id: str | Unset = UNSET,
    players_below: int | Unset = UNSET,
    players_above: int | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    by: str | Unset = UNSET,
) -> Response[GameServerList | Problem]:
    """List game servers

     Newest first. By default only `starting`, `running` and `stopping`; pass `status=stopped,failed` to
    see ended ones (kept 90 days). Warm game servers appear only once allocated.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        version (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        status (list[GameServerStatus] | Unset):
        label (list[str] | Unset):
        external_id (str | Unset):
        players_below (int | Unset):
        players_above (int | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
        version=version,
        region=region,
        continent=continent,
        status=status,
        label=label,
        external_id=external_id,
        players_below=players_below,
        players_above=players_above,
        created_after=created_after,
        created_before=created_before,
        by=by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    version: str | Unset = UNSET,
    region: str | Unset = UNSET,
    continent: str | Unset = UNSET,
    status: list[GameServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
    external_id: str | Unset = UNSET,
    players_below: int | Unset = UNSET,
    players_above: int | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    by: str | Unset = UNSET,
) -> GameServerList | Problem | None:
    """List game servers

     Newest first. By default only `starting`, `running` and `stopping`; pass `status=stopped,failed` to
    see ended ones (kept 90 days). Warm game servers appear only once allocated.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        version (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`,
            `middle-east`, `africa`.
        status (list[GameServerStatus] | Unset):
        label (list[str] | Unset):
        external_id (str | Unset):
        players_below (int | Unset):
        players_above (int | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            app=app,
            version=version,
            region=region,
            continent=continent,
            status=status,
            label=label,
            external_id=external_id,
            players_below=players_below,
            players_above=players_above,
            created_after=created_after,
            created_before=created_before,
            by=by,
        )
    ).parsed

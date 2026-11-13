from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.persistent_server_list import PersistentServerList
from ...models.persistent_server_status import PersistentServerStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    status: list[PersistentServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["app"] = app

    params["region"] = region

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/persistent-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PersistentServerList | Problem:
    if response.status_code == 200:
        response_200 = PersistentServerList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PersistentServerList | Problem]:
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
    region: str | Unset = UNSET,
    status: list[PersistentServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[PersistentServerList | Problem]:
    """List persistent servers

     Newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        status (list[PersistentServerStatus] | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
        region=region,
        status=status,
        label=label,
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
    region: str | Unset = UNSET,
    status: list[PersistentServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> PersistentServerList | Problem | None:
    """List persistent servers

     Newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        status (list[PersistentServerStatus] | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        app=app,
        region=region,
        status=status,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    status: list[PersistentServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> Response[PersistentServerList | Problem]:
    """List persistent servers

     Newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        status (list[PersistentServerStatus] | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        app=app,
        region=region,
        status=status,
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    app: str | Unset = UNSET,
    region: str | Unset = UNSET,
    status: list[PersistentServerStatus] | Unset = UNSET,
    label: list[str] | Unset = UNSET,
) -> PersistentServerList | Problem | None:
    """List persistent servers

     Newest first.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        app (str | Unset):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`,
            `europe-west`, `uk`. An older region ID is still accepted, and answers carry the new one.
        status (list[PersistentServerStatus] | Unset):
        label (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            app=app,
            region=region,
            status=status,
            label=label,
        )
    ).parsed

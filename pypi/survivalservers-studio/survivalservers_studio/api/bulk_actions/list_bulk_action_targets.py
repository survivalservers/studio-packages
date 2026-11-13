from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_target_list import BulkActionTargetList
from ...models.bulk_action_target_status import BulkActionTargetStatus
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[BulkActionTargetStatus] | Unset = UNSET,
    batch: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["batch"] = batch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/bulk-actions/{id}/targets".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkActionTargetList | Problem:
    if response.status_code == 200:
        response_200 = BulkActionTargetList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkActionTargetList | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[BulkActionTargetStatus] | Unset = UNSET,
    batch: int | Unset = UNSET,
) -> Response[BulkActionTargetList | Problem]:
    """List a bulk action's targets

     Each persistent_server, game server or pool with its batch, result, answer or error, in batch order.

    Args:
        id (str): Bulk action ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (list[BulkActionTargetStatus] | Unset):
        batch (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionTargetList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        status=status,
        batch=batch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[BulkActionTargetStatus] | Unset = UNSET,
    batch: int | Unset = UNSET,
) -> BulkActionTargetList | Problem | None:
    """List a bulk action's targets

     Each persistent_server, game server or pool with its batch, result, answer or error, in batch order.

    Args:
        id (str): Bulk action ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (list[BulkActionTargetStatus] | Unset):
        batch (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionTargetList | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
        batch=batch,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[BulkActionTargetStatus] | Unset = UNSET,
    batch: int | Unset = UNSET,
) -> Response[BulkActionTargetList | Problem]:
    """List a bulk action's targets

     Each persistent_server, game server or pool with its batch, result, answer or error, in batch order.

    Args:
        id (str): Bulk action ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (list[BulkActionTargetStatus] | Unset):
        batch (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionTargetList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        status=status,
        batch=batch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[BulkActionTargetStatus] | Unset = UNSET,
    batch: int | Unset = UNSET,
) -> BulkActionTargetList | Problem | None:
    """List a bulk action's targets

     Each persistent_server, game server or pool with its batch, result, answer or error, in batch order.

    Args:
        id (str): Bulk action ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        status (list[BulkActionTargetStatus] | Unset):
        batch (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionTargetList | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
            batch=batch,
        )
    ).parsed

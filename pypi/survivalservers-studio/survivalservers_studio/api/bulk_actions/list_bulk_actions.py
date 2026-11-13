from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_list import BulkActionList
from ...models.bulk_action_status import BulkActionStatus
from ...models.bulk_action_type import BulkActionType
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: list[BulkActionType] | Unset = UNSET,
    status: list[BulkActionStatus] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/bulk-actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkActionList | Problem:
    if response.status_code == 200:
        response_200 = BulkActionList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkActionList | Problem]:
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
    type_: list[BulkActionType] | Unset = UNSET,
    status: list[BulkActionStatus] | Unset = UNSET,
) -> Response[BulkActionList | Problem]:
    """List bulk actions

     Newest first; kept 90 days after they end. A key limited to some apps sees only bulk actions whose
    targets are all in its apps.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        type_ (list[BulkActionType] | Unset):
        status (list[BulkActionStatus] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        type_=type_,
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
    type_: list[BulkActionType] | Unset = UNSET,
    status: list[BulkActionStatus] | Unset = UNSET,
) -> BulkActionList | Problem | None:
    """List bulk actions

     Newest first; kept 90 days after they end. A key limited to some apps sees only bulk actions whose
    targets are all in its apps.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        type_ (list[BulkActionType] | Unset):
        status (list[BulkActionStatus] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        type_=type_,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: list[BulkActionType] | Unset = UNSET,
    status: list[BulkActionStatus] | Unset = UNSET,
) -> Response[BulkActionList | Problem]:
    """List bulk actions

     Newest first; kept 90 days after they end. A key limited to some apps sees only bulk actions whose
    targets are all in its apps.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        type_ (list[BulkActionType] | Unset):
        status (list[BulkActionStatus] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        type_=type_,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    type_: list[BulkActionType] | Unset = UNSET,
    status: list[BulkActionStatus] | Unset = UNSET,
) -> BulkActionList | Problem | None:
    """List bulk actions

     Newest first; kept 90 days after they end. A key limited to some apps sees only bulk actions whose
    targets are all in its apps.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        type_ (list[BulkActionType] | Unset):
        status (list[BulkActionStatus] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            type_=type_,
            status=status,
        )
    ).parsed

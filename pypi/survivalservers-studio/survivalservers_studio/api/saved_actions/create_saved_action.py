from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.saved_action import SavedAction
from ...models.saved_action_create import SavedActionCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SavedActionCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/saved-actions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SavedAction:
    if response.status_code == 201:
        response_201 = SavedAction.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | SavedAction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedActionCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SavedAction]:
    """Create a saved action

     Keeps a bulk action's request under a name, to run again with `POST /v0/saved-actions/{id}/run` or
    by itself on a `schedule`. The request is checked as a dry run. Each run works out its targets
    again, names what it skips and shows in the bulk actions list like any other.

    Args:
        idempotency_key (str | Unset):
        body (SavedActionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SavedAction]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SavedActionCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SavedAction | None:
    """Create a saved action

     Keeps a bulk action's request under a name, to run again with `POST /v0/saved-actions/{id}/run` or
    by itself on a `schedule`. The request is checked as a dry run. Each run works out its targets
    again, names what it skips and shows in the bulk actions list like any other.

    Args:
        idempotency_key (str | Unset):
        body (SavedActionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SavedAction
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedActionCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | SavedAction]:
    """Create a saved action

     Keeps a bulk action's request under a name, to run again with `POST /v0/saved-actions/{id}/run` or
    by itself on a `schedule`. The request is checked as a dry run. Each run works out its targets
    again, names what it skips and shows in the bulk actions list like any other.

    Args:
        idempotency_key (str | Unset):
        body (SavedActionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SavedAction]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SavedActionCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | SavedAction | None:
    """Create a saved action

     Keeps a bulk action's request under a name, to run again with `POST /v0/saved-actions/{id}/run` or
    by itself on a `schedule`. The request is checked as a dry run. Each run works out its targets
    again, names what it skips and shows in the bulk actions list like any other.

    Args:
        idempotency_key (str | Unset):
        body (SavedActionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SavedAction
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

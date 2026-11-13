from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.app import App
from ...models.app_update import AppUpdate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app: str,
    *,
    body: AppUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/apps/{app}".format(
            app=quote(str(app), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> App | Problem:
    if response.status_code == 200:
        response_200 = App.from_dict(response.json())

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
) -> Response[App | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[App | Problem]:
    """Update an app

     Changes the name, tier, default placement or color. The operating system cannot change.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    idempotency_key: str | Unset = UNSET,
) -> App | Problem | None:
    """Update an app

     Changes the name, tier, default placement or color. The operating system cannot change.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | Problem
    """

    return sync_detailed(
        app=app,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[App | Problem]:
    """Update an app

     Changes the name, tier, default placement or color. The operating system cannot change.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    idempotency_key: str | Unset = UNSET,
) -> App | Problem | None:
    """Update an app

     Changes the name, tier, default placement or color. The operating system cannot change.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

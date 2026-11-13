from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.build import Build
from ...models.build_create import BuildCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app: str,
    *,
    body: BuildCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/apps/{app}/builds".format(
            app=quote(str(app), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Build | Problem:
    if response.status_code == 201:
        response_201 = Build.from_dict(response.json())

        return response_201

    if response.status_code == 202:
        response_202 = Build.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Build | Problem]:
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
    body: BuildCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Build | Problem]:
    """Create a build

     Windows: describe the zip and get presigned part URLs (`201`, `awaiting_upload`). `PUT` each part
    straight to
    storage, keep each part's `ETag`, then call complete.

    Linux: name an image in any registry (`202`, `processing`); we copy it into ours, pinned by digest,
    so your
    registry being down never blocks a start.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (BuildCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Build | Problem]
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
    body: BuildCreate,
    idempotency_key: str | Unset = UNSET,
) -> Build | Problem | None:
    """Create a build

     Windows: describe the zip and get presigned part URLs (`201`, `awaiting_upload`). `PUT` each part
    straight to
    storage, keep each part's `ETag`, then call complete.

    Linux: name an image in any registry (`202`, `processing`); we copy it into ours, pinned by digest,
    so your
    registry being down never blocks a start.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (BuildCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Build | Problem
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
    body: BuildCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Build | Problem]:
    """Create a build

     Windows: describe the zip and get presigned part URLs (`201`, `awaiting_upload`). `PUT` each part
    straight to
    storage, keep each part's `ETag`, then call complete.

    Linux: name an image in any registry (`202`, `processing`); we copy it into ours, pinned by digest,
    so your
    registry being down never blocks a start.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (BuildCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Build | Problem]
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
    body: BuildCreate,
    idempotency_key: str | Unset = UNSET,
) -> Build | Problem | None:
    """Create a build

     Windows: describe the zip and get presigned part URLs (`201`, `awaiting_upload`). `PUT` each part
    straight to
    storage, keep each part's `ETag`, then call complete.

    Linux: name an image in any registry (`202`, `processing`); we copy it into ours, pinned by digest,
    so your
    registry being down never blocks a start.

    Args:
        app (str):
        idempotency_key (str | Unset):
        body (BuildCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Build | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

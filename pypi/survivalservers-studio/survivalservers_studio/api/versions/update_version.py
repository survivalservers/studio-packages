from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.version import Version
from ...models.version_update import VersionUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app: str,
    version: str,
    *,
    body: VersionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/apps/{app}/versions/{version}".format(
            app=quote(str(app), safe=""),
            version=quote(str(version), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Version:
    if response.status_code == 200:
        response_200 = Version.from_dict(response.json())

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
) -> Response[Problem | Version]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: VersionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Version]:
    """Change a version

     Only `deprecated` (no new starts) and the target region list can change; everything else is fixed so
    a version name always means the same thing.

    Args:
        app (str):
        version (str):
        idempotency_key (str | Unset):
        body (VersionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Version]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: VersionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Version | None:
    """Change a version

     Only `deprecated` (no new starts) and the target region list can change; everything else is fixed so
    a version name always means the same thing.

    Args:
        app (str):
        version (str):
        idempotency_key (str | Unset):
        body (VersionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Version
    """

    return sync_detailed(
        app=app,
        version=version,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: VersionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Version]:
    """Change a version

     Only `deprecated` (no new starts) and the target region list can change; everything else is fixed so
    a version name always means the same thing.

    Args:
        app (str):
        version (str):
        idempotency_key (str | Unset):
        body (VersionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Version]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: VersionUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Version | None:
    """Change a version

     Only `deprecated` (no new starts) and the target region list can change; everything else is fixed so
    a version name always means the same thing.

    Args:
        app (str):
        version (str):
        idempotency_key (str | Unset):
        body (VersionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Version
    """

    return (
        await asyncio_detailed(
            app=app,
            version=version,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

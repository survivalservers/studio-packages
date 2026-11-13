from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.branch_map import BranchMap
from ...models.branch_set import BranchSet
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    app: str,
    branch: str,
    *,
    body: BranchSet,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/apps/{app}/branches/{branch}".format(
            app=quote(str(app), safe=""),
            branch=quote(str(branch), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BranchMap | Problem:
    if response.status_code == 200:
        response_200 = BranchMap.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[BranchMap | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BranchSet,
) -> Response[BranchMap | Problem]:
    """Set a branch's version

     Creates the branch or sets the version it runs. A new version on a branch is the update; the old one
    set back is the rollback. Pools on the branch start new slots, a few at a time, once the new version
    is copied to their region, and keep their ready slots of the old version until as many new ones are
    ready, so starts that name the old version stay warm. Persistent servers that follow the branch take
    the new version at their next restart; a stopped one at once.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.
        body (BranchSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchMap | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        branch=branch,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BranchSet,
) -> BranchMap | Problem | None:
    """Set a branch's version

     Creates the branch or sets the version it runs. A new version on a branch is the update; the old one
    set back is the rollback. Pools on the branch start new slots, a few at a time, once the new version
    is copied to their region, and keep their ready slots of the old version until as many new ones are
    ready, so starts that name the old version stay warm. Persistent servers that follow the branch take
    the new version at their next restart; a stopped one at once.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.
        body (BranchSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchMap | Problem
    """

    return sync_detailed(
        app=app,
        branch=branch,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BranchSet,
) -> Response[BranchMap | Problem]:
    """Set a branch's version

     Creates the branch or sets the version it runs. A new version on a branch is the update; the old one
    set back is the rollback. Pools on the branch start new slots, a few at a time, once the new version
    is copied to their region, and keep their ready slots of the old version until as many new ones are
    ready, so starts that name the old version stay warm. Persistent servers that follow the branch take
    the new version at their next restart; a stopped one at once.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.
        body (BranchSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchMap | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        branch=branch,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BranchSet,
) -> BranchMap | Problem | None:
    """Set a branch's version

     Creates the branch or sets the version it runs. A new version on a branch is the update; the old one
    set back is the rollback. Pools on the branch start new slots, a few at a time, once the new version
    is copied to their region, and keep their ready slots of the old version until as many new ones are
    ready, so starts that name the old version stay warm. Persistent servers that follow the branch take
    the new version at their next restart; a stopped one at once.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.
        body (BranchSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchMap | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            branch=branch,
            client=client,
            body=body,
        )
    ).parsed

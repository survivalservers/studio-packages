from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    app: str,
    branch: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v0/apps/{app}/branches/{branch}".format(
            app=quote(str(app), safe=""),
            branch=quote(str(branch), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Problem:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Problem]:
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
) -> Response[Any | Problem]:
    """Delete a branch

     Removes the branch; its version stays. `409 in_use`, naming them, while a pool or a persistent
    server (running or stopped) follows the branch; set them to another branch or a version first. Game
    servers keep the version they started on, so they never hold a branch.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        branch=branch,
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
) -> Any | Problem | None:
    """Delete a branch

     Removes the branch; its version stays. `409 in_use`, naming them, while a pool or a persistent
    server (running or stopped) follows the branch; set them to another branch or a version first. Game
    servers keep the version they started on, so they never hold a branch.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return sync_detailed(
        app=app,
        branch=branch,
        client=client,
    ).parsed


async def asyncio_detailed(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Problem]:
    """Delete a branch

     Removes the branch; its version stays. `409 in_use`, naming them, while a pool or a persistent
    server (running or stopped) follows the branch; set them to another branch or a version first. Game
    servers keep the version they started on, so they never hold a branch.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    branch: str,
    *,
    client: AuthenticatedClient,
) -> Any | Problem | None:
    """Delete a branch

     Removes the branch; its version stays. `409 in_use`, naming them, while a pool or a persistent
    server (running or stopped) follows the branch; set them to another branch or a version first. Game
    servers keep the version they started on, so they never hold a branch.

    Args:
        app (str):
        branch (str): Branch name, for example `live`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            branch=branch,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_profile import GameProfile
from ...models.problem import Problem
from ...models.version_profile import VersionProfile
from ...types import Response


def _get_kwargs(
    app: str,
    version: str,
    *,
    body: GameProfile,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/apps/{app}/versions/{version}/profile".format(
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
) -> Problem | VersionProfile:
    if response.status_code == 200:
        response_200 = VersionProfile.from_dict(response.json())

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
) -> Response[Problem | VersionProfile]:
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
    body: GameProfile,
) -> Response[Problem | VersionProfile]:
    """Set a version's game profile

     Replaces the whole profile; `{}` clears it. A profile can change after a version is made, because it
    changes no bytes of the build. Each save adds one to `revision` and an audit line. Connections are
    checked against the version: their `port` must be one of its ports and `password_env` one of its env
    values.

    Args:
        app (str):
        version (str):
        body (GameProfile): One description of a server, read by the panel, the API, the CLI and
            AI tools: how to reach the game and the commands it takes. Plain JSON, and every part is
            optional. Secrets stay in the version's env values; a profile only names them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionProfile]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
        body=body,
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
    body: GameProfile,
) -> Problem | VersionProfile | None:
    """Set a version's game profile

     Replaces the whole profile; `{}` clears it. A profile can change after a version is made, because it
    changes no bytes of the build. Each save adds one to `revision` and an audit line. Connections are
    checked against the version: their `port` must be one of its ports and `password_env` one of its env
    values.

    Args:
        app (str):
        version (str):
        body (GameProfile): One description of a server, read by the panel, the API, the CLI and
            AI tools: how to reach the game and the commands it takes. Plain JSON, and every part is
            optional. Secrets stay in the version's env values; a profile only names them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VersionProfile
    """

    return sync_detailed(
        app=app,
        version=version,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: GameProfile,
) -> Response[Problem | VersionProfile]:
    """Set a version's game profile

     Replaces the whole profile; `{}` clears it. A profile can change after a version is made, because it
    changes no bytes of the build. Each save adds one to `revision` and an audit line. Connections are
    checked against the version: their `port` must be one of its ports and `password_env` one of its env
    values.

    Args:
        app (str):
        version (str):
        body (GameProfile): One description of a server, read by the panel, the API, the CLI and
            AI tools: how to reach the game and the commands it takes. Plain JSON, and every part is
            optional. Secrets stay in the version's env values; a profile only names them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionProfile]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
    body: GameProfile,
) -> Problem | VersionProfile | None:
    """Set a version's game profile

     Replaces the whole profile; `{}` clears it. A profile can change after a version is made, because it
    changes no bytes of the build. Each save adds one to `revision` and an audit line. Connections are
    checked against the version: their `port` must be one of its ports and `password_env` one of its env
    values.

    Args:
        app (str):
        version (str):
        body (GameProfile): One description of a server, read by the panel, the API, the CLI and
            AI tools: how to reach the game and the commands it takes. Plain JSON, and every part is
            optional. Secrets stay in the version's env values; a profile only names them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VersionProfile
    """

    return (
        await asyncio_detailed(
            app=app,
            version=version,
            client=client,
            body=body,
        )
    ).parsed

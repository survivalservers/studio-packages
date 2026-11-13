from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.version_profile import VersionProfile
from ...types import Response


def _get_kwargs(
    app: str,
    version: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/apps/{app}/versions/{version}/profile".format(
            app=quote(str(app), safe=""),
            version=quote(str(version), safe=""),
        ),
    }

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
) -> Response[Problem | VersionProfile]:
    """Get a version's game profile

     The version's game profile and its revision. A version with none answers an empty profile and
    revision 0.

    Args:
        app (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionProfile]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
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
) -> Problem | VersionProfile | None:
    """Get a version's game profile

     The version's game profile and its revision. A version with none answers an empty profile and
    revision 0.

    Args:
        app (str):
        version (str):

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
    ).parsed


async def asyncio_detailed(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | VersionProfile]:
    """Get a version's game profile

     The version's game profile and its revision. A version with none answers an empty profile and
    revision 0.

    Args:
        app (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VersionProfile]
    """

    kwargs = _get_kwargs(
        app=app,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Problem | VersionProfile | None:
    """Get a version's game profile

     The version's game profile and its revision. A version with none answers an empty profile and
    revision 0.

    Args:
        app (str):
        version (str):

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
        )
    ).parsed

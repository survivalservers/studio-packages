from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.two_factor_methods import TwoFactorMethods
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/me/two-factor-methods",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | TwoFactorMethods:
    if response.status_code == 200:
        response_200 = TwoFactorMethods.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | TwoFactorMethods]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Problem | TwoFactorMethods]:
    """List your own 2FA methods

     The signed-in person's own two-factor authentication (2FA) methods, as Profile shows them: each
    one's kind, the name it was given and when it was set up. Never anyone else's, and never the
    password. People only: no API key can call it, whatever its scopes. To remove one, Profile sends the
    person to sign in again with a different kind of 2FA, where the method is removed; there is no API
    call that removes one. People who sign in through their company keep their 2FA there, so their list
    is usually empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TwoFactorMethods]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Problem | TwoFactorMethods | None:
    """List your own 2FA methods

     The signed-in person's own two-factor authentication (2FA) methods, as Profile shows them: each
    one's kind, the name it was given and when it was set up. Never anyone else's, and never the
    password. People only: no API key can call it, whatever its scopes. To remove one, Profile sends the
    person to sign in again with a different kind of 2FA, where the method is removed; there is no API
    call that removes one. People who sign in through their company keep their 2FA there, so their list
    is usually empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TwoFactorMethods
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Problem | TwoFactorMethods]:
    """List your own 2FA methods

     The signed-in person's own two-factor authentication (2FA) methods, as Profile shows them: each
    one's kind, the name it was given and when it was set up. Never anyone else's, and never the
    password. People only: no API key can call it, whatever its scopes. To remove one, Profile sends the
    person to sign in again with a different kind of 2FA, where the method is removed; there is no API
    call that removes one. People who sign in through their company keep their 2FA there, so their list
    is usually empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | TwoFactorMethods]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Problem | TwoFactorMethods | None:
    """List your own 2FA methods

     The signed-in person's own two-factor authentication (2FA) methods, as Profile shows them: each
    one's kind, the name it was given and when it was set up. Never anyone else's, and never the
    password. People only: no API key can call it, whatever its scopes. To remove one, Profile sends the
    person to sign in again with a different kind of 2FA, where the method is removed; there is no API
    call that removes one. People who sign in through their company keep their 2FA there, so their list
    is usually empty.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | TwoFactorMethods
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

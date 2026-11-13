from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.sso import Sso
from ...models.sso_put import SsoPut
from ...types import Response


def _get_kwargs(
    *,
    body: SsoPut,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/sso",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Sso:
    if response.status_code == 200:
        response_200 = Sso.from_dict(response.json())

        return response_200

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
) -> Response[Problem | Sso]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SsoPut,
) -> Response[Problem | Sso]:
    """Set single sign-on

     Saves the studio's own sign-in provider (OIDC or SAML) and its email domains, and switches single
    sign-on on or off. A domain counts once its DNS TXT record (in `domain_records`) is found. Register
    `redirect_uri` at your provider. Leave out `oidc_client_secret` to keep the one saved. Public email
    services cannot be connected, and a domain another studio has proven answers `409 name_taken`.
    Owners only. Switching on (`enabled: true` when it was off) needs three things, or it answers `422`:
    the provider as saved (change it while off), at least one proven domain, and a test, which is that
    the sign-in making this call came through the provider (`signed_in_through_provider`: sign in with
    it first, from the panel), so a broken provider never locks the studio out. It also needs
    `emergency_owner`, an owner with a password and a one-time code. Once on, whoever signs in with an
    email in a proven domain goes to your provider: every account there loses its password (`moving`
    counts them before you switch on) and joins the provider by email at its next sign-in, except the
    emergency owner, who keeps a password and a one-time code as the way in if the provider fails. While
    on, the provider cannot be changed; turn it off first.

    Args:
        body (SsoPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Sso]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SsoPut,
) -> Problem | Sso | None:
    """Set single sign-on

     Saves the studio's own sign-in provider (OIDC or SAML) and its email domains, and switches single
    sign-on on or off. A domain counts once its DNS TXT record (in `domain_records`) is found. Register
    `redirect_uri` at your provider. Leave out `oidc_client_secret` to keep the one saved. Public email
    services cannot be connected, and a domain another studio has proven answers `409 name_taken`.
    Owners only. Switching on (`enabled: true` when it was off) needs three things, or it answers `422`:
    the provider as saved (change it while off), at least one proven domain, and a test, which is that
    the sign-in making this call came through the provider (`signed_in_through_provider`: sign in with
    it first, from the panel), so a broken provider never locks the studio out. It also needs
    `emergency_owner`, an owner with a password and a one-time code. Once on, whoever signs in with an
    email in a proven domain goes to your provider: every account there loses its password (`moving`
    counts them before you switch on) and joins the provider by email at its next sign-in, except the
    emergency owner, who keeps a password and a one-time code as the way in if the provider fails. While
    on, the provider cannot be changed; turn it off first.

    Args:
        body (SsoPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Sso
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SsoPut,
) -> Response[Problem | Sso]:
    """Set single sign-on

     Saves the studio's own sign-in provider (OIDC or SAML) and its email domains, and switches single
    sign-on on or off. A domain counts once its DNS TXT record (in `domain_records`) is found. Register
    `redirect_uri` at your provider. Leave out `oidc_client_secret` to keep the one saved. Public email
    services cannot be connected, and a domain another studio has proven answers `409 name_taken`.
    Owners only. Switching on (`enabled: true` when it was off) needs three things, or it answers `422`:
    the provider as saved (change it while off), at least one proven domain, and a test, which is that
    the sign-in making this call came through the provider (`signed_in_through_provider`: sign in with
    it first, from the panel), so a broken provider never locks the studio out. It also needs
    `emergency_owner`, an owner with a password and a one-time code. Once on, whoever signs in with an
    email in a proven domain goes to your provider: every account there loses its password (`moving`
    counts them before you switch on) and joins the provider by email at its next sign-in, except the
    emergency owner, who keeps a password and a one-time code as the way in if the provider fails. While
    on, the provider cannot be changed; turn it off first.

    Args:
        body (SsoPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Sso]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SsoPut,
) -> Problem | Sso | None:
    """Set single sign-on

     Saves the studio's own sign-in provider (OIDC or SAML) and its email domains, and switches single
    sign-on on or off. A domain counts once its DNS TXT record (in `domain_records`) is found. Register
    `redirect_uri` at your provider. Leave out `oidc_client_secret` to keep the one saved. Public email
    services cannot be connected, and a domain another studio has proven answers `409 name_taken`.
    Owners only. Switching on (`enabled: true` when it was off) needs three things, or it answers `422`:
    the provider as saved (change it while off), at least one proven domain, and a test, which is that
    the sign-in making this call came through the provider (`signed_in_through_provider`: sign in with
    it first, from the panel), so a broken provider never locks the studio out. It also needs
    `emergency_owner`, an owner with a password and a one-time code. Once on, whoever signs in with an
    email in a proven domain goes to your provider: every account there loses its password (`moving`
    counts them before you switch on) and joins the provider by email at its next sign-in, except the
    emergency owner, who keeps a password and a one-time code as the way in if the provider fails. While
    on, the provider cannot be changed; turn it off first.

    Args:
        body (SsoPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Sso
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

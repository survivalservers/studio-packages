from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.registry_token import RegistryToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/registry/token",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RegistryToken:
    if response.status_code == 200:
        response_200 = RegistryToken.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | RegistryToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | RegistryToken]:
    """Get a registry push login

     Returns a short-lived login for `docker login` and `docker push`. Then create the build with the
    pushed image. A login made with an API key stops when the key is revoked; for a key limited to some
    apps it pushes and reads only under each of its apps' `uploads/<studio>/<app id>/` (`repository`
    names it when the key has one app), checked at every request.

    Args:
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegistryToken]
    """

    kwargs = _get_kwargs(
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Problem | RegistryToken | None:
    """Get a registry push login

     Returns a short-lived login for `docker login` and `docker push`. Then create the build with the
    pushed image. A login made with an API key stops when the key is revoked; for a key limited to some
    apps it pushes and reads only under each of its apps' `uploads/<studio>/<app id>/` (`repository`
    names it when the key has one app), checked at every request.

    Args:
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegistryToken
    """

    return sync_detailed(
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | RegistryToken]:
    """Get a registry push login

     Returns a short-lived login for `docker login` and `docker push`. Then create the build with the
    pushed image. A login made with an API key stops when the key is revoked; for a key limited to some
    apps it pushes and reads only under each of its apps' `uploads/<studio>/<app id>/` (`repository`
    names it when the key has one app), checked at every request.

    Args:
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegistryToken]
    """

    kwargs = _get_kwargs(
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Problem | RegistryToken | None:
    """Get a registry push login

     Returns a short-lived login for `docker login` and `docker push`. Then create the build with the
    pushed image. A login made with an API key stops when the key is revoked; for a key limited to some
    apps it pushes and reads only under each of its apps' `uploads/<studio>/<app id>/` (`repository`
    names it when the key has one app), checked at every request.

    Args:
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegistryToken
    """

    return (
        await asyncio_detailed(
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed

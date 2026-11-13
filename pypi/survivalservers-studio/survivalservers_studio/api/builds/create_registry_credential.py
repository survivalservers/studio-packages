from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.registry_credential import RegistryCredential
from ...models.registry_credential_create import RegistryCredentialCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RegistryCredentialCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/registry-credentials",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | RegistryCredential:
    if response.status_code == 201:
        response_201 = RegistryCredential.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | RegistryCredential]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RegistryCredentialCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | RegistryCredential]:
    """Save a login for your registry

     Saves a login we use to copy private images. Write-only; the password is never returned.

    Args:
        idempotency_key (str | Unset):
        body (RegistryCredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegistryCredential]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RegistryCredentialCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | RegistryCredential | None:
    """Save a login for your registry

     Saves a login we use to copy private images. Write-only; the password is never returned.

    Args:
        idempotency_key (str | Unset):
        body (RegistryCredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegistryCredential
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RegistryCredentialCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | RegistryCredential]:
    """Save a login for your registry

     Saves a login we use to copy private images. Write-only; the password is never returned.

    Args:
        idempotency_key (str | Unset):
        body (RegistryCredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | RegistryCredential]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RegistryCredentialCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | RegistryCredential | None:
    """Save a login for your registry

     Saves a login we use to copy private images. Write-only; the password is never returned.

    Args:
        idempotency_key (str | Unset):
        body (RegistryCredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | RegistryCredential
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

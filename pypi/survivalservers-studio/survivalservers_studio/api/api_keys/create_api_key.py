from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_key_create import ApiKeyCreate
from ...models.api_key_with_secret import ApiKeyWithSecret
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ApiKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyWithSecret | Problem:
    if response.status_code == 201:
        response_201 = ApiKeyWithSecret.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyWithSecret | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiKeyWithSecret | Problem]:
    """Create an API key

     `key` is in this reply only. A key can never have scopes its creator lacks. A key made by a key also
    stays inside that key's apps, IP ranges and end date (`403 key_restricted`).

    Args:
        idempotency_key (str | Unset):
        body (ApiKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithSecret | Problem]
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
    body: ApiKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> ApiKeyWithSecret | Problem | None:
    """Create an API key

     `key` is in this reply only. A key can never have scopes its creator lacks. A key made by a key also
    stays inside that key's apps, IP ranges and end date (`403 key_restricted`).

    Args:
        idempotency_key (str | Unset):
        body (ApiKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithSecret | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiKeyWithSecret | Problem]:
    """Create an API key

     `key` is in this reply only. A key can never have scopes its creator lacks. A key made by a key also
    stays inside that key's apps, IP ranges and end date (`403 key_restricted`).

    Args:
        idempotency_key (str | Unset):
        body (ApiKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithSecret | Problem]
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
    body: ApiKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> ApiKeyWithSecret | Problem | None:
    """Create an API key

     `key` is in this reply only. A key can never have scopes its creator lacks. A key made by a key also
    stays inside that key's apps, IP ranges and end date (`403 key_restricted`).

    Args:
        idempotency_key (str | Unset):
        body (ApiKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithSecret | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

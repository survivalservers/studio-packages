from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.config_set import ConfigSet
from ...models.config_set_create import ConfigSetCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConfigSetCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/config-sets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigSet | Problem:
    if response.status_code == 201:
        response_201 = ConfigSet.from_dict(response.json())

        return response_201

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
) -> Response[ConfigSet | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConfigSetCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConfigSet | Problem]:
    """Create a config set

     A named set of settings for one app, with its first version. Apply it to persistent servers with
    `POST /v0/config-sets/{id}/apply`.

    Args:
        idempotency_key (str | Unset):
        body (ConfigSetCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSet | Problem]
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
    body: ConfigSetCreate,
    idempotency_key: str | Unset = UNSET,
) -> ConfigSet | Problem | None:
    """Create a config set

     A named set of settings for one app, with its first version. Apply it to persistent servers with
    `POST /v0/config-sets/{id}/apply`.

    Args:
        idempotency_key (str | Unset):
        body (ConfigSetCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSet | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConfigSetCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConfigSet | Problem]:
    """Create a config set

     A named set of settings for one app, with its first version. Apply it to persistent servers with
    `POST /v0/config-sets/{id}/apply`.

    Args:
        idempotency_key (str | Unset):
        body (ConfigSetCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSet | Problem]
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
    body: ConfigSetCreate,
    idempotency_key: str | Unset = UNSET,
) -> ConfigSet | Problem | None:
    """Create a config set

     A named set of settings for one app, with its first version. Apply it to persistent servers with
    `POST /v0/config-sets/{id}/apply`.

    Args:
        idempotency_key (str | Unset):
        body (ConfigSetCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSet | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

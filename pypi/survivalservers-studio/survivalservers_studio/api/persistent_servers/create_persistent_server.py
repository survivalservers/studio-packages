from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.persistent_server import PersistentServer
from ...models.persistent_server_create import PersistentServerCreate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PersistentServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PersistentServer | Problem:
    if response.status_code == 201:
        response_201 = PersistentServer.from_dict(response.json())

        return response_201

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PersistentServer | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PersistentServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServer | Problem]:
    """Create a persistent server

     A named game server that keeps its saves, address and identity across restarts. Billed per second at
    the reserved rate while running. With `when_empty` it pauses when nobody plays and resumes on the
    first player.

    Args:
        idempotency_key (str | Unset):
        body (PersistentServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServer | Problem]
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
    body: PersistentServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServer | Problem | None:
    """Create a persistent server

     A named game server that keeps its saves, address and identity across restarts. Billed per second at
    the reserved rate while running. With `when_empty` it pauses when nobody plays and resumes on the
    first player.

    Args:
        idempotency_key (str | Unset):
        body (PersistentServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServer | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PersistentServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServer | Problem]:
    """Create a persistent server

     A named game server that keeps its saves, address and identity across restarts. Billed per second at
    the reserved rate while running. With `when_empty` it pauses when nobody plays and resumes on the
    first player.

    Args:
        idempotency_key (str | Unset):
        body (PersistentServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServer | Problem]
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
    body: PersistentServerCreate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServer | Problem | None:
    """Create a persistent server

     A named game server that keeps its saves, address and identity across restarts. Billed per second at
    the reserved rate while running. With `when_empty` it pauses when nobody plays and resumes on the
    first player.

    Args:
        idempotency_key (str | Unset):
        body (PersistentServerCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServer | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

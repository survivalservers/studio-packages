from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.persistent_server import PersistentServer
from ...models.persistent_server_update import PersistentServerUpdate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PersistentServerUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/persistent-servers/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PersistentServer | Problem:
    if response.status_code == 200:
        response_200 = PersistentServer.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[PersistentServer | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PersistentServerUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServer | Problem]:
    """Change a persistent server

     A new version is copied to the machine before it is applied. `apply` is `next_restart` (default) or
    `now` (graceful restart). The new version starts only once the backup taken at the stop is stored,
    as a `before_update` backup; if it is not, the server starts again on its old version and the new
    one waits for the next restart (`update_held` on the run's timeline).

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServer | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PersistentServerUpdate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServer | Problem | None:
    """Change a persistent server

     A new version is copied to the machine before it is applied. `apply` is `next_restart` (default) or
    `now` (graceful restart). The new version starts only once the backup taken at the stop is stored,
    as a `before_update` backup; if it is not, the server starts again on its old version and the new
    one waits for the next restart (`update_held` on the run's timeline).

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServer | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PersistentServerUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServer | Problem]:
    """Change a persistent server

     A new version is copied to the machine before it is applied. `apply` is `next_restart` (default) or
    `now` (graceful restart). The new version starts only once the backup taken at the stop is stored,
    as a `before_update` backup; if it is not, the server starts again on its old version and the new
    one waits for the next restart (`update_held` on the run's timeline).

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServer | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PersistentServerUpdate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServer | Problem | None:
    """Change a persistent server

     A new version is copied to the machine before it is applied. `apply` is `next_restart` (default) or
    `now` (graceful restart). The new version starts only once the backup taken at the stop is stored,
    as a `before_update` backup; if it is not, the server starts again on its old version and the new
    one waits for the next restart (`update_held` on the run's timeline).

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServer | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

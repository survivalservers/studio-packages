from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.persistent_server_config import PersistentServerConfig
from ...models.persistent_server_config_update import PersistentServerConfigUpdate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PersistentServerConfigUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/persistent-servers/{id}/config".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PersistentServerConfig | Problem:
    if response.status_code == 200:
        response_200 = PersistentServerConfig.from_dict(response.json())

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
) -> Response[PersistentServerConfig | Problem]:
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
    body: PersistentServerConfigUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServerConfig | Problem]:
    """Change its game settings

     Sets the server's own values; null removes one. They are written at its next run. With `live`, a
    setting that can change in the running game is also sent now, and `results` says how each one went.
    A config set's value wins over the server's own.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerConfigUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerConfig | Problem]
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
    body: PersistentServerConfigUpdate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServerConfig | Problem | None:
    """Change its game settings

     Sets the server's own values; null removes one. They are written at its next run. With `live`, a
    setting that can change in the running game is also sent now, and `results` says how each one went.
    A config set's value wins over the server's own.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerConfigUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerConfig | Problem
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
    body: PersistentServerConfigUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[PersistentServerConfig | Problem]:
    """Change its game settings

     Sets the server's own values; null removes one. They are written at its next run. With `live`, a
    setting that can change in the running game is also sent now, and `results` says how each one went.
    A config set's value wins over the server's own.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerConfigUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersistentServerConfig | Problem]
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
    body: PersistentServerConfigUpdate,
    idempotency_key: str | Unset = UNSET,
) -> PersistentServerConfig | Problem | None:
    """Change its game settings

     Sets the server's own values; null removes one. They are written at its next run. With `live`, a
    setting that can change in the running game is also sent now, and `results` says how each one went.
    A config set's value wins over the server's own.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerConfigUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersistentServerConfig | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

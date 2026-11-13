from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_result import BulkActionResult
from ...models.persistent_server_restore import PersistentServerRestore
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PersistentServerRestore,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/persistent-servers/{id}/restore".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkActionResult | Problem:
    if response.status_code == 200:
        response_200 = BulkActionResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = BulkActionResult.from_dict(response.json())

        return response_202

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
) -> Response[BulkActionResult | Problem]:
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
    body: PersistentServerRestore,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Restore a backup

     Puts one persistent server back to a backup or a time, as a one-target rollback bulk action. A
    running one is saved and stopped, its current state is backed up, then it is restored and started. A
    stopped one restores at its next start. `dry_run` answers the plan; `persistent_server.restored`
    fires when it is back. With `version: then`, a backup whose version was deleted since is refused
    with 409 `invalid_state`, naming that version, before anything changes: restore it with `version:
    keep`, or pick another backup.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerRestore): Give `backup` or `at`, or the `plan` of a preview.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionResult | Problem]
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
    body: PersistentServerRestore,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Restore a backup

     Puts one persistent server back to a backup or a time, as a one-target rollback bulk action. A
    running one is saved and stopped, its current state is backed up, then it is restored and started. A
    stopped one restores at its next start. `dry_run` answers the plan; `persistent_server.restored`
    fires when it is back. With `version: then`, a backup whose version was deleted since is refused
    with 409 `invalid_state`, naming that version, before anything changes: restore it with `version:
    keep`, or pick another backup.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerRestore): Give `backup` or `at`, or the `plan` of a preview.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionResult | Problem
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
    body: PersistentServerRestore,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Restore a backup

     Puts one persistent server back to a backup or a time, as a one-target rollback bulk action. A
    running one is saved and stopped, its current state is backed up, then it is restored and started. A
    stopped one restores at its next start. `dry_run` answers the plan; `persistent_server.restored`
    fires when it is back. With `version: then`, a backup whose version was deleted since is refused
    with 409 `invalid_state`, naming that version, before anything changes: restore it with `version:
    keep`, or pick another backup.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerRestore): Give `backup` or `at`, or the `plan` of a preview.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkActionResult | Problem]
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
    body: PersistentServerRestore,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Restore a backup

     Puts one persistent server back to a backup or a time, as a one-target rollback bulk action. A
    running one is saved and stopped, its current state is backed up, then it is restored and started. A
    stopped one restores at its next start. `dry_run` answers the plan; `persistent_server.restored`
    fires when it is back. With `version: then`, a backup whose version was deleted since is refused
    with 409 `invalid_state`, naming that version, before anything changes: restore it with `version:
    keep`, or pick another backup.

    Args:
        id (str): Persistent server ID.
        idempotency_key (str | Unset):
        body (PersistentServerRestore): Give `backup` or `at`, or the `plan` of a preview.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkActionResult | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

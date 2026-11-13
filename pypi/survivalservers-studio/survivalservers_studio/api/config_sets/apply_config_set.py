from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_action_result import BulkActionResult
from ...models.config_set_apply import ConfigSetApply
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: ConfigSetApply,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/config-sets/{id}/apply".format(
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

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

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
    body: ConfigSetApply,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Apply a config set version

     Puts the matching persistent servers on a version of the set (or, with `remove`, takes the set off
    them). With `apply` `next_restart` each persistent server takes it at its next run; `now` restarts
    the running ones in rolling batches. The `dry_run` plan groups the persistent servers by what they
    have now and shows the diff for each group. Each persistent server's previous config set version is
    kept for `POST /v0/bulk-actions/{id}/undo`.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigSetApply):

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
    body: ConfigSetApply,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Apply a config set version

     Puts the matching persistent servers on a version of the set (or, with `remove`, takes the set off
    them). With `apply` `next_restart` each persistent server takes it at its next run; `now` restarts
    the running ones in rolling batches. The `dry_run` plan groups the persistent servers by what they
    have now and shows the diff for each group. Each persistent server's previous config set version is
    kept for `POST /v0/bulk-actions/{id}/undo`.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigSetApply):

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
    body: ConfigSetApply,
    idempotency_key: str | Unset = UNSET,
) -> Response[BulkActionResult | Problem]:
    """Apply a config set version

     Puts the matching persistent servers on a version of the set (or, with `remove`, takes the set off
    them). With `apply` `next_restart` each persistent server takes it at its next run; `now` restarts
    the running ones in rolling batches. The `dry_run` plan groups the persistent servers by what they
    have now and shows the diff for each group. Each persistent server's previous config set version is
    kept for `POST /v0/bulk-actions/{id}/undo`.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigSetApply):

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
    body: ConfigSetApply,
    idempotency_key: str | Unset = UNSET,
) -> BulkActionResult | Problem | None:
    """Apply a config set version

     Puts the matching persistent servers on a version of the set (or, with `remove`, takes the set off
    them). With `apply` `next_restart` each persistent server takes it at its next run; `now` restarts
    the running ones in rolling batches. The `dry_run` plan groups the persistent servers by what they
    have now and shows the diff for each group. Each persistent server's previous config set version is
    kept for `POST /v0/bulk-actions/{id}/undo`.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigSetApply):

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

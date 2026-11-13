from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.download_link import DownloadLink
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    dump: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/game-servers/{id}/crash-dumps/{dump}/link".format(
            id=quote(str(id), safe=""),
            dump=quote(str(dump), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DownloadLink | Problem:
    if response.status_code == 200:
        response_200 = DownloadLink.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DownloadLink | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    dump: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[DownloadLink | Problem]:
    """Make a download link for a crash dump

     A link that downloads this one crash dump, opened, once, within 2 minutes, from the same browser and
    address that asked for it: the answer sets a cookie (`HttpOnly`, `Secure`, `SameSite=Strict`, path
    `/v0/crash-dump-downloads/`, 2 minutes) holding a random secret, and the link works only with it.
    Owners and admins with the crash-dump permission only, from the panel (`403 missing_scope`
    otherwise); a suspended studio makes none (`403 studio_suspended`). The audit log records who asked,
    and again the download. Call again for a fresh link.

    Args:
        id (str): Game server ID.
        dump (str): Collected file ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadLink | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        dump=dump,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    dump: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> DownloadLink | Problem | None:
    """Make a download link for a crash dump

     A link that downloads this one crash dump, opened, once, within 2 minutes, from the same browser and
    address that asked for it: the answer sets a cookie (`HttpOnly`, `Secure`, `SameSite=Strict`, path
    `/v0/crash-dump-downloads/`, 2 minutes) holding a random secret, and the link works only with it.
    Owners and admins with the crash-dump permission only, from the panel (`403 missing_scope`
    otherwise); a suspended studio makes none (`403 studio_suspended`). The audit log records who asked,
    and again the download. Call again for a fresh link.

    Args:
        id (str): Game server ID.
        dump (str): Collected file ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadLink | Problem
    """

    return sync_detailed(
        id=id,
        dump=dump,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    dump: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[DownloadLink | Problem]:
    """Make a download link for a crash dump

     A link that downloads this one crash dump, opened, once, within 2 minutes, from the same browser and
    address that asked for it: the answer sets a cookie (`HttpOnly`, `Secure`, `SameSite=Strict`, path
    `/v0/crash-dump-downloads/`, 2 minutes) holding a random secret, and the link works only with it.
    Owners and admins with the crash-dump permission only, from the panel (`403 missing_scope`
    otherwise); a suspended studio makes none (`403 studio_suspended`). The audit log records who asked,
    and again the download. Call again for a fresh link.

    Args:
        id (str): Game server ID.
        dump (str): Collected file ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadLink | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        dump=dump,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    dump: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> DownloadLink | Problem | None:
    """Make a download link for a crash dump

     A link that downloads this one crash dump, opened, once, within 2 minutes, from the same browser and
    address that asked for it: the answer sets a cookie (`HttpOnly`, `Secure`, `SameSite=Strict`, path
    `/v0/crash-dump-downloads/`, 2 minutes) holding a random secret, and the link works only with it.
    Owners and admins with the crash-dump permission only, from the panel (`403 missing_scope`
    otherwise); a suspended studio makes none (`403 studio_suspended`). The audit log records who asked,
    and again the download. Call again for a fresh link.

    Args:
        id (str): Game server ID.
        dump (str): Collected file ID.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadLink | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            dump=dump,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed

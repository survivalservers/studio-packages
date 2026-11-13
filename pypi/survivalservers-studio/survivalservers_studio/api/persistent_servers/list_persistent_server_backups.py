import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_kind import BackupKind
from ...models.backup_list import BackupList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    kind: BackupKind | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/persistent-servers/{id}/backups".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupList | Problem:
    if response.status_code == 200:
        response_200 = BackupList.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BackupList | Problem]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    kind: BackupKind | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[BackupList | Problem]:
    """List backups

     Newest first. `before` finds the backup a rollback to that moment would go to.

    Args:
        id (str): Persistent server ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        kind (BackupKind | Unset): `scheduled` is taken on the server's schedule, `stop` at each
            stop, `manual` when asked. `continuous` is copied within seconds of each game save; the
            newest 3 are kept, apart from your other backups, and a persistent server that loses its
            machine starts again from the newest. `before_restore` is how it was just before a restore
            or rollback, which an undo goes back to. `before_update` is the backup taken at the stop
            before a new version started: the old version's last save, kept 30 days like
            `before_restore`. `imported` is a save you uploaded. `recovered` holds newer saves found
            on a machine that came back after its persistent server moved.
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        kind=kind,
        before=before,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    kind: BackupKind | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> BackupList | Problem | None:
    """List backups

     Newest first. `before` finds the backup a rollback to that moment would go to.

    Args:
        id (str): Persistent server ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        kind (BackupKind | Unset): `scheduled` is taken on the server's schedule, `stop` at each
            stop, `manual` when asked. `continuous` is copied within seconds of each game save; the
            newest 3 are kept, apart from your other backups, and a persistent server that loses its
            machine starts again from the newest. `before_restore` is how it was just before a restore
            or rollback, which an undo goes back to. `before_update` is the backup taken at the stop
            before a new version started: the old version's last save, kept 30 days like
            `before_restore`. `imported` is a save you uploaded. `recovered` holds newer saves found
            on a machine that came back after its persistent server moved.
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupList | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        kind=kind,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    kind: BackupKind | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> Response[BackupList | Problem]:
    """List backups

     Newest first. `before` finds the backup a rollback to that moment would go to.

    Args:
        id (str): Persistent server ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        kind (BackupKind | Unset): `scheduled` is taken on the server's schedule, `stop` at each
            stop, `manual` when asked. `continuous` is copied within seconds of each game save; the
            newest 3 are kept, apart from your other backups, and a persistent server that loses its
            machine starts again from the newest. `before_restore` is how it was just before a restore
            or rollback, which an undo goes back to. `before_update` is the backup taken at the stop
            before a new version started: the old version's last save, kept 30 days like
            `before_restore`. `imported` is a save you uploaded. `recovered` holds newer saves found
            on a machine that came back after its persistent server moved.
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupList | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        kind=kind,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    kind: BackupKind | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
) -> BackupList | Problem | None:
    """List backups

     Newest first. `before` finds the backup a rollback to that moment would go to.

    Args:
        id (str): Persistent server ID.
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        kind (BackupKind | Unset): `scheduled` is taken on the server's schedule, `stop` at each
            stop, `manual` when asked. `continuous` is copied within seconds of each game save; the
            newest 3 are kept, apart from your other backups, and a persistent server that loses its
            machine starts again from the newest. `before_restore` is how it was just before a restore
            or rollback, which an undo goes back to. `before_update` is the backup taken at the stop
            before a new version started: the old version's last save, kept 30 days like
            `before_restore`. `imported` is a save you uploaded. `recovered` holds newer saves found
            on a machine that came back after its persistent server moved.
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupList | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            kind=kind,
            before=before,
            after=after,
        )
    ).parsed

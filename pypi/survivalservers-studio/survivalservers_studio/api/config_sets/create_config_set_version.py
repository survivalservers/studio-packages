from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.config_content import ConfigContent
from ...models.config_set_version import ConfigSetVersion
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: ConfigContent,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/config-sets/{id}/versions".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigSetVersion | Problem:
    if response.status_code == 201:
        response_201 = ConfigSetVersion.from_dict(response.json())

        return response_201

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
) -> Response[ConfigSetVersion | Problem]:
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
    body: ConfigContent,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConfigSetVersion | Problem]:
    """Save a new version

     The full settings of the new version (not a patch). Versions never change; persistent servers stay
    on theirs until one is applied.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigContent): The settings of one version. The set's `env` replaces a persistent
            server's own value of the same name (a change across all your servers reaches every
            persistent server); the set's `args` come after the version's and the persistent server's
            own; `files` are written into the persistent server's folder before every run, replacing
            what is there. Up to 32 files and 512 KiB in all. `values` set the settings in the game
            profile by ID, changing only those keys in the game's own files, and win over a server's
            own values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSetVersion | Problem]
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
    body: ConfigContent,
    idempotency_key: str | Unset = UNSET,
) -> ConfigSetVersion | Problem | None:
    """Save a new version

     The full settings of the new version (not a patch). Versions never change; persistent servers stay
    on theirs until one is applied.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigContent): The settings of one version. The set's `env` replaces a persistent
            server's own value of the same name (a change across all your servers reaches every
            persistent server); the set's `args` come after the version's and the persistent server's
            own; `files` are written into the persistent server's folder before every run, replacing
            what is there. Up to 32 files and 512 KiB in all. `values` set the settings in the game
            profile by ID, changing only those keys in the game's own files, and win over a server's
            own values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSetVersion | Problem
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
    body: ConfigContent,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConfigSetVersion | Problem]:
    """Save a new version

     The full settings of the new version (not a patch). Versions never change; persistent servers stay
    on theirs until one is applied.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigContent): The settings of one version. The set's `env` replaces a persistent
            server's own value of the same name (a change across all your servers reaches every
            persistent server); the set's `args` come after the version's and the persistent server's
            own; `files` are written into the persistent server's folder before every run, replacing
            what is there. Up to 32 files and 512 KiB in all. `values` set the settings in the game
            profile by ID, changing only those keys in the game's own files, and win over a server's
            own values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigSetVersion | Problem]
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
    body: ConfigContent,
    idempotency_key: str | Unset = UNSET,
) -> ConfigSetVersion | Problem | None:
    """Save a new version

     The full settings of the new version (not a patch). Versions never change; persistent servers stay
    on theirs until one is applied.

    Args:
        id (str): Config set ID.
        idempotency_key (str | Unset):
        body (ConfigContent): The settings of one version. The set's `env` replaces a persistent
            server's own value of the same name (a change across all your servers reaches every
            persistent server); the set's `args` come after the version's and the persistent server's
            own; `files` are written into the persistent server's folder before every run, replacing
            what is there. Up to 32 files and 512 KiB in all. `values` set the settings in the game
            profile by ID, changing only those keys in the game's own files, and win over a server's
            own values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigSetVersion | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

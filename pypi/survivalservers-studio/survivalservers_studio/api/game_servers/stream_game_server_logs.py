from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    source: str | Unset = "console",
    tail: int | Unset = UNSET,
    follow: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["source"] = source

    params["tail"] = tail

    params["follow"] = follow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/logs/stream".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | str:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | str]:
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
    source: str | Unset = "console",
    tail: int | Unset = UNSET,
    follow: bool | Unset = False,
) -> Response[Problem | str]:
    """Read or follow a log

     Plain text, streamed. `follow=true` keeps the stream open while the server runs.

    Args:
        id (str): Game server ID.
        source (str | Unset):  Default: 'console'.
        tail (int | Unset):
        follow (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        id=id,
        source=source,
        tail=tail,
        follow=follow,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    source: str | Unset = "console",
    tail: int | Unset = UNSET,
    follow: bool | Unset = False,
) -> Problem | str | None:
    """Read or follow a log

     Plain text, streamed. `follow=true` keeps the stream open while the server runs.

    Args:
        id (str): Game server ID.
        source (str | Unset):  Default: 'console'.
        tail (int | Unset):
        follow (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return sync_detailed(
        id=id,
        client=client,
        source=source,
        tail=tail,
        follow=follow,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    source: str | Unset = "console",
    tail: int | Unset = UNSET,
    follow: bool | Unset = False,
) -> Response[Problem | str]:
    """Read or follow a log

     Plain text, streamed. `follow=true` keeps the stream open while the server runs.

    Args:
        id (str): Game server ID.
        source (str | Unset):  Default: 'console'.
        tail (int | Unset):
        follow (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | str]
    """

    kwargs = _get_kwargs(
        id=id,
        source=source,
        tail=tail,
        follow=follow,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    source: str | Unset = "console",
    tail: int | Unset = UNSET,
    follow: bool | Unset = False,
) -> Problem | str | None:
    """Read or follow a log

     Plain text, streamed. `follow=true` keeps the stream open while the server runs.

    Args:
        id (str): Game server ID.
        source (str | Unset):  Default: 'console'.
        tail (int | Unset):
        follow (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            source=source,
            tail=tail,
            follow=follow,
        )
    ).parsed

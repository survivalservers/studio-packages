from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.config_diff import ConfigDiff
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    from_: int,
    to: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/config-sets/{id}/diff".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigDiff | Problem:
    if response.status_code == 200:
        response_200 = ConfigDiff.from_dict(response.json())

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
) -> Response[ConfigDiff | Problem]:
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
    from_: int,
    to: int | Unset = UNSET,
) -> Response[ConfigDiff | Problem]:
    """Compare two versions

     Environment values added, changed and removed (secret ones without their values), the arguments
    before and after, and a line diff of each changed file.

    Args:
        id (str): Config set ID.
        from_ (int):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigDiff | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int | Unset = UNSET,
) -> ConfigDiff | Problem | None:
    """Compare two versions

     Environment values added, changed and removed (secret ones without their values), the arguments
    before and after, and a line diff of each changed file.

    Args:
        id (str): Config set ID.
        from_ (int):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigDiff | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int | Unset = UNSET,
) -> Response[ConfigDiff | Problem]:
    """Compare two versions

     Environment values added, changed and removed (secret ones without their values), the arguments
    before and after, and a line diff of each changed file.

    Args:
        id (str): Config set ID.
        from_ (int):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigDiff | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int | Unset = UNSET,
) -> ConfigDiff | Problem | None:
    """Compare two versions

     Environment values added, changed and removed (secret ones without their values), the arguments
    before and after, and a line diff of each changed file.

    Args:
        id (str): Config set ID.
        from_ (int):
        to (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigDiff | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed

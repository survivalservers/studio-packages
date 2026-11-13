from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.connect_request import ConnectRequest
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    handle: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/connect/{handle}".format(
            handle=quote(str(handle), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectRequest | Problem:
    if response.status_code == 200:
        response_200 = ConnectRequest.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectRequest | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConnectRequest | Problem]:
    """Get a sign-in waiting for approval

     Which tool asks to connect, and where the sign-in goes back to, for the approval page. The request
    is the one-time handle the sign-in server put in the panel's address; it works for 10 minutes and
    until it is approved or refused. Needs no sign-in, so the sign-in page can name the tool.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRequest | Problem]
    """

    kwargs = _get_kwargs(
        handle=handle,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectRequest | Problem | None:
    """Get a sign-in waiting for approval

     Which tool asks to connect, and where the sign-in goes back to, for the approval page. The request
    is the one-time handle the sign-in server put in the panel's address; it works for 10 minutes and
    until it is approved or refused. Needs no sign-in, so the sign-in page can name the tool.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRequest | Problem
    """

    return sync_detailed(
        handle=handle,
        client=client,
    ).parsed


async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ConnectRequest | Problem]:
    """Get a sign-in waiting for approval

     Which tool asks to connect, and where the sign-in goes back to, for the approval page. The request
    is the one-time handle the sign-in server put in the panel's address; it works for 10 minutes and
    until it is approved or refused. Needs no sign-in, so the sign-in page can name the tool.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRequest | Problem]
    """

    kwargs = _get_kwargs(
        handle=handle,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    handle: str,
    *,
    client: AuthenticatedClient | Client,
) -> ConnectRequest | Problem | None:
    """Get a sign-in waiting for approval

     Which tool asks to connect, and where the sign-in goes back to, for the approval page. The request
    is the one-time handle the sign-in server put in the panel's address; it works for 10 minutes and
    until it is approved or refused. Needs no sign-in, so the sign-in page can name the tool.

    Args:
        handle (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRequest | Problem
    """

    return (
        await asyncio_detailed(
            handle=handle,
            client=client,
        )
    ).parsed

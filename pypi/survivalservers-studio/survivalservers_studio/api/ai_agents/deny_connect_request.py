from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.connect_decision import ConnectDecision
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    handle: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/connect/{handle}/deny".format(
            handle=quote(str(handle), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectDecision | Problem:
    if response.status_code == 200:
        response_200 = ConnectDecision.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectDecision | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    handle: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConnectDecision | Problem]:
    """Refuse a tool's sign-in

     The tool is told the member said no (`error=access_denied`).

    Args:
        handle (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectDecision | Problem]
    """

    kwargs = _get_kwargs(
        handle=handle,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    handle: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> ConnectDecision | Problem | None:
    """Refuse a tool's sign-in

     The tool is told the member said no (`error=access_denied`).

    Args:
        handle (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectDecision | Problem
    """

    return sync_detailed(
        handle=handle,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    handle: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[ConnectDecision | Problem]:
    """Refuse a tool's sign-in

     The tool is told the member said no (`error=access_denied`).

    Args:
        handle (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectDecision | Problem]
    """

    kwargs = _get_kwargs(
        handle=handle,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    handle: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> ConnectDecision | Problem | None:
    """Refuse a tool's sign-in

     The tool is told the member said no (`error=access_denied`).

    Args:
        handle (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectDecision | Problem
    """

    return (
        await asyncio_detailed(
            handle=handle,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.terms import Terms
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/terms",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Terms:
    if response.status_code == 200:
        response_200 = Terms.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | Terms]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Problem | Terms]:
    """Get the terms in effect

     The version of the terms in effect and the addresses of its pages: the Terms of Service, the
    documents they name and the Privacy Notice. Needs no key and no sign-in, so the sign-up page can
    show the box to tick. While no version is in effect, `version` is `null` and nothing asks for one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Terms]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Problem | Terms | None:
    """Get the terms in effect

     The version of the terms in effect and the addresses of its pages: the Terms of Service, the
    documents they name and the Privacy Notice. Needs no key and no sign-in, so the sign-up page can
    show the box to tick. While no version is in effect, `version` is `null` and nothing asks for one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Terms
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Problem | Terms]:
    """Get the terms in effect

     The version of the terms in effect and the addresses of its pages: the Terms of Service, the
    documents they name and the Privacy Notice. Needs no key and no sign-in, so the sign-up page can
    show the box to tick. While no version is in effect, `version` is `null` and nothing asks for one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Terms]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Problem | Terms | None:
    """Get the terms in effect

     The version of the terms in effect and the addresses of its pages: the Terms of Service, the
    documents they name and the Privacy Notice. Needs no key and no sign-in, so the sign-up page can
    show the box to tick. While no version is in effect, `version` is `null` and nothing asks for one.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Terms
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

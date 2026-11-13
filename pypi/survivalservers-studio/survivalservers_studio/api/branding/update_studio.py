from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.studio import Studio
from ...models.studio_update import StudioUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StudioUpdate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v0/studio",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Studio:
    if response.status_code == 200:
        response_200 = Studio.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | Studio]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StudioUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Studio]:
    """Update your studio

     Renames the studio, sets or clears (`null`) the color the panel uses for the studio's highlights and
    the first line of its charts, sets its time zone (for the panel and its emails; the API's times stay
    in UTC), or sets its notice contacts or its tax registration number (Owners only, from the panel).
    The short name (`slug`) never changes, so addresses and scripts that use it keep working. Owners and
    admins only (`studio:write`).

    Args:
        idempotency_key (str | Unset):
        body (StudioUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Studio]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: StudioUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Studio | None:
    """Update your studio

     Renames the studio, sets or clears (`null`) the color the panel uses for the studio's highlights and
    the first line of its charts, sets its time zone (for the panel and its emails; the API's times stay
    in UTC), or sets its notice contacts or its tax registration number (Owners only, from the panel).
    The short name (`slug`) never changes, so addresses and scripts that use it keep working. Owners and
    admins only (`studio:write`).

    Args:
        idempotency_key (str | Unset):
        body (StudioUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Studio
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StudioUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Studio]:
    """Update your studio

     Renames the studio, sets or clears (`null`) the color the panel uses for the studio's highlights and
    the first line of its charts, sets its time zone (for the panel and its emails; the API's times stay
    in UTC), or sets its notice contacts or its tax registration number (Owners only, from the panel).
    The short name (`slug`) never changes, so addresses and scripts that use it keep working. Owners and
    admins only (`studio:write`).

    Args:
        idempotency_key (str | Unset):
        body (StudioUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Studio]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StudioUpdate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Studio | None:
    """Update your studio

     Renames the studio, sets or clears (`null`) the color the panel uses for the studio's highlights and
    the first line of its charts, sets its time zone (for the panel and its emails; the API's times stay
    in UTC), or sets its notice contacts or its tax registration number (Owners only, from the panel).
    The short name (`slug`) never changes, so addresses and scripts that use it keep working. Owners and
    admins only (`studio:write`).

    Args:
        idempotency_key (str | Unset):
        body (StudioUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Studio
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

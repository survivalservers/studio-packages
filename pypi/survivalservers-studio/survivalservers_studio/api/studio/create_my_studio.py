from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.my_studio_create import MyStudioCreate
from ...models.problem import Problem
from ...models.studio import Studio
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MyStudioCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/me/studio",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Studio:
    if response.status_code == 201:
        response_201 = Studio.from_dict(response.json())

        return response_201

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

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
    body: MyStudioCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Studio]:
    """Make your first studio

     For a signed-in person who belongs to no studio yet: makes one with them as its owner, named after
    them (for example "Riley Chen’s studio"; rename it with `PATCH /v0/studio`), on the same terms as
    `POST /v0/studios` (the free vCPU-hours; a card before the first start). It is made once: a person
    who already belongs to a studio gets `409 invalid_state` and no new one, however many calls arrive
    together. A person with an invitation waiting (`invitations` in `GET /v0/me`) also gets `409
    invalid_state`, so nobody is given an empty studio instead of the one that invited them, unless
    `ignore_invitations` says they chose their own.

    Args:
        idempotency_key (str | Unset):
        body (MyStudioCreate):

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
    body: MyStudioCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Studio | None:
    """Make your first studio

     For a signed-in person who belongs to no studio yet: makes one with them as its owner, named after
    them (for example "Riley Chen’s studio"; rename it with `PATCH /v0/studio`), on the same terms as
    `POST /v0/studios` (the free vCPU-hours; a card before the first start). It is made once: a person
    who already belongs to a studio gets `409 invalid_state` and no new one, however many calls arrive
    together. A person with an invitation waiting (`invitations` in `GET /v0/me`) also gets `409
    invalid_state`, so nobody is given an empty studio instead of the one that invited them, unless
    `ignore_invitations` says they chose their own.

    Args:
        idempotency_key (str | Unset):
        body (MyStudioCreate):

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
    body: MyStudioCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[Problem | Studio]:
    """Make your first studio

     For a signed-in person who belongs to no studio yet: makes one with them as its owner, named after
    them (for example "Riley Chen’s studio"; rename it with `PATCH /v0/studio`), on the same terms as
    `POST /v0/studios` (the free vCPU-hours; a card before the first start). It is made once: a person
    who already belongs to a studio gets `409 invalid_state` and no new one, however many calls arrive
    together. A person with an invitation waiting (`invitations` in `GET /v0/me`) also gets `409
    invalid_state`, so nobody is given an empty studio instead of the one that invited them, unless
    `ignore_invitations` says they chose their own.

    Args:
        idempotency_key (str | Unset):
        body (MyStudioCreate):

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
    body: MyStudioCreate,
    idempotency_key: str | Unset = UNSET,
) -> Problem | Studio | None:
    """Make your first studio

     For a signed-in person who belongs to no studio yet: makes one with them as its owner, named after
    them (for example "Riley Chen’s studio"; rename it with `PATCH /v0/studio`), on the same terms as
    `POST /v0/studios` (the free vCPU-hours; a card before the first start). It is made once: a person
    who already belongs to a studio gets `409 invalid_state` and no new one, however many calls arrive
    together. A person with an invitation waiting (`invitations` in `GET /v0/me`) also gets `409
    invalid_state`, so nobody is given an empty studio instead of the one that invited them, unless
    `ignore_invitations` says they chose their own.

    Args:
        idempotency_key (str | Unset):
        body (MyStudioCreate):

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

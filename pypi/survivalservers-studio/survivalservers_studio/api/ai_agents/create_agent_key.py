from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_key_create import AgentKeyCreate
from ...models.agent_with_key import AgentWithKey
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AgentKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/agents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentWithKey | Problem:
    if response.status_code == 201:
        response_201 = AgentWithKey.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentWithKey | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[AgentWithKey | Problem]:
    """Create an agent key

     An API key for an AI agent with no person present, with the same permissions, time limit and
    spending cap as a connected tool. It acts for the member who makes it, can never do more than their
    role allows, and its actions are marked "by AI" in the audit log. `key` is in this reply only.

    Args:
        idempotency_key (str | Unset):
        body (AgentKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentWithKey | Problem]
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
    body: AgentKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> AgentWithKey | Problem | None:
    """Create an agent key

     An API key for an AI agent with no person present, with the same permissions, time limit and
    spending cap as a connected tool. It acts for the member who makes it, can never do more than their
    role allows, and its actions are marked "by AI" in the audit log. `key` is in this reply only.

    Args:
        idempotency_key (str | Unset):
        body (AgentKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentWithKey | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[AgentWithKey | Problem]:
    """Create an agent key

     An API key for an AI agent with no person present, with the same permissions, time limit and
    spending cap as a connected tool. It acts for the member who makes it, can never do more than their
    role allows, and its actions are marked "by AI" in the audit log. `key` is in this reply only.

    Args:
        idempotency_key (str | Unset):
        body (AgentKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentWithKey | Problem]
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
    body: AgentKeyCreate,
    idempotency_key: str | Unset = UNSET,
) -> AgentWithKey | Problem | None:
    """Create an agent key

     An API key for an AI agent with no person present, with the same permissions, time limit and
    spending cap as a connected tool. It acts for the member who makes it, can never do more than their
    role allows, and its actions are marked "by AI" in the audit log. `key` is in this reply only.

    Args:
        idempotency_key (str | Unset):
        body (AgentKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentWithKey | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

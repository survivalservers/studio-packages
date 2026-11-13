from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_list import AuditList
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    agent: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["agent"] = agent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/agent-actions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditList | Problem:
    if response.status_code == 200:
        response_200 = AuditList.from_dict(response.json())

        return response_200

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditList | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    agent: str | Unset = UNSET,
) -> Response[AuditList | Problem]:
    """List recent actions by AI

     The audit log's entries made by AI agents, newest first, each with the agent and the person it acted
    for. A member without `keys:write` sees the actions of the agents they connected.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        agent (str | Unset): AI agent ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        agent=agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    agent: str | Unset = UNSET,
) -> AuditList | Problem | None:
    """List recent actions by AI

     The audit log's entries made by AI agents, newest first, each with the agent and the person it acted
    for. A member without `keys:write` sees the actions of the agents they connected.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        agent (str | Unset): AI agent ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditList | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        agent=agent,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    agent: str | Unset = UNSET,
) -> Response[AuditList | Problem]:
    """List recent actions by AI

     The audit log's entries made by AI agents, newest first, each with the agent and the person it acted
    for. A member without `keys:write` sees the actions of the agents they connected.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        agent (str | Unset): AI agent ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditList | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        agent=agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    agent: str | Unset = UNSET,
) -> AuditList | Problem | None:
    """List recent actions by AI

     The audit log's entries made by AI agents, newest first, each with the agent and the person it acted
    for. A member without `keys:write` sees the actions of the agents they connected.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        agent (str | Unset): AI agent ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditList | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            agent=agent,
        )
    ).parsed

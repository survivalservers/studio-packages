from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.machine_create import MachineCreate
from ...models.machine_with_enrollment import MachineWithEnrollment
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MachineCreate,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/machines",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MachineWithEnrollment | Problem:
    if response.status_code == 201:
        response_201 = MachineWithEnrollment.from_dict(response.json())

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
) -> Response[MachineWithEnrollment | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MachineCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[MachineWithEnrollment | Problem]:
    """Add one of your own machines

     Makes the machine's record and a one-time machine setup token, valid 24 hours and in this reply
    only. Install the machine agent on the machine and enroll it with the token; from then on it takes
    only your studio's game servers, ahead of our shared machines in its region. It bills
    `own_machine_cpu_month` for each of its usable vCPUs from enrollment until you remove it, spread
    over the hours it was enrolled; game servers on it bill nothing per hour. `region` is the region it
    counts as for placement and pings: pick the nearest one.

    Args:
        idempotency_key (str | Unset):
        body (MachineCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineWithEnrollment | Problem]
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
    body: MachineCreate,
    idempotency_key: str | Unset = UNSET,
) -> MachineWithEnrollment | Problem | None:
    """Add one of your own machines

     Makes the machine's record and a one-time machine setup token, valid 24 hours and in this reply
    only. Install the machine agent on the machine and enroll it with the token; from then on it takes
    only your studio's game servers, ahead of our shared machines in its region. It bills
    `own_machine_cpu_month` for each of its usable vCPUs from enrollment until you remove it, spread
    over the hours it was enrolled; game servers on it bill nothing per hour. `region` is the region it
    counts as for placement and pings: pick the nearest one.

    Args:
        idempotency_key (str | Unset):
        body (MachineCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineWithEnrollment | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MachineCreate,
    idempotency_key: str | Unset = UNSET,
) -> Response[MachineWithEnrollment | Problem]:
    """Add one of your own machines

     Makes the machine's record and a one-time machine setup token, valid 24 hours and in this reply
    only. Install the machine agent on the machine and enroll it with the token; from then on it takes
    only your studio's game servers, ahead of our shared machines in its region. It bills
    `own_machine_cpu_month` for each of its usable vCPUs from enrollment until you remove it, spread
    over the hours it was enrolled; game servers on it bill nothing per hour. `region` is the region it
    counts as for placement and pings: pick the nearest one.

    Args:
        idempotency_key (str | Unset):
        body (MachineCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineWithEnrollment | Problem]
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
    body: MachineCreate,
    idempotency_key: str | Unset = UNSET,
) -> MachineWithEnrollment | Problem | None:
    """Add one of your own machines

     Makes the machine's record and a one-time machine setup token, valid 24 hours and in this reply
    only. Install the machine agent on the machine and enroll it with the token; from then on it takes
    only your studio's game servers, ahead of our shared machines in its region. It bills
    `own_machine_cpu_month` for each of its usable vCPUs from enrollment until you remove it, spread
    over the hours it was enrolled; game servers on it bill nothing per hour. `region` is the region it
    counts as for placement and pings: pick the nearest one.

    Args:
        idempotency_key (str | Unset):
        body (MachineCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineWithEnrollment | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed

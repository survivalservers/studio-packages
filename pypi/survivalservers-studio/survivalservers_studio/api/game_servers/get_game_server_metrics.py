import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metric_step import MetricStep
from ...models.metrics import Metrics
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: MetricStep | Unset = MetricStep.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_step: str | Unset = UNSET
    if not isinstance(step, Unset):
        json_step = step.value

    params["step"] = json_step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/game-servers/{id}/metrics".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Metrics | Problem:
    if response.status_code == 200:
        response_200 = Metrics.from_dict(response.json())

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
) -> Response[Metrics | Problem]:
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: MetricStep | Unset = MetricStep.VALUE_1,
) -> Response[Metrics | Problem]:
    """Get metrics

     CPU use (relative to the game server's own vCPUs), committed memory, network and, when the server
    reports frame times, tick p99. `step=1s` for the last 48 hours; `10s` and the longer steps for 90
    days, each point the average of its step. At most 20,000 points a series: a week at `1m`, 90 days at
    `15m`.

    Args:
        id (str): Game server ID.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (MetricStep | Unset): A point's length; every point is the average over its step,
            starting on a UTC step boundary. Default: MetricStep.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Metrics | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        step=step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: MetricStep | Unset = MetricStep.VALUE_1,
) -> Metrics | Problem | None:
    """Get metrics

     CPU use (relative to the game server's own vCPUs), committed memory, network and, when the server
    reports frame times, tick p99. `step=1s` for the last 48 hours; `10s` and the longer steps for 90
    days, each point the average of its step. At most 20,000 points a series: a week at `1m`, 90 days at
    `15m`.

    Args:
        id (str): Game server ID.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (MetricStep | Unset): A point's length; every point is the average over its step,
            starting on a UTC step boundary. Default: MetricStep.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Metrics | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
        step=step,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: MetricStep | Unset = MetricStep.VALUE_1,
) -> Response[Metrics | Problem]:
    """Get metrics

     CPU use (relative to the game server's own vCPUs), committed memory, network and, when the server
    reports frame times, tick p99. `step=1s` for the last 48 hours; `10s` and the longer steps for 90
    days, each point the average of its step. At most 20,000 points a series: a week at `1m`, 90 days at
    `15m`.

    Args:
        id (str): Game server ID.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (MetricStep | Unset): A point's length; every point is the average over its step,
            starting on a UTC step boundary. Default: MetricStep.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Metrics | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        step=step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    step: MetricStep | Unset = MetricStep.VALUE_1,
) -> Metrics | Problem | None:
    """Get metrics

     CPU use (relative to the game server's own vCPUs), committed memory, network and, when the server
    reports frame times, tick p99. `step=1s` for the last 48 hours; `10s` and the longer steps for 90
    days, each point the average of its step. At most 20,000 points a series: a week at `1m`, 90 days at
    `15m`.

    Args:
        id (str): Game server ID.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        step (MetricStep | Unset): A point's length; every point is the average over its step,
            starting on a UTC step boundary. Default: MetricStep.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Metrics | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
            step=step,
        )
    ).parsed

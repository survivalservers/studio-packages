from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_usage_granularity import GetUsageGranularity
from ...models.problem import Problem
from ...models.usage_group_by import UsageGroupBy
from ...models.usage_report import UsageReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    group_by: list[UsageGroupBy] | Unset = UNSET,
    granularity: GetUsageGranularity | Unset = GetUsageGranularity.DAY,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_group_by: list[str] | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = []
        for group_by_item_data in group_by:
            group_by_item = group_by_item_data.value
            json_group_by.append(group_by_item)

    params["group_by"] = json_group_by

    json_granularity: str | Unset = UNSET
    if not isinstance(granularity, Unset):
        json_granularity = granularity.value

    params["granularity"] = json_granularity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UsageReport:
    if response.status_code == 200:
        response_200 = UsageReport.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UsageReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    group_by: list[UsageGroupBy] | Unset = UNSET,
    granularity: GetUsageGranularity | Unset = GetUsageGranularity.DAY,
) -> Response[Problem | UsageReport]:
    """Get usage and cost

     Counted per second with no minimum, priced at the studio's locked price book. Exact to the cent once
    a month closes; the current month is live and estimated. Rows are UTC hours, days, weeks (from
    Monday), months or years; `from` and `to` are rounded down to whole UTC hours. One report covers at
    most 62 days by hour, 1,830 days by day, and 3,660 days by week, month or year. For a key limited to
    some apps the whole report, totals included, is worked out over those apps alone: the month's free
    CPU-hours and free backup storage go to their usage, and the studio's credits, its own machines and
    reservations are left out.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        group_by (list[UsageGroupBy] | Unset):
        granularity (GetUsageGranularity | Unset):  Default: GetUsageGranularity.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UsageReport]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        group_by=group_by,
        granularity=granularity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    group_by: list[UsageGroupBy] | Unset = UNSET,
    granularity: GetUsageGranularity | Unset = GetUsageGranularity.DAY,
) -> Problem | UsageReport | None:
    """Get usage and cost

     Counted per second with no minimum, priced at the studio's locked price book. Exact to the cent once
    a month closes; the current month is live and estimated. Rows are UTC hours, days, weeks (from
    Monday), months or years; `from` and `to` are rounded down to whole UTC hours. One report covers at
    most 62 days by hour, 1,830 days by day, and 3,660 days by week, month or year. For a key limited to
    some apps the whole report, totals included, is worked out over those apps alone: the month's free
    CPU-hours and free backup storage go to their usage, and the studio's credits, its own machines and
    reservations are left out.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        group_by (list[UsageGroupBy] | Unset):
        granularity (GetUsageGranularity | Unset):  Default: GetUsageGranularity.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UsageReport
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        group_by=group_by,
        granularity=granularity,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    group_by: list[UsageGroupBy] | Unset = UNSET,
    granularity: GetUsageGranularity | Unset = GetUsageGranularity.DAY,
) -> Response[Problem | UsageReport]:
    """Get usage and cost

     Counted per second with no minimum, priced at the studio's locked price book. Exact to the cent once
    a month closes; the current month is live and estimated. Rows are UTC hours, days, weeks (from
    Monday), months or years; `from` and `to` are rounded down to whole UTC hours. One report covers at
    most 62 days by hour, 1,830 days by day, and 3,660 days by week, month or year. For a key limited to
    some apps the whole report, totals included, is worked out over those apps alone: the month's free
    CPU-hours and free backup storage go to their usage, and the studio's credits, its own machines and
    reservations are left out.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        group_by (list[UsageGroupBy] | Unset):
        granularity (GetUsageGranularity | Unset):  Default: GetUsageGranularity.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UsageReport]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        group_by=group_by,
        granularity=granularity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    group_by: list[UsageGroupBy] | Unset = UNSET,
    granularity: GetUsageGranularity | Unset = GetUsageGranularity.DAY,
) -> Problem | UsageReport | None:
    """Get usage and cost

     Counted per second with no minimum, priced at the studio's locked price book. Exact to the cent once
    a month closes; the current month is live and estimated. Rows are UTC hours, days, weeks (from
    Monday), months or years; `from` and `to` are rounded down to whole UTC hours. One report covers at
    most 62 days by hour, 1,830 days by day, and 3,660 days by week, month or year. For a key limited to
    some apps the whole report, totals included, is worked out over those apps alone: the month's free
    CPU-hours and free backup storage go to their usage, and the studio's credits, its own machines and
    reservations are left out.

    Args:
        from_ (str | Unset):
        to (str | Unset):
        group_by (list[UsageGroupBy] | Unset):
        granularity (GetUsageGranularity | Unset):  Default: GetUsageGranularity.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UsageReport
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            group_by=group_by,
            granularity=granularity,
        )
    ).parsed

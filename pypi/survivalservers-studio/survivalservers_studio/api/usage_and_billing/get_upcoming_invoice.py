from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.upcoming_invoice import UpcomingInvoice
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/billing/upcoming-invoice",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | UpcomingInvoice:
    if response.status_code == 200:
        response_200 = UpcomingInvoice.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | UpcomingInvoice]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Problem | UpcomingInvoice]:
    """See the next invoice so far

     What your next invoice would say if its month closed now: that month's usage so far, plus any usage
    from an
    earlier month that reached us after that month's invoice was made. Those lines name the month they
    came from
    and use that month's prices, its unused free vCPU-hours and its uptime credit, so they cost what
    they would have
    cost on time. Worked out at most once a minute per studio (`as_of` says when). Reading it bills
    nothing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpcomingInvoice]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Problem | UpcomingInvoice | None:
    """See the next invoice so far

     What your next invoice would say if its month closed now: that month's usage so far, plus any usage
    from an
    earlier month that reached us after that month's invoice was made. Those lines name the month they
    came from
    and use that month's prices, its unused free vCPU-hours and its uptime credit, so they cost what
    they would have
    cost on time. Worked out at most once a minute per studio (`as_of` says when). Reading it bills
    nothing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpcomingInvoice
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Problem | UpcomingInvoice]:
    """See the next invoice so far

     What your next invoice would say if its month closed now: that month's usage so far, plus any usage
    from an
    earlier month that reached us after that month's invoice was made. Those lines name the month they
    came from
    and use that month's prices, its unused free vCPU-hours and its uptime credit, so they cost what
    they would have
    cost on time. Worked out at most once a minute per studio (`as_of` says when). Reading it bills
    nothing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | UpcomingInvoice]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Problem | UpcomingInvoice | None:
    """See the next invoice so far

     What your next invoice would say if its month closed now: that month's usage so far, plus any usage
    from an
    earlier month that reached us after that month's invoice was made. Those lines name the month they
    came from
    and use that month's prices, its unused free vCPU-hours and its uptime credit, so they cost what
    they would have
    cost on time. Worked out at most once a minute per studio (`as_of` says when). Reading it bills
    nothing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | UpcomingInvoice
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

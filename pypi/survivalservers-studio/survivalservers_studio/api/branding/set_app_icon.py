from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.app import App
from ...models.problem import Problem
from ...types import File, Response


def _get_kwargs(
    app: str,
    *,
    body: File,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v0/apps/{app}/icon".format(
            app=quote(str(app), safe=""),
        ),
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> App | Problem:
    if response.status_code == 200:
        response_200 = App.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = Problem.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    response_default = Problem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[App | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    body: File,
) -> Response[App | Problem]:
    """Set an app's icon

     Send the picture itself as the body (`Content-Type: application/octet-stream`, or the picture's own
    type):
    PNG, JPEG or WebP, up to 1 MiB, at least 32 and at most 2048 pixels on each side. The type is read
    from the
    bytes, never from a file name; SVG, GIF, animated WebP and anything else are refused (`422
    unsupported_image`), and so is a body whose `Content-Type` names another picture type than its bytes
    are.
    We decode it, take the middle square of a picture that is not square, and make new WebP files of 64,
    128
    and 256 pixels with no metadata, so nothing of the upload but its pixels is kept. A new picture
    replaces the
    old one, and the old addresses stop answering.

    Args:
        app (str):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app: str,
    *,
    client: AuthenticatedClient,
    body: File,
) -> App | Problem | None:
    """Set an app's icon

     Send the picture itself as the body (`Content-Type: application/octet-stream`, or the picture's own
    type):
    PNG, JPEG or WebP, up to 1 MiB, at least 32 and at most 2048 pixels on each side. The type is read
    from the
    bytes, never from a file name; SVG, GIF, animated WebP and anything else are refused (`422
    unsupported_image`), and so is a body whose `Content-Type` names another picture type than its bytes
    are.
    We decode it, take the middle square of a picture that is not square, and make new WebP files of 64,
    128
    and 256 pixels with no metadata, so nothing of the upload but its pixels is kept. A new picture
    replaces the
    old one, and the old addresses stop answering.

    Args:
        app (str):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | Problem
    """

    return sync_detailed(
        app=app,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app: str,
    *,
    client: AuthenticatedClient,
    body: File,
) -> Response[App | Problem]:
    """Set an app's icon

     Send the picture itself as the body (`Content-Type: application/octet-stream`, or the picture's own
    type):
    PNG, JPEG or WebP, up to 1 MiB, at least 32 and at most 2048 pixels on each side. The type is read
    from the
    bytes, never from a file name; SVG, GIF, animated WebP and anything else are refused (`422
    unsupported_image`), and so is a body whose `Content-Type` names another picture type than its bytes
    are.
    We decode it, take the middle square of a picture that is not square, and make new WebP files of 64,
    128
    and 256 pixels with no metadata, so nothing of the upload but its pixels is kept. A new picture
    replaces the
    old one, and the old addresses stop answering.

    Args:
        app (str):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[App | Problem]
    """

    kwargs = _get_kwargs(
        app=app,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app: str,
    *,
    client: AuthenticatedClient,
    body: File,
) -> App | Problem | None:
    """Set an app's icon

     Send the picture itself as the body (`Content-Type: application/octet-stream`, or the picture's own
    type):
    PNG, JPEG or WebP, up to 1 MiB, at least 32 and at most 2048 pixels on each side. The type is read
    from the
    bytes, never from a file name; SVG, GIF, animated WebP and anything else are refused (`422
    unsupported_image`), and so is a body whose `Content-Type` names another picture type than its bytes
    are.
    We decode it, take the middle square of a picture that is not square, and make new WebP files of 64,
    128
    and 256 pixels with no metadata, so nothing of the upload but its pixels is kept. A new picture
    replaces the
    old one, and the old addresses stop answering.

    Args:
        app (str):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        App | Problem
    """

    return (
        await asyncio_detailed(
            app=app,
            client=client,
            body=body,
        )
    ).parsed

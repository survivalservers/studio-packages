"""connect(): the client signed in with an API key, with this package's defaults: a time limit and the client's name
and version. Hand-written: oss/clients/generate.sh copies it in beside the generated code."""

from importlib import metadata
from typing import Any

import httpx

from .client import AuthenticatedClient

# How long a call waits for each part of its answer: above the API's longest wait of 60 seconds. A followed log that
# may stay quiet for longer needs timeout=httpx.Timeout(70.0, read=None).
DEFAULT_TIMEOUT = httpx.Timeout(70.0, connect=10.0)


def _user_agent() -> str:
    try:
        return "survivalservers-studio/" + metadata.version("survivalservers-studio")
    except metadata.PackageNotFoundError:
        return "survivalservers-studio"


# Which client and version is calling, for the API's logs. A User-Agent in headers replaces it.
USER_AGENT = _user_agent()


def connect(api_key: str, base_url: str, *, timeout: httpx.Timeout | None = DEFAULT_TIMEOUT,
            headers: dict[str, str] | None = None, **kwargs: Any) -> AuthenticatedClient:
    """A client for the API at base_url (https://studio.survivalservers.com) with an API key (gsk_live_...).
    Other keyword arguments go to AuthenticatedClient (httpx_args, raise_on_unexpected_status)."""
    if not api_key:
        raise ValueError("an API key is required")
    if not base_url:
        raise ValueError("the API's address is required (https://studio.survivalservers.com)")
    return AuthenticatedClient(base_url=base_url.rstrip("/"), token=api_key, timeout=timeout,
                               headers={"User-Agent": USER_AGENT, **(headers or {})}, **kwargs)

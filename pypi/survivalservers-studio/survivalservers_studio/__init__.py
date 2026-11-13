"""A client library for accessing Survival Servers Studio API"""

from .client import AuthenticatedClient, Client
from .connect import DEFAULT_TIMEOUT, USER_AGENT, connect

__all__ = (
    "DEFAULT_TIMEOUT",
    "USER_AGENT",
    "AuthenticatedClient",
    "Client",
    "connect",
)

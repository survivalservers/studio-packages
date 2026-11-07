"""Survival Servers Studio, game server hosting for studios by Survival Servers.

The Python client for the Studio API is not released yet. This first version has one helper, docs_url().
"""

__version__ = "0.0.0"

DOCS_URL = "https://studio.survivalservers.com/docs/"


def docs_url(page: str = "") -> str:
    """Return the address of a Survival Servers Studio docs page, for example docs_url("guides/api-clients/")."""
    return DOCS_URL + page.lstrip("/")

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusCardCreate")


@_attrs_define
class StatusCardCreate:
    """
    Attributes:
        url (str): A Discord webhook URL, `https://discord.com/api/webhooks/...`. It is the secret: shown masked from
            then on.
        app (str): App ID or slug.
        branch (str | Unset): The branch whose version the card shows. Default: 'live'.
        regions (list[str] | Unset): Regions to list. Empty lists every region the branch's version is ready in.
        persistent_servers (list[str] | Unset): Persistent servers to list, with their player counts. Default none.
    """

    url: str
    app: str
    branch: str | Unset = "live"
    regions: list[str] | Unset = UNSET
    persistent_servers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        app = self.app

        branch = self.branch

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        persistent_servers: list[str] | Unset = UNSET
        if not isinstance(self.persistent_servers, Unset):
            persistent_servers = self.persistent_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "app": app,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if regions is not UNSET:
            field_dict["regions"] = regions
        if persistent_servers is not UNSET:
            field_dict["persistent_servers"] = persistent_servers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        app = d.pop("app")

        branch = d.pop("branch", UNSET)

        regions = cast(list[str], d.pop("regions", UNSET))

        persistent_servers = cast(list[str], d.pop("persistent_servers", UNSET))

        status_card_create = cls(
            url=url,
            app=app,
            branch=branch,
            regions=regions,
            persistent_servers=persistent_servers,
        )

        status_card_create.additional_properties = d
        return status_card_create

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServerEventDataDiskHigh")


@_attrs_define
class GameServerEventDataDiskHigh:
    """`game_server.disk_high` only.

    Attributes:
        used_mb (int): What its own files took when measured (its folder, its saves and what it wrote into its
            container; on Windows the build's files in its folder count too, and its size includes them).
        size_mb (int): Its disk size: its build plus 10 GiB, or 50 GiB for a persistent server, never less than its
            files held when its run began.
        free_mb (int): Free space on the machine's emptiest disk that holds game servers' files.
        since (datetime.datetime | Unset): When it was first measured over its size (when it was stopped, for a nearly
            full machine disk).
    """

    used_mb: int
    size_mb: int
    free_mb: int
    since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_mb = self.used_mb

        size_mb = self.size_mb

        free_mb = self.free_mb

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used_mb": used_mb,
                "size_mb": size_mb,
                "free_mb": free_mb,
            }
        )
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        used_mb = d.pop("used_mb")

        size_mb = d.pop("size_mb")

        free_mb = d.pop("free_mb")

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        game_server_event_data_disk_high = cls(
            used_mb=used_mb,
            size_mb=size_mb,
            free_mb=free_mb,
            since=since,
        )

        game_server_event_data_disk_high.additional_properties = d
        return game_server_event_data_disk_high

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

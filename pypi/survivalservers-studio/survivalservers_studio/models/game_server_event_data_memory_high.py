from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServerEventDataMemoryHigh")


@_attrs_define
class GameServerEventDataMemoryHigh:
    """`game_server.memory_high` only.

    Attributes:
        memory_mb (int): Its use when the minute was up (Windows: committed; Linux: in use less the file cache the
            system can drop).
        size_mb (int): Its memory size.
        since (datetime.datetime | Unset): When it went over 90%.
    """

    memory_mb: int
    size_mb: int
    since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_mb = self.memory_mb

        size_mb = self.size_mb

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory_mb": memory_mb,
                "size_mb": size_mb,
            }
        )
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        memory_mb = d.pop("memory_mb")

        size_mb = d.pop("size_mb")

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        game_server_event_data_memory_high = cls(
            memory_mb=memory_mb,
            size_mb=size_mb,
            since=since,
        )

        game_server_event_data_memory_high.additional_properties = d
        return game_server_event_data_memory_high

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

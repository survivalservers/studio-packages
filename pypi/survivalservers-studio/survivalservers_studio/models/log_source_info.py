from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogSourceInfo")


@_attrs_define
class LogSourceInfo:
    """
    Attributes:
        name (str):
        bytes_ (int | None): The bytes kept. While the game server runs, what it has sent so far (about every 15
            minutes); `null` while nothing has been sent yet, which does not mean the log is empty.
        live (bool):
    """

    name: str
    bytes_: int | None
    live: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bytes_: int | None
        bytes_ = self.bytes_

        live = self.live

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "bytes": bytes_,
                "live": live,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_bytes_(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        bytes_ = _parse_bytes_(d.pop("bytes"))

        live = d.pop("live")

        log_source_info = cls(
            name=name,
            bytes_=bytes_,
            live=live,
        )

        log_source_info.additional_properties = d
        return log_source_info

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

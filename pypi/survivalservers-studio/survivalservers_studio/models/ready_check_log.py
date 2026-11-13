from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ready_check_log_type import ReadyCheckLogType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadyCheckLog")


@_attrs_define
class ReadyCheckLog:
    """A regular expression on the console or a log file.

    Attributes:
        type_ (ReadyCheckLogType):
        pattern (str):
        source (str | Unset): Default the console.
    """

    type_: ReadyCheckLogType
    pattern: str
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        pattern = self.pattern

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "pattern": pattern,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ReadyCheckLogType(d.pop("type"))

        pattern = d.pop("pattern")

        source = d.pop("source", UNSET)

        ready_check_log = cls(
            type_=type_,
            pattern=pattern,
            source=source,
        )

        ready_check_log.additional_properties = d
        return ready_check_log

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

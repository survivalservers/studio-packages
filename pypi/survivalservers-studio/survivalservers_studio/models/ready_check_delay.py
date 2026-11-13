from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ready_check_delay_type import ReadyCheckDelayType

T = TypeVar("T", bound="ReadyCheckDelay")


@_attrs_define
class ReadyCheckDelay:
    """Ready after a fixed time.

    Attributes:
        type_ (ReadyCheckDelayType):
        after (int | str): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
    """

    type_: ReadyCheckDelayType
    after: int | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        after: int | str
        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "after": after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ReadyCheckDelayType(d.pop("type"))

        def _parse_after(data: object) -> int | str:
            return cast(int | str, data)

        after = _parse_after(d.pop("after"))

        ready_check_delay = cls(
            type_=type_,
            after=after,
        )

        ready_check_delay.additional_properties = d
        return ready_check_delay

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkActionWarning")


@_attrs_define
class BulkActionWarning:
    """
    Attributes:
        before (int | str): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        message (str):
    """

    before: int | str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        before: int | str
        before = self.before

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "before": before,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_before(data: object) -> int | str:
            return cast(int | str, data)

        before = _parse_before(d.pop("before"))

        message = d.pop("message")

        bulk_action_warning = cls(
            before=before,
            message=message,
        )

        bulk_action_warning.additional_properties = d
        return bulk_action_warning

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

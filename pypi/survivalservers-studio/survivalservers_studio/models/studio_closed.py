from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StudioClosed")


@_attrs_define
class StudioClosed:
    """
    Attributes:
        closed_at (datetime.datetime):
        readable_until (datetime.datetime):
        deleted_by (datetime.datetime):
    """

    closed_at: datetime.datetime
    readable_until: datetime.datetime
    deleted_by: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed_at = self.closed_at.isoformat()

        readable_until = self.readable_until.isoformat()

        deleted_by = self.deleted_by.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "closed_at": closed_at,
                "readable_until": readable_until,
                "deleted_by": deleted_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        closed_at = datetime.datetime.fromisoformat(d.pop("closed_at"))

        readable_until = datetime.datetime.fromisoformat(d.pop("readable_until"))

        deleted_by = datetime.datetime.fromisoformat(d.pop("deleted_by"))

        studio_closed = cls(
            closed_at=closed_at,
            readable_until=readable_until,
            deleted_by=deleted_by,
        )

        studio_closed.additional_properties = d
        return studio_closed

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

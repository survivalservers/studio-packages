from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageFreeMonth")


@_attrs_define
class UsageFreeMonth:
    """
    Attributes:
        month (str): The month, `YYYY-MM`.
        free_cpu_hours (int): The month's free vCPU-hours.
        used_up_at (datetime.datetime | None): When the month's usage passed its free vCPU-hours, to the minute; `null`
            when some were still left at the end of the period, and the month's first moment when it has none.
    """

    month: str
    free_cpu_hours: int
    used_up_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        free_cpu_hours = self.free_cpu_hours

        used_up_at: None | str
        if isinstance(self.used_up_at, datetime.datetime):
            used_up_at = self.used_up_at.isoformat()
        else:
            used_up_at = self.used_up_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "free_cpu_hours": free_cpu_hours,
                "used_up_at": used_up_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        month = d.pop("month")

        free_cpu_hours = d.pop("free_cpu_hours")

        def _parse_used_up_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                used_up_at_type_0 = datetime.datetime.fromisoformat(data)

                return used_up_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        used_up_at = _parse_used_up_at(d.pop("used_up_at"))

        usage_free_month = cls(
            month=month,
            free_cpu_hours=free_cpu_hours,
            used_up_at=used_up_at,
        )

        usage_free_month.additional_properties = d
        return usage_free_month

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

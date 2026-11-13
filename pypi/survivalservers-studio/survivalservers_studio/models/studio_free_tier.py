from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StudioFreeTier")


@_attrs_define
class StudioFreeTier:
    """This month's free vCPU-hours and how many are used. For a key limited to some apps, `cpu_hours_used` counts its
    apps' usage alone.

        Attributes:
            cpu_hours_per_month (int):
            cpu_hours_used (str): vCPU-hours as a decimal string.
    """

    cpu_hours_per_month: int
    cpu_hours_used: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_hours_per_month = self.cpu_hours_per_month

        cpu_hours_used = self.cpu_hours_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_hours_per_month": cpu_hours_per_month,
                "cpu_hours_used": cpu_hours_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu_hours_per_month = d.pop("cpu_hours_per_month")

        cpu_hours_used = d.pop("cpu_hours_used")

        studio_free_tier = cls(
            cpu_hours_per_month=cpu_hours_per_month,
            cpu_hours_used=cpu_hours_used,
        )

        studio_free_tier.additional_properties = d
        return studio_free_tier

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

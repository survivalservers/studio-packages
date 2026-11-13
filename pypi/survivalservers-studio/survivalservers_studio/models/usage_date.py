from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageDate")


@_attrs_define
class UsageDate:
    """One hour, day, week, month or year of a usage report: its vCPU-hours, the vCPU-hours of it the month's free vCPU-
    hours covered (its usage before they ran out), and what it cost after them and credits (the month's bill so far at
    its end minus at its start; nothing before the free vCPU-hours ran out but what they never cover, such as
    reservations and your own machines).

        Attributes:
            date (str): The UTC hour, day, week, month or year, as in `rows`.
            cpu_hours (str): vCPU-hours as a decimal string.
            free_cpu_hours (str): vCPU-hours as a decimal string.
            amount_usd (str): USD as a decimal string.
    """

    date: str
    cpu_hours: str
    free_cpu_hours: str
    amount_usd: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cpu_hours = self.cpu_hours

        free_cpu_hours = self.free_cpu_hours

        amount_usd = self.amount_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "cpu_hours": cpu_hours,
                "free_cpu_hours": free_cpu_hours,
                "amount_usd": amount_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        cpu_hours = d.pop("cpu_hours")

        free_cpu_hours = d.pop("free_cpu_hours")

        amount_usd = d.pop("amount_usd")

        usage_date = cls(
            date=date,
            cpu_hours=cpu_hours,
            free_cpu_hours=free_cpu_hours,
            amount_usd=amount_usd,
        )

        usage_date.additional_properties = d
        return usage_date

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

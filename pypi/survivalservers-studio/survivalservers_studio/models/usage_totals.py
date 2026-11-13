from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageTotals")


@_attrs_define
class UsageTotals:
    """The period's vCPU-hours, and what it cost: the month's bill (as on its invoice: the free vCPU-hours on the month's
    dearest usage first, then credits) at the period's end minus at its start, each month on its own. Periods side by
    side add up to the month, and a whole closed month to its invoice.

        Attributes:
            cpu_hours (str): vCPU-hours as a decimal string.
            amount_usd (str): USD as a decimal string.
            free_cpu_hours_used (str): vCPU-hours as a decimal string.
            credits_usd (str): USD as a decimal string.
            projected_month_usd (str): USD as a decimal string.
            backup_gb_months (str | Unset): Backup storage in the period
            free_backup_gb_months_used (str | Unset): Of that
    """

    cpu_hours: str
    amount_usd: str
    free_cpu_hours_used: str
    credits_usd: str
    projected_month_usd: str
    backup_gb_months: str | Unset = UNSET
    free_backup_gb_months_used: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_hours = self.cpu_hours

        amount_usd = self.amount_usd

        free_cpu_hours_used = self.free_cpu_hours_used

        credits_usd = self.credits_usd

        projected_month_usd = self.projected_month_usd

        backup_gb_months = self.backup_gb_months

        free_backup_gb_months_used = self.free_backup_gb_months_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_hours": cpu_hours,
                "amount_usd": amount_usd,
                "free_cpu_hours_used": free_cpu_hours_used,
                "credits_usd": credits_usd,
                "projected_month_usd": projected_month_usd,
            }
        )
        if backup_gb_months is not UNSET:
            field_dict["backup_gb_months"] = backup_gb_months
        if free_backup_gb_months_used is not UNSET:
            field_dict["free_backup_gb_months_used"] = free_backup_gb_months_used

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu_hours = d.pop("cpu_hours")

        amount_usd = d.pop("amount_usd")

        free_cpu_hours_used = d.pop("free_cpu_hours_used")

        credits_usd = d.pop("credits_usd")

        projected_month_usd = d.pop("projected_month_usd")

        backup_gb_months = d.pop("backup_gb_months", UNSET)

        free_backup_gb_months_used = d.pop("free_backup_gb_months_used", UNSET)

        usage_totals = cls(
            cpu_hours=cpu_hours,
            amount_usd=amount_usd,
            free_cpu_hours_used=free_cpu_hours_used,
            credits_usd=credits_usd,
            projected_month_usd=projected_month_usd,
            backup_gb_months=backup_gb_months,
            free_backup_gb_months_used=free_backup_gb_months_used,
        )

        usage_totals.additional_properties = d
        return usage_totals

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

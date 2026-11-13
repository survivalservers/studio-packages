from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_report_currency import UsageReportCurrency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_date import UsageDate
    from ..models.usage_free_month import UsageFreeMonth
    from ..models.usage_row import UsageRow
    from ..models.usage_totals import UsageTotals


T = TypeVar("T", bound="UsageReport")


@_attrs_define
class UsageReport:
    """
    Attributes:
        currency (UsageReportCurrency):
        totals (UsageTotals): The period's vCPU-hours, and what it cost: the month's bill (as on its invoice: the free
            vCPU-hours on the month's dearest usage first, then credits) at the period's end minus at its start, each month
            on its own. Periods side by side add up to the month, and a whole closed month to its invoice.
        rows (list[UsageRow]):
        free_hours (list[UsageFreeMonth] | Unset): Each calendar month (UTC) the period touches, oldest first: its free
            vCPU-hours and when they ran out, counting the month's usage in time order from its first day (the free vCPU-
            hours' value still goes to the month's most expensive usage first).
        dates (list[UsageDate] | Unset): Each hour, day, week, month or year of the period with usage or a cost, oldest
            first, priced like the totals: what the month's bill grew by over it. They add up to the totals.
    """

    currency: UsageReportCurrency
    totals: UsageTotals
    rows: list[UsageRow]
    free_hours: list[UsageFreeMonth] | Unset = UNSET
    dates: list[UsageDate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        totals = self.totals.to_dict()

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        free_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.free_hours, Unset):
            free_hours = []
            for free_hours_item_data in self.free_hours:
                free_hours_item = free_hours_item_data.to_dict()
                free_hours.append(free_hours_item)

        dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.to_dict()
                dates.append(dates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "totals": totals,
                "rows": rows,
            }
        )
        if free_hours is not UNSET:
            field_dict["free_hours"] = free_hours
        if dates is not UNSET:
            field_dict["dates"] = dates

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_date import UsageDate
        from ..models.usage_free_month import UsageFreeMonth
        from ..models.usage_row import UsageRow
        from ..models.usage_totals import UsageTotals

        d = dict(src_dict)
        currency = UsageReportCurrency(d.pop("currency"))

        totals = UsageTotals.from_dict(d.pop("totals"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = UsageRow.from_dict(rows_item_data)

            rows.append(rows_item)

        _free_hours = d.pop("free_hours", UNSET)
        free_hours: list[UsageFreeMonth] | Unset = UNSET
        if _free_hours is not UNSET:
            free_hours = []
            for free_hours_item_data in _free_hours:
                free_hours_item = UsageFreeMonth.from_dict(free_hours_item_data)

                free_hours.append(free_hours_item)

        _dates = d.pop("dates", UNSET)
        dates: list[UsageDate] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = UsageDate.from_dict(dates_item_data)

                dates.append(dates_item)

        usage_report = cls(
            currency=currency,
            totals=totals,
            rows=rows,
            free_hours=free_hours,
            dates=dates,
        )

        usage_report.additional_properties = d
        return usage_report

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

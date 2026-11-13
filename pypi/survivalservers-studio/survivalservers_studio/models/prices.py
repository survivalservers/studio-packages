from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prices_bandwidth import PricesBandwidth
from ..models.prices_currency import PricesCurrency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prices_rates import PricesRates


T = TypeVar("T", bound="Prices")


@_attrs_define
class Prices:
    """
    Attributes:
        currency (PricesCurrency):
        locked_until (datetime.datetime):
        rates (PricesRates):
        free_cpu_hours_per_month (int):
        paused_free_minutes (int): The first minutes of each freeze of a paused persistent server are free.
        bandwidth (PricesBandwidth):
        free_backup_gb_months (int | Unset): Backup storage each month at no charge.
    """

    currency: PricesCurrency
    locked_until: datetime.datetime
    rates: PricesRates
    free_cpu_hours_per_month: int
    paused_free_minutes: int
    bandwidth: PricesBandwidth
    free_backup_gb_months: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        locked_until = self.locked_until.isoformat()

        rates = self.rates.to_dict()

        free_cpu_hours_per_month = self.free_cpu_hours_per_month

        paused_free_minutes = self.paused_free_minutes

        bandwidth = self.bandwidth.value

        free_backup_gb_months = self.free_backup_gb_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "locked_until": locked_until,
                "rates": rates,
                "free_cpu_hours_per_month": free_cpu_hours_per_month,
                "paused_free_minutes": paused_free_minutes,
                "bandwidth": bandwidth,
            }
        )
        if free_backup_gb_months is not UNSET:
            field_dict["free_backup_gb_months"] = free_backup_gb_months

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.prices_rates import PricesRates

        d = dict(src_dict)
        currency = PricesCurrency(d.pop("currency"))

        locked_until = datetime.datetime.fromisoformat(d.pop("locked_until"))

        rates = PricesRates.from_dict(d.pop("rates"))

        free_cpu_hours_per_month = d.pop("free_cpu_hours_per_month")

        paused_free_minutes = d.pop("paused_free_minutes")

        bandwidth = PricesBandwidth(d.pop("bandwidth"))

        free_backup_gb_months = d.pop("free_backup_gb_months", UNSET)

        prices = cls(
            currency=currency,
            locked_until=locked_until,
            rates=rates,
            free_cpu_hours_per_month=free_cpu_hours_per_month,
            paused_free_minutes=paused_free_minutes,
            bandwidth=bandwidth,
            free_backup_gb_months=free_backup_gb_months,
        )

        prices.additional_properties = d
        return prices

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

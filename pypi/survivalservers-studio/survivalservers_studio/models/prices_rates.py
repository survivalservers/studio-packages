from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PricesRates")


@_attrs_define
class PricesRates:
    """
    Attributes:
        on_demand_cpu_hour_2gb (str): USD as a decimal string.
        on_demand_cpu_hour_4gb (str): USD as a decimal string.
        reserved_cpu_hour (str): USD as a decimal string.
        persistent_server_cpu_hour (str): USD as a decimal string.
        own_machine_cpu_month (str): USD as a decimal string.
        paused_cpu_hour (str): USD as a decimal string.
        warm_cpu_hour (str | Unset): USD as a decimal string.
        backup_gb_month (str | Unset): USD as a decimal string.
    """

    on_demand_cpu_hour_2gb: str
    on_demand_cpu_hour_4gb: str
    reserved_cpu_hour: str
    persistent_server_cpu_hour: str
    own_machine_cpu_month: str
    paused_cpu_hour: str
    warm_cpu_hour: str | Unset = UNSET
    backup_gb_month: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_demand_cpu_hour_2gb = self.on_demand_cpu_hour_2gb

        on_demand_cpu_hour_4gb = self.on_demand_cpu_hour_4gb

        reserved_cpu_hour = self.reserved_cpu_hour

        persistent_server_cpu_hour = self.persistent_server_cpu_hour

        own_machine_cpu_month = self.own_machine_cpu_month

        paused_cpu_hour = self.paused_cpu_hour

        warm_cpu_hour = self.warm_cpu_hour

        backup_gb_month = self.backup_gb_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "on_demand_cpu_hour_2gb": on_demand_cpu_hour_2gb,
                "on_demand_cpu_hour_4gb": on_demand_cpu_hour_4gb,
                "reserved_cpu_hour": reserved_cpu_hour,
                "persistent_server_cpu_hour": persistent_server_cpu_hour,
                "own_machine_cpu_month": own_machine_cpu_month,
                "paused_cpu_hour": paused_cpu_hour,
            }
        )
        if warm_cpu_hour is not UNSET:
            field_dict["warm_cpu_hour"] = warm_cpu_hour
        if backup_gb_month is not UNSET:
            field_dict["backup_gb_month"] = backup_gb_month

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        on_demand_cpu_hour_2gb = d.pop("on_demand_cpu_hour_2gb")

        on_demand_cpu_hour_4gb = d.pop("on_demand_cpu_hour_4gb")

        reserved_cpu_hour = d.pop("reserved_cpu_hour")

        persistent_server_cpu_hour = d.pop("persistent_server_cpu_hour")

        own_machine_cpu_month = d.pop("own_machine_cpu_month")

        paused_cpu_hour = d.pop("paused_cpu_hour")

        warm_cpu_hour = d.pop("warm_cpu_hour", UNSET)

        backup_gb_month = d.pop("backup_gb_month", UNSET)

        prices_rates = cls(
            on_demand_cpu_hour_2gb=on_demand_cpu_hour_2gb,
            on_demand_cpu_hour_4gb=on_demand_cpu_hour_4gb,
            reserved_cpu_hour=reserved_cpu_hour,
            persistent_server_cpu_hour=persistent_server_cpu_hour,
            own_machine_cpu_month=own_machine_cpu_month,
            paused_cpu_hour=paused_cpu_hour,
            warm_cpu_hour=warm_cpu_hour,
            backup_gb_month=backup_gb_month,
        )

        prices_rates.additional_properties = d
        return prices_rates

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

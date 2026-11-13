from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rate_class import RateClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageRow")


@_attrs_define
class UsageRow:
    """
    Attributes:
        date (str): The UTC hour, day, week, month or year this row covers: `2026-10-09T14:00:00Z`, `2026-10-09`, the
            week's Monday `2026-10-05`, `2026-10` or `2026`.
        cpu_hours (str): vCPU-hours as a decimal string.
        amount_usd (str): USD as a decimal string.
        app (str | Unset): App ID.
        version (str | Unset): Version name, unique in its app, for example `2.3.1`.
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        rate_class (RateClass | Unset): `warm` appears only if warm standby is billed. `persistent_server_paused`: a
            paused persistent server kept paused past its free minutes. `reserved_included`: usage a reservation covered,
            priced at 0; the reservation's own `reserved` row is what it costs. New classes may be added (section 1.1).
        backup_gb_hours (str | Unset): Backup storage in this row
    """

    date: str
    cpu_hours: str
    amount_usd: str
    app: str | Unset = UNSET
    version: str | Unset = UNSET
    region: str | Unset = UNSET
    rate_class: RateClass | Unset = UNSET
    backup_gb_hours: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cpu_hours = self.cpu_hours

        amount_usd = self.amount_usd

        app = self.app

        version = self.version

        region = self.region

        rate_class: str | Unset = UNSET
        if not isinstance(self.rate_class, Unset):
            rate_class = self.rate_class.value

        backup_gb_hours = self.backup_gb_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "cpu_hours": cpu_hours,
                "amount_usd": amount_usd,
            }
        )
        if app is not UNSET:
            field_dict["app"] = app
        if version is not UNSET:
            field_dict["version"] = version
        if region is not UNSET:
            field_dict["region"] = region
        if rate_class is not UNSET:
            field_dict["rate_class"] = rate_class
        if backup_gb_hours is not UNSET:
            field_dict["backup_gb_hours"] = backup_gb_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        cpu_hours = d.pop("cpu_hours")

        amount_usd = d.pop("amount_usd")

        app = d.pop("app", UNSET)

        version = d.pop("version", UNSET)

        region = d.pop("region", UNSET)

        _rate_class = d.pop("rate_class", UNSET)
        rate_class: RateClass | Unset
        if isinstance(_rate_class, Unset):
            rate_class = UNSET
        else:
            rate_class = RateClass(_rate_class)

        backup_gb_hours = d.pop("backup_gb_hours", UNSET)

        usage_row = cls(
            date=date,
            cpu_hours=cpu_hours,
            amount_usd=amount_usd,
            app=app,
            version=version,
            region=region,
            rate_class=rate_class,
            backup_gb_hours=backup_gb_hours,
        )

        usage_row.additional_properties = d
        return usage_row

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

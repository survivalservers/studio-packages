from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rate_class import RateClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLine")


@_attrs_define
class InvoiceLine:
    """
    Attributes:
        description (str):
        amount_usd (str): USD as a decimal string.
        rate_class (RateClass | Unset): `warm` appears only if warm standby is billed. `persistent_server_paused`: a
            paused persistent server kept paused past its free minutes. `reserved_included`: usage a reservation covered,
            priced at 0; the reservation's own `reserved` row is what it costs. New classes may be added (section 1.1).
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        cpu_hours (str | Unset): USD as a decimal string.
        usage_period (None | str | Unset): The month this line's usage ran in, when it is not the invoice's own (usage
            that reached us after that month's invoice was made).
    """

    description: str
    amount_usd: str
    rate_class: RateClass | Unset = UNSET
    region: str | Unset = UNSET
    cpu_hours: str | Unset = UNSET
    usage_period: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        amount_usd = self.amount_usd

        rate_class: str | Unset = UNSET
        if not isinstance(self.rate_class, Unset):
            rate_class = self.rate_class.value

        region = self.region

        cpu_hours = self.cpu_hours

        usage_period: None | str | Unset
        if isinstance(self.usage_period, Unset):
            usage_period = UNSET
        else:
            usage_period = self.usage_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "amount_usd": amount_usd,
            }
        )
        if rate_class is not UNSET:
            field_dict["rate_class"] = rate_class
        if region is not UNSET:
            field_dict["region"] = region
        if cpu_hours is not UNSET:
            field_dict["cpu_hours"] = cpu_hours
        if usage_period is not UNSET:
            field_dict["usage_period"] = usage_period

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        amount_usd = d.pop("amount_usd")

        _rate_class = d.pop("rate_class", UNSET)
        rate_class: RateClass | Unset
        if isinstance(_rate_class, Unset):
            rate_class = UNSET
        else:
            rate_class = RateClass(_rate_class)

        region = d.pop("region", UNSET)

        cpu_hours = d.pop("cpu_hours", UNSET)

        def _parse_usage_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_period = _parse_usage_period(d.pop("usage_period", UNSET))

        invoice_line = cls(
            description=description,
            amount_usd=amount_usd,
            rate_class=rate_class,
            region=region,
            cpu_hours=cpu_hours,
            usage_period=usage_period,
        )

        invoice_line.additional_properties = d
        return invoice_line

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

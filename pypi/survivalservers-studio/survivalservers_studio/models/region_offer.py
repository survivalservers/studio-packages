from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..models.tier import Tier

T = TypeVar("T", bound="RegionOffer")


@_attrs_define
class RegionOffer:
    """
    Attributes:
        tier (Tier): Public hardware tier.
        os (list[Os]):
    """

    tier: Tier
    os: list[Os]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier.value

        os = []
        for os_item_data in self.os:
            os_item = os_item_data.value
            os.append(os_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "os": os,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tier = Tier(d.pop("tier"))

        os = []
        _os = d.pop("os")
        for os_item_data in _os:
            os_item = Os(os_item_data)

            os.append(os_item)

        region_offer = cls(
            tier=tier,
            os=os,
        )

        region_offer.additional_properties = d
        return region_offer

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

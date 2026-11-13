from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.placement_player_pings_additional_property import (
        PlacementPlayerPingsAdditionalProperty,
    )


T = TypeVar("T", bound="PlacementPlayerPings")


@_attrs_define
class PlacementPlayerPings:
    """Measured ping in ms per player per region (from the beacons). Regions are ranked by the worst player's ping."""

    additional_properties: dict[str, PlacementPlayerPingsAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.placement_player_pings_additional_property import (
            PlacementPlayerPingsAdditionalProperty,
        )

        d = dict(src_dict)
        placement_player_pings = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PlacementPlayerPingsAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        placement_player_pings.additional_properties = additional_properties
        return placement_player_pings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PlacementPlayerPingsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: PlacementPlayerPingsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

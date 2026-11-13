from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.placement_player_pings import PlacementPlayerPings


T = TypeVar("T", bound="Placement")


@_attrs_define
class Placement:
    """
    Attributes:
        regions (list[str] | Unset): Preferred regions in order.
        continents (list[str] | Unset): Any region in these continents, after `regions`.
        player_pings (PlacementPlayerPings | Unset): Measured ping in ms per player per region (from the beacons).
            Regions are ranked by the worst player's ping.
        player_ips (list[str] | Unset): Used when pings are missing; we estimate from location.
        max_ping_ms (int | Unset): Drop regions above this worst-player ping.
        fallback (bool | Unset): If nothing meets `max_ping_ms`, use the best region that has capacity and say so in the
            reply. Default: True.
    """

    regions: list[str] | Unset = UNSET
    continents: list[str] | Unset = UNSET
    player_pings: PlacementPlayerPings | Unset = UNSET
    player_ips: list[str] | Unset = UNSET
    max_ping_ms: int | Unset = UNSET
    fallback: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        continents: list[str] | Unset = UNSET
        if not isinstance(self.continents, Unset):
            continents = self.continents

        player_pings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_pings, Unset):
            player_pings = self.player_pings.to_dict()

        player_ips: list[str] | Unset = UNSET
        if not isinstance(self.player_ips, Unset):
            player_ips = self.player_ips

        max_ping_ms = self.max_ping_ms

        fallback = self.fallback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["regions"] = regions
        if continents is not UNSET:
            field_dict["continents"] = continents
        if player_pings is not UNSET:
            field_dict["player_pings"] = player_pings
        if player_ips is not UNSET:
            field_dict["player_ips"] = player_ips
        if max_ping_ms is not UNSET:
            field_dict["max_ping_ms"] = max_ping_ms
        if fallback is not UNSET:
            field_dict["fallback"] = fallback

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.placement_player_pings import PlacementPlayerPings

        d = dict(src_dict)
        regions = cast(list[str], d.pop("regions", UNSET))

        continents = cast(list[str], d.pop("continents", UNSET))

        _player_pings = d.pop("player_pings", UNSET)
        player_pings: PlacementPlayerPings | Unset
        if isinstance(_player_pings, Unset):
            player_pings = UNSET
        else:
            player_pings = PlacementPlayerPings.from_dict(_player_pings)

        player_ips = cast(list[str], d.pop("player_ips", UNSET))

        max_ping_ms = d.pop("max_ping_ms", UNSET)

        fallback = d.pop("fallback", UNSET)

        placement = cls(
            regions=regions,
            continents=continents,
            player_pings=player_pings,
            player_ips=player_ips,
            max_ping_ms=max_ping_ms,
            fallback=fallback,
        )

        placement.additional_properties = d
        return placement

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

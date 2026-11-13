from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultPlacement")


@_attrs_define
class DefaultPlacement:
    """Used by starts that send no `placement`.

    Attributes:
        regions (list[str] | Unset):
        continents (list[str] | Unset):
    """

    regions: list[str] | Unset = UNSET
    continents: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        continents: list[str] | Unset = UNSET
        if not isinstance(self.continents, Unset):
            continents = self.continents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["regions"] = regions
        if continents is not UNSET:
            field_dict["continents"] = continents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        regions = cast(list[str], d.pop("regions", UNSET))

        continents = cast(list[str], d.pop("continents", UNSET))

        default_placement = cls(
            regions=regions,
            continents=continents,
        )

        default_placement.additional_properties = d
        return default_placement

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

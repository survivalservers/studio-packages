from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SimulatedPlayers")


@_attrs_define
class SimulatedPlayers:
    """
    Attributes:
        simulated_count (int):
        simulated (bool): Always true; the count is not real players.
    """

    simulated_count: int
    simulated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        simulated_count = self.simulated_count

        simulated = self.simulated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "simulated_count": simulated_count,
                "simulated": simulated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        simulated_count = d.pop("simulated_count")

        simulated = d.pop("simulated")

        simulated_players = cls(
            simulated_count=simulated_count,
            simulated=simulated,
        )

        simulated_players.additional_properties = d
        return simulated_players

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

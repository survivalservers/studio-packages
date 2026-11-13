from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimulatedPlayersSet")


@_attrs_define
class SimulatedPlayersSet:
    """
    Attributes:
        count (int): Simulated players on the game server from now.
    """

    count: int

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        simulated_players_set = cls(
            count=count,
        )

        return simulated_players_set

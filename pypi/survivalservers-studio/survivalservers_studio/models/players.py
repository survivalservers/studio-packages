from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.players_source import PlayersSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="Players")


@_attrs_define
class Players:
    """
    Attributes:
        count (int):
        ids (list[str] | Unset):
        source (PlayersSource | Unset): Where the count came from. `reported`: the game, on the local API. `api`: your
            own calls to the players call (`POST /v0/game-servers/{id}/players`). `query`: the machine read the game's Steam
            query port. `connection`: the machine asked the game the way its game profile says. The machine reads a game
            whose profile says how to read its players every 30 seconds (60 for a console line) while it runs, unless the
            game reports them itself or your calls do. Left out before anything counted.
        simulated_count (int | Unset): Our own test setup only: simulated players, for showing a launch day on a game no
            test player can join. Never part of `count`, and never where studios' game servers run.
    """

    count: int
    ids: list[str] | Unset = UNSET
    source: PlayersSource | Unset = UNSET
    simulated_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        simulated_count = self.simulated_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if source is not UNSET:
            field_dict["source"] = source
        if simulated_count is not UNSET:
            field_dict["simulated_count"] = simulated_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        ids = cast(list[str], d.pop("ids", UNSET))

        _source = d.pop("source", UNSET)
        source: PlayersSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PlayersSource(_source)

        simulated_count = d.pop("simulated_count", UNSET)

        players = cls(
            count=count,
            ids=ids,
            source=source,
            simulated_count=simulated_count,
        )

        players.additional_properties = d
        return players

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

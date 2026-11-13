from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerPlayer")


@_attrs_define
class ServerPlayer:
    """One player. What is here depends on what the game shares.

    Attributes:
        id (str | Unset): The game's ID for the player.
        name (str | Unset): The name other players see.
        x (float | Unset): Its position in the game's own units.
        y (float | Unset):
        z (float | Unset):
        map_ (str | Unset):
        team (str | Unset):
        ping_ms (int | Unset):
        seconds (float | Unset): How long it has been on the server.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    x: float | Unset = UNSET
    y: float | Unset = UNSET
    z: float | Unset = UNSET
    map_: str | Unset = UNSET
    team: str | Unset = UNSET
    ping_ms: int | Unset = UNSET
    seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        x = self.x

        y = self.y

        z = self.z

        map_ = self.map_

        team = self.team

        ping_ms = self.ping_ms

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if map_ is not UNSET:
            field_dict["map"] = map_
        if team is not UNSET:
            field_dict["team"] = team
        if ping_ms is not UNSET:
            field_dict["ping_ms"] = ping_ms
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        map_ = d.pop("map", UNSET)

        team = d.pop("team", UNSET)

        ping_ms = d.pop("ping_ms", UNSET)

        seconds = d.pop("seconds", UNSET)

        server_player = cls(
            id=id,
            name=name,
            x=x,
            y=y,
            z=z,
            map_=map_,
            team=team,
            ping_ms=ping_ms,
            seconds=seconds,
        )

        server_player.additional_properties = d
        return server_player

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

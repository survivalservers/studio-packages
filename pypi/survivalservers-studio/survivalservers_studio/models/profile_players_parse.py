from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilePlayersParse")


@_attrs_define
class ProfilePlayersParse:
    """How to read the answer: `regex` per line, or `list` in a JSON answer.

    Attributes:
        regex (str | Unset): An RE2 pattern tried on each line, with named groups `id`, `name`, `x`, `y`, `z`, `map`,
            `team` and `ping`.
        split (str | Unset): With `regex`: `name` holds every player on one line, split by this.
        list_ (str | Unset): JSON: a path with dots to the list of players. Empty for a list at the top.
        id (str | Unset): JSON: the path to a player's ID in each row. The others below work the same way.
        name (str | Unset):
        x (str | Unset):
        y (str | Unset):
        z (str | Unset):
        map_ (str | Unset):
        team (str | Unset):
        ping (str | Unset):
    """

    regex: str | Unset = UNSET
    split: str | Unset = UNSET
    list_: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    x: str | Unset = UNSET
    y: str | Unset = UNSET
    z: str | Unset = UNSET
    map_: str | Unset = UNSET
    team: str | Unset = UNSET
    ping: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        regex = self.regex

        split = self.split

        list_ = self.list_

        id = self.id

        name = self.name

        x = self.x

        y = self.y

        z = self.z

        map_ = self.map_

        team = self.team

        ping = self.ping

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if regex is not UNSET:
            field_dict["regex"] = regex
        if split is not UNSET:
            field_dict["split"] = split
        if list_ is not UNSET:
            field_dict["list"] = list_
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
        if ping is not UNSET:
            field_dict["ping"] = ping

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        regex = d.pop("regex", UNSET)

        split = d.pop("split", UNSET)

        list_ = d.pop("list", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        map_ = d.pop("map", UNSET)

        team = d.pop("team", UNSET)

        ping = d.pop("ping", UNSET)

        profile_players_parse = cls(
            regex=regex,
            split=split,
            list_=list_,
            id=id,
            name=name,
            x=x,
            y=y,
            z=z,
            map_=map_,
            team=team,
            ping=ping,
        )

        return profile_players_parse

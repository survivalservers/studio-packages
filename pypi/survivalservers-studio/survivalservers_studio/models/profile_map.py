from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileMap")


@_attrs_define
class ProfileMap:
    """
    Attributes:
        id (str): Matches a player's `map`. With one map, every player is on it.
        name (str):
        image (str): The address of a picture of the whole map, on your own site.
        x (list[float]): The game's x at the picture's left and right edges.
        y (list[float]): The game's y at the picture's top and bottom edges.
    """

    id: str
    name: str
    image: str
    x: list[float]
    y: list[float]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        image = self.image

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "image": image,
                "x": x,
                "y": y,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        image = d.pop("image")

        x = cast(list[float], d.pop("x"))

        y = cast(list[float], d.pop("y"))

        profile_map = cls(
            id=id,
            name=name,
            image=image,
            x=x,
            y=y,
        )

        return profile_map

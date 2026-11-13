from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_command_console_type import GameCommandConsoleType

T = TypeVar("T", bound="GameCommandConsole")


@_attrs_define
class GameCommandConsole:
    """A line typed into the game's console (its standard input), followed by Enter (CR LF on Windows, LF on Linux).

    Attributes:
        type_ (GameCommandConsoleType):
        line (str):
    """

    type_: GameCommandConsoleType
    line: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        line = self.line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "line": line,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = GameCommandConsoleType(d.pop("type"))

        line = d.pop("line")

        game_command_console = cls(
            type_=type_,
            line=line,
        )

        game_command_console.additional_properties = d
        return game_command_console

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

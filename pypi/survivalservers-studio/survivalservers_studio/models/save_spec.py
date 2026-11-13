from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="SaveSpec")


@_attrs_define
class SaveSpec:
    """How to make the game save, for servers that do not save on their own before a backup: sent before every persistent
    server backup (manual, scheduled and at a stop) and before the stop method. A save that fails or runs out of time
    does not hold up the backup; the timeline says `save_failed`.

        Attributes:
            command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon): A command for the game
                server itself.
            wait (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
            done_log (str | Unset): A console line (an RE2 pattern) that says the save is done, ending the wait early.
    """

    command: (
        GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon
    )
    wait: int | str | Unset = UNSET
    done_log: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        command: dict[str, Any]
        if (
            isinstance(self.command, GameCommandConsole)
            or isinstance(self.command, GameCommandRcon)
            or isinstance(self.command, GameCommandHttp)
        ):
            command = self.command.to_dict()
        else:
            command = self.command.to_dict()

        wait: int | str | Unset
        if isinstance(self.wait, Unset):
            wait = UNSET
        else:
            wait = self.wait

        done_log = self.done_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if wait is not UNSET:
            field_dict["wait"] = wait
        if done_log is not UNSET:
            field_dict["done_log"] = done_log

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)

        def _parse_command(
            data: object,
        ) -> (
            GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_0 = GameCommandConsole.from_dict(
                    data
                )

                return componentsschemas_game_command_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_1 = GameCommandRcon.from_dict(data)

                return componentsschemas_game_command_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_2 = GameCommandHttp.from_dict(data)

                return componentsschemas_game_command_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_game_command_type_3 = GameCommandIsleRcon.from_dict(data)

            return componentsschemas_game_command_type_3

        command = _parse_command(d.pop("command"))

        def _parse_wait(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        wait = _parse_wait(d.pop("wait", UNSET))

        done_log = d.pop("done_log", UNSET)

        save_spec = cls(
            command=command,
            wait=wait,
            done_log=done_log,
        )

        save_spec.additional_properties = d
        return save_spec

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

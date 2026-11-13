from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_args import CommandArgs
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="CommandSend")


@_attrs_define
class CommandSend:
    """Give one of `command`, a saved command's `command_id` with its `args`, or a `line` sent through a connection
    (`via`).

        Attributes:
            command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command for
                the game server itself.
            command_id (str | Unset): A saved command in the version's game profile: see `commands` in GameProfile.
            args (CommandArgs | Unset): The saved command's arguments, by name. Values are strings, numbers included.
            line (str | Unset): A line to send as it is, through `via`.
            via (str | Unset): With `line`, a connection in the version's game profile. Default `console`.
            capture (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
    """

    command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    command_id: str | Unset = UNSET
    args: CommandArgs | Unset = UNSET
    line: str | Unset = UNSET
    via: str | Unset = UNSET
    capture: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        command: dict[str, Any] | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        elif (
            isinstance(self.command, GameCommandConsole)
            or isinstance(self.command, GameCommandRcon)
            or isinstance(self.command, GameCommandHttp)
        ):
            command = self.command.to_dict()
        else:
            command = self.command.to_dict()

        command_id = self.command_id

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        line = self.line

        via = self.via

        capture: int | str | Unset
        if isinstance(self.capture, Unset):
            capture = UNSET
        else:
            capture = self.capture

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if command_id is not UNSET:
            field_dict["command_id"] = command_id
        if args is not UNSET:
            field_dict["args"] = args
        if line is not UNSET:
            field_dict["line"] = line
        if via is not UNSET:
            field_dict["via"] = via
        if capture is not UNSET:
            field_dict["capture"] = capture

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.command_args import CommandArgs
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)

        def _parse_command(
            data: object,
        ) -> (
            GameCommandConsole
            | GameCommandHttp
            | GameCommandIsleRcon
            | GameCommandRcon
            | Unset
        ):
            if isinstance(data, Unset):
                return data
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

        command = _parse_command(d.pop("command", UNSET))

        command_id = d.pop("command_id", UNSET)

        _args = d.pop("args", UNSET)
        args: CommandArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = CommandArgs.from_dict(_args)

        line = d.pop("line", UNSET)

        via = d.pop("via", UNSET)

        def _parse_capture(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        capture = _parse_capture(d.pop("capture", UNSET))

        command_send = cls(
            command=command,
            command_id=command_id,
            args=args,
            line=line,
            via=via,
            capture=capture,
        )

        command_send.additional_properties = d
        return command_send

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

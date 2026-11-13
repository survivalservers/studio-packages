from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_spec_method import StopSpecMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="StopSpec")


@_attrs_define
class StopSpec:
    """
    Attributes:
        method (StopSpecMethod | Unset): Windows - `ctrl_break` (default), `ctrl_c` (delivered as Ctrl+Break, the same
            as `ctrl_break`), `wm_close`, `local_api`, `kill`. Linux - `sigterm` (default), `sigint`, `local_api`, `kill`.
            Either - `command`: sends `command` (a console line, an RCON command or an HTTP call, as servers such as
            Source's, Minecraft's or Palworld's want); if it cannot be delivered, the system's default signal goes instead
            and the timeline says `stop_command_failed`. Every stop sends the shutdown notice on the local API first (after
            the version's save, when it has one). A signal (`ctrl_break`, `ctrl_c`, `wm_close`, `sigterm`, `sigint`) is held
            back for a game that has asked for the notice during its run (`GET /v0/self/shutdown`, as the SDKs and engine
            add-ons do): it comes only if the game still runs halfway through `shutdown_time`. A game that never asks gets
            it at once.
        command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command for
            the game server itself.
        shutdown_time (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
    """

    method: StopSpecMethod | Unset = UNSET
    command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    shutdown_time: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

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

        shutdown_time: int | str | Unset
        if isinstance(self.shutdown_time, Unset):
            shutdown_time = UNSET
        else:
            shutdown_time = self.shutdown_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if command is not UNSET:
            field_dict["command"] = command
        if shutdown_time is not UNSET:
            field_dict["shutdown_time"] = shutdown_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: StopSpecMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = StopSpecMethod(_method)

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

        def _parse_shutdown_time(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        shutdown_time = _parse_shutdown_time(d.pop("shutdown_time", UNSET))

        stop_spec = cls(
            method=method,
            command=command,
            shutdown_time=shutdown_time,
        )

        stop_spec.additional_properties = d
        return stop_spec

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

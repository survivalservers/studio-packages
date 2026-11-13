from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_server_exit_reason import GameServerExitReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServerExit")


@_attrs_define
class GameServerExit:
    """Present once the game server has ended.

    Attributes:
        reason (GameServerExitReason): `restart`: a persistent server's run ended for its next run (its schedule, a
            restart asked for, or a new version applied now). `out_of_memory`: it went over its memory size and was stopped
            for it (Linux: killed at its size; Windows: refused memory past its size and ended); `crashed` is true too.
            `out_of_disk`: its own files went over 120% of its disk size (its build plus 10 GiB, or 50 GiB for a persistent
            server, and never less than its files held when its run began), or the machine's disk was nearly full and it had
            written the most since its run began; it was warned (`disk_high`) and then saved and stopped as any stop is,
            never killed outright, so `crashed` is false and it ends `stopped`.
        crashed (bool):
        killed (bool): True when the machine ended the program itself: it was still running when its stop's shutdown
            time ran out (the version's stop method or command did not end it, or the version stops with `kill`). `code` is
            then the machine's, not the game's own (Windows ends it with 1, Linux with 137), and the game had no chance to
            save on the way out. `reason` still says why it was stopped.
        code (int | None | Unset): The program's exit code. Windows: the unsigned 32-bit code as Windows reports it
            (3221225781 is 0xC0000135, a missing DLL); Linux: the code, or 128 plus the signal number when a signal ended
            it.
    """

    reason: GameServerExitReason
    crashed: bool
    killed: bool
    code: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        crashed = self.crashed

        killed = self.killed

        code: int | None | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "crashed": crashed,
                "killed": killed,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reason = GameServerExitReason(d.pop("reason"))

        crashed = d.pop("crashed")

        killed = d.pop("killed")

        def _parse_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        game_server_exit = cls(
            reason=reason,
            crashed=crashed,
            killed=killed,
            code=code,
        )

        game_server_exit.additional_properties = d
        return game_server_exit

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

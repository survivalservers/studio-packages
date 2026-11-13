from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_server_event_data_crash_reason import GameServerEventDataCrashReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServerEventDataCrash")


@_attrs_define
class GameServerEventDataCrash:
    """`game_server.restarted` only: how the run before this one ended, and whether it left a crash dump.

    Attributes:
        run (int): The run that crashed (the game server's first run is 1).
        reason (GameServerEventDataCrashReason): Why the run ended.
        crash_dump (bool): Whether the machine found a crash dump of it.
        exit_code (int | None | Unset): Its exit code (Linux: 128 plus the signal for a signal; Windows: the exception
            code for an exception, such as 3221225477 for 0xC0000005).
        signal (str | Unset): Linux: the signal that ended it, such as `SIGSEGV`. Absent for a plain exit code.
        exception (str | Unset): Windows: the exception that ended it, such as `STATUS_ACCESS_VIOLATION`. Absent for a
            plain exit code.
    """

    run: int
    reason: GameServerEventDataCrashReason
    crash_dump: bool
    exit_code: int | None | Unset = UNSET
    signal: str | Unset = UNSET
    exception: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run = self.run

        reason = self.reason.value

        crash_dump = self.crash_dump

        exit_code: int | None | Unset
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        signal = self.signal

        exception = self.exception

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run": run,
                "reason": reason,
                "crash_dump": crash_dump,
            }
        )
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if signal is not UNSET:
            field_dict["signal"] = signal
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        run = d.pop("run")

        reason = GameServerEventDataCrashReason(d.pop("reason"))

        crash_dump = d.pop("crash_dump")

        def _parse_exit_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exit_code = _parse_exit_code(d.pop("exit_code", UNSET))

        signal = d.pop("signal", UNSET)

        exception = d.pop("exception", UNSET)

        game_server_event_data_crash = cls(
            run=run,
            reason=reason,
            crash_dump=crash_dump,
            exit_code=exit_code,
            signal=signal,
            exception=exception,
        )

        game_server_event_data_crash.additional_properties = d
        return game_server_event_data_crash

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

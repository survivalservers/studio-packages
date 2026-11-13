from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeline_entry_type import TimelineEntryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeline_entry_data import TimelineEntryData


T = TypeVar("T", bound="TimelineEntry")


@_attrs_define
class TimelineEntry:
    """
    Attributes:
        seq (int):
        type_ (TimelineEntryType): A paused persistent server's run: `paused` with `data.then` `pause` or `stop` (again
            with `stop` when a paused one stops fully), `resuming`, then `resumed` with `data.from`, `paused` or `stopped`.
            A resume that may not bring a player (a packet nobody follows up, a scan) has `data.trial` on its `resuming` and
            `resumed`: the persistent server stays paused, that time is not billed as running, and no event or webhook goes
            out. When a player comes, a `resumed` with `data.trial_passed` follows and the persistent server is running from
            then; otherwise it pauses again the same way, and a `paused` step with `data.trial` says so. A `resuming` with
            `data.refused` (the reason) is such a resume refused for want of room on its machine: the persistent server
            stays paused where it is. `restarted` or `exited` with `data.stops_instead`: it exited by itself right after a
            resume, so the persistent server stops when empty instead of pausing (see `stops_instead` on the persistent
            server). `save_failed` (`data.reason`): the save command before a backup, a pause or a stop failed or ran out of
            time. `stop_command_failed` (`data.reason`): the stop command could not be delivered, so the default signal went
            instead. `exited` (`data.code`, `data.reason`, `data.crashed`, `data.killed`): `data.killed` is true when the
            machine killed it once its shutdown time ran out (see `killed` on the game server's `exit`). `memory_high`
            (`data.memory_mb`, `data.size_mb`, `data.since`): the run has used more than 90% of its memory size for over a
            minute; going over the size stops it. `disk_high` (`data.used_mb`, `data.size_mb`, `data.free_mb`,
            `data.since`): its own files have grown past its disk size, or it is about to be stopped as the biggest writer
            on a nearly full machine disk; going on to 120% of its size saves and stops it (`out_of_disk`).
            `simulated_players_changed` (`data.count`, `data.simulated`, `data.ended`): our own test setup only, simulated
            players set or ended; never real players. `update_held` (`data.version`, `data.reason`): this run started on the
            version the last one ran, because the backup at that run's stop was not stored, and the new version in
            `data.version` waits for the next restart. `backup_failed` (`data.kind`, `data.reason`, `data.detail`,
            `data.backup`): the machine could not make a backup (see `BackupFailure`); a scheduled or continuous one failing
            again the same way is a new step at most every 10 minutes. `restored_nothing` (`data.reason`): a persistent
            server that keeps saves moved to another machine with no backup to bring back (its machine was lost before its
            first backup was stored, or that backup is gone), so this run started on empty save folders. `process_ended`
            (`data.pid`, `data.program`): Windows only. The machine ended a process that ran as the studio's account outside
            all of its game servers there, one started through WMI, a scheduled task or a COM server, for example. No one
            game server started it, so the step is on each of the studio's game servers running on that machine.
            `data.program` is the program's file name, absent when Windows does not give it. `profile_written`
            (`data.files`, `data.folders`): Windows only, just before the run's `exited`. The run wrote files under the
            studio's Windows user profile, which all of the studio's game servers on that machine share: those files are not
            in save paths or backups and do not move with a persistent server. `data.folders` names up to five of their
            folders from inside the profile, such as `AppData\\LocalLow\\Acme\\Game`. Keep saves in the game server's folder
            with the game's own option. A start (`created` or `allocated`) and a `stop_requested` made through the API carry
            `data.by`, the key, member or AI agent that made it, and `data.ip`, the caller's address; those two steps are
            kept a year, the rest of the timeline 90 days after the game server ends.
        at (datetime.datetime):
        data (TimelineEntryData | Unset):
    """

    seq: int
    type_: TimelineEntryType
    at: datetime.datetime
    data: TimelineEntryData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        type_ = self.type_.value

        at = self.at.isoformat()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seq": seq,
                "type": type_,
                "at": at,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.timeline_entry_data import TimelineEntryData

        d = dict(src_dict)
        seq = d.pop("seq")

        type_ = TimelineEntryType(d.pop("type"))

        at = datetime.datetime.fromisoformat(d.pop("at"))

        _data = d.pop("data", UNSET)
        data: TimelineEntryData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TimelineEntryData.from_dict(_data)

        timeline_entry = cls(
            seq=seq,
            type_=type_,
            at=at,
            data=data,
        )

        timeline_entry.additional_properties = d
        return timeline_entry

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

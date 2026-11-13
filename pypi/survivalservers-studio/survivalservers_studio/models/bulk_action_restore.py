from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_kind import BackupKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_restore_skipped import BulkActionRestoreSkipped


T = TypeVar("T", bound="BulkActionRestore")


@_attrs_define
class BulkActionRestore:
    """The backup a rollback takes this target to.

    Attributes:
        backup (str): Backup ID.
        kind (BackupKind): `scheduled` is taken on the server's schedule, `stop` at each stop, `manual` when asked.
            `continuous` is copied within seconds of each game save; the newest 3 are kept, apart from your other backups,
            and a persistent server that loses its machine starts again from the newest. `before_restore` is how it was just
            before a restore or rollback, which an undo goes back to. `before_update` is the backup taken at the stop before
            a new version started: the old version's last save, kept 30 days like `before_restore`. `imported` is a save you
            uploaded. `recovered` holds newer saves found on a machine that came back after its persistent server moved.
        saved_at (datetime.datetime): How recent the game state in it is.
        play_lost (int | str): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        bytes_ (int | Unset): The size of the saves in it.
        version (None | str | Unset): The version it ran on.
        restores_version (bool | Unset): That version goes back with the saves.
        skipped (BulkActionRestoreSkipped | Unset): By time, when the backup used is not the newest from before the time
            asked: that newer one. Within a minute, a backup the game saved for or taken at a stop is used over a newer copy
            of the same run.
        note (str | Unset): In plain words, the backup used when a newer one was skipped, or when no backup was kept at
            the stop before an update.
        caution (str | Unset): Set when this backup holds no saves, holds under half of what the server's newest backup
            holds, or is partial (files the game held locked were left out of it, and restoring it leaves them out).
    """

    backup: str
    kind: BackupKind
    saved_at: datetime.datetime
    play_lost: int | str
    bytes_: int | Unset = UNSET
    version: None | str | Unset = UNSET
    restores_version: bool | Unset = UNSET
    skipped: BulkActionRestoreSkipped | Unset = UNSET
    note: str | Unset = UNSET
    caution: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup = self.backup

        kind = self.kind.value

        saved_at = self.saved_at.isoformat()

        play_lost: int | str
        play_lost = self.play_lost

        bytes_ = self.bytes_

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        restores_version = self.restores_version

        skipped: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = self.skipped.to_dict()

        note = self.note

        caution = self.caution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup": backup,
                "kind": kind,
                "saved_at": saved_at,
                "play_lost": play_lost,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if version is not UNSET:
            field_dict["version"] = version
        if restores_version is not UNSET:
            field_dict["restores_version"] = restores_version
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if note is not UNSET:
            field_dict["note"] = note
        if caution is not UNSET:
            field_dict["caution"] = caution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_restore_skipped import BulkActionRestoreSkipped

        d = dict(src_dict)
        backup = d.pop("backup")

        kind = BackupKind(d.pop("kind"))

        saved_at = datetime.datetime.fromisoformat(d.pop("saved_at"))

        def _parse_play_lost(data: object) -> int | str:
            return cast(int | str, data)

        play_lost = _parse_play_lost(d.pop("play_lost"))

        bytes_ = d.pop("bytes", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        restores_version = d.pop("restores_version", UNSET)

        _skipped = d.pop("skipped", UNSET)
        skipped: BulkActionRestoreSkipped | Unset
        if isinstance(_skipped, Unset):
            skipped = UNSET
        else:
            skipped = BulkActionRestoreSkipped.from_dict(_skipped)

        note = d.pop("note", UNSET)

        caution = d.pop("caution", UNSET)

        bulk_action_restore = cls(
            backup=backup,
            kind=kind,
            saved_at=saved_at,
            play_lost=play_lost,
            bytes_=bytes_,
            version=version,
            restores_version=restores_version,
            skipped=skipped,
            note=note,
            caution=caution,
        )

        bulk_action_restore.additional_properties = d
        return bulk_action_restore

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_check import BackupCheck
from ..models.backup_kind import BackupKind
from ..models.backup_status import BackupStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_failure import BackupFailure


T = TypeVar("T", bound="Backup")


@_attrs_define
class Backup:
    """
    Attributes:
        id (str): Backup ID.
        persistent_server (str): Persistent server ID.
        kind (BackupKind): `scheduled` is taken on the server's schedule, `stop` at each stop, `manual` when asked.
            `continuous` is copied within seconds of each game save; the newest 3 are kept, apart from your other backups,
            and a persistent server that loses its machine starts again from the newest. `before_restore` is how it was just
            before a restore or rollback, which an undo goes back to. `before_update` is the backup taken at the stop before
            a new version started: the old version's last save, kept 30 days like `before_restore`. `imported` is a save you
            uploaded. `recovered` holds newer saves found on a machine that came back after its persistent server moved.
        status (BackupStatus):
        created_at (datetime.datetime): When it was made.
        bytes_ (int | Unset):
        added_bytes (int | Unset): What this backup added to the persistent server's stored backups. Most of a backup is
            shared with the ones before it.
        offsite (bool | Unset): Its second copy is stored too
        locked (bool | Unset): It stays until you unlock and delete it.
        label (None | str | Unset): Your name for it, such as `Season 3 end`.
        kept_by_game (bool | Unset): The game itself asked to keep it. While locked it counts toward the 20 a game can
            keep of one server; past that a save is an ordinary backup and `persistent_server.keep_limit_reached` fires, at
            most once a day.
        check (BackupCheck | Unset): `passed`: restored into a scratch folder and every file matched. `failed`: it did
            not come back whole. `smaller`: under half the size of the backup before it, which is what a backup with no save
            inside looks like. `backup.check_failed` fires for the last two.
        checked_at (datetime.datetime | None | Unset): When that check ended.
        saved_at (datetime.datetime | None | Unset): The newest write among its files
        version (str | Unset): Version name, unique in its app, for example `2.3.1`.
        failure (BackupFailure | Unset): Why a backup failed. A run of the same failure on one run is one failed backup:
            `times` counts the tries and `last_at` is the newest.
        left_out (list[str] | Unset): Save files left out because the game held them locked while they were copied
            (Windows), by their path in the backup, at most 20 named. A file named `*.lock` under 1 KB that the game holds
            is its own in-use marker, such as Minecraft's `session.lock`, with no save data: it is named here, but the
            backup is still whole. Absent when nothing was left out.
        left_out_count (int | Unset): How many files were left out, named or not. Absent when none.
        partial (bool | Unset): A file left out holds save data, so this backup is not whole: restoring it leaves those
            files out of the persistent server. Present and true only then.
        expires_at (datetime.datetime | None | Unset): When it expires.
    """

    id: str
    persistent_server: str
    kind: BackupKind
    status: BackupStatus
    created_at: datetime.datetime
    bytes_: int | Unset = UNSET
    added_bytes: int | Unset = UNSET
    offsite: bool | Unset = UNSET
    locked: bool | Unset = UNSET
    label: None | str | Unset = UNSET
    kept_by_game: bool | Unset = UNSET
    check: BackupCheck | Unset = UNSET
    checked_at: datetime.datetime | None | Unset = UNSET
    saved_at: datetime.datetime | None | Unset = UNSET
    version: str | Unset = UNSET
    failure: BackupFailure | Unset = UNSET
    left_out: list[str] | Unset = UNSET
    left_out_count: int | Unset = UNSET
    partial: bool | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        persistent_server = self.persistent_server

        kind = self.kind.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        bytes_ = self.bytes_

        added_bytes = self.added_bytes

        offsite = self.offsite

        locked = self.locked

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        kept_by_game = self.kept_by_game

        check: str | Unset = UNSET
        if not isinstance(self.check, Unset):
            check = self.check.value

        checked_at: None | str | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        elif isinstance(self.checked_at, datetime.datetime):
            checked_at = self.checked_at.isoformat()
        else:
            checked_at = self.checked_at

        saved_at: None | str | Unset
        if isinstance(self.saved_at, Unset):
            saved_at = UNSET
        elif isinstance(self.saved_at, datetime.datetime):
            saved_at = self.saved_at.isoformat()
        else:
            saved_at = self.saved_at

        version = self.version

        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        left_out: list[str] | Unset = UNSET
        if not isinstance(self.left_out, Unset):
            left_out = self.left_out

        left_out_count = self.left_out_count

        partial = self.partial

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "persistent_server": persistent_server,
                "kind": kind,
                "status": status,
                "created_at": created_at,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if added_bytes is not UNSET:
            field_dict["added_bytes"] = added_bytes
        if offsite is not UNSET:
            field_dict["offsite"] = offsite
        if locked is not UNSET:
            field_dict["locked"] = locked
        if label is not UNSET:
            field_dict["label"] = label
        if kept_by_game is not UNSET:
            field_dict["kept_by_game"] = kept_by_game
        if check is not UNSET:
            field_dict["check"] = check
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if saved_at is not UNSET:
            field_dict["saved_at"] = saved_at
        if version is not UNSET:
            field_dict["version"] = version
        if failure is not UNSET:
            field_dict["failure"] = failure
        if left_out is not UNSET:
            field_dict["left_out"] = left_out
        if left_out_count is not UNSET:
            field_dict["left_out_count"] = left_out_count
        if partial is not UNSET:
            field_dict["partial"] = partial
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_failure import BackupFailure

        d = dict(src_dict)
        id = d.pop("id")

        persistent_server = d.pop("persistent_server")

        kind = BackupKind(d.pop("kind"))

        status = BackupStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        bytes_ = d.pop("bytes", UNSET)

        added_bytes = d.pop("added_bytes", UNSET)

        offsite = d.pop("offsite", UNSET)

        locked = d.pop("locked", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        kept_by_game = d.pop("kept_by_game", UNSET)

        _check = d.pop("check", UNSET)
        check: BackupCheck | Unset
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = BackupCheck(_check)

        def _parse_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checked_at", UNSET))

        def _parse_saved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                saved_at_type_0 = datetime.datetime.fromisoformat(data)

                return saved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        saved_at = _parse_saved_at(d.pop("saved_at", UNSET))

        version = d.pop("version", UNSET)

        _failure = d.pop("failure", UNSET)
        failure: BackupFailure | Unset
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = BackupFailure.from_dict(_failure)

        left_out = cast(list[str], d.pop("left_out", UNSET))

        left_out_count = d.pop("left_out_count", UNSET)

        partial = d.pop("partial", UNSET)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        backup = cls(
            id=id,
            persistent_server=persistent_server,
            kind=kind,
            status=status,
            created_at=created_at,
            bytes_=bytes_,
            added_bytes=added_bytes,
            offsite=offsite,
            locked=locked,
            label=label,
            kept_by_game=kept_by_game,
            check=check,
            checked_at=checked_at,
            saved_at=saved_at,
            version=version,
            failure=failure,
            left_out=left_out,
            left_out_count=left_out_count,
            partial=partial,
            expires_at=expires_at,
        )

        backup.additional_properties = d
        return backup

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

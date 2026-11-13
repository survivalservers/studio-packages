from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_kind import BackupKind

T = TypeVar("T", bound="BulkActionRestoreSkipped")


@_attrs_define
class BulkActionRestoreSkipped:
    """By time, when the backup used is not the newest from before the time asked: that newer one. Within a minute, a
    backup the game saved for or taken at a stop is used over a newer copy of the same run.

        Attributes:
            backup (str): Backup ID.
            kind (BackupKind): `scheduled` is taken on the server's schedule, `stop` at each stop, `manual` when asked.
                `continuous` is copied within seconds of each game save; the newest 3 are kept, apart from your other backups,
                and a persistent server that loses its machine starts again from the newest. `before_restore` is how it was just
                before a restore or rollback, which an undo goes back to. `before_update` is the backup taken at the stop before
                a new version started: the old version's last save, kept 30 days like `before_restore`. `imported` is a save you
                uploaded. `recovered` holds newer saves found on a machine that came back after its persistent server moved.
            saved_at (datetime.datetime):
    """

    backup: str
    kind: BackupKind
    saved_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup = self.backup

        kind = self.kind.value

        saved_at = self.saved_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup": backup,
                "kind": kind,
                "saved_at": saved_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup = d.pop("backup")

        kind = BackupKind(d.pop("kind"))

        saved_at = datetime.datetime.fromisoformat(d.pop("saved_at"))

        bulk_action_restore_skipped = cls(
            backup=backup,
            kind=kind,
            saved_at=saved_at,
        )

        bulk_action_restore_skipped.additional_properties = d
        return bulk_action_restore_skipped

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

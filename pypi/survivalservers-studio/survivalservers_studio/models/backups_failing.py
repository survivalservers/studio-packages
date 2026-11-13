from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_failure_reason import BackupFailureReason

T = TypeVar("T", bound="BackupsFailing")


@_attrs_define
class BackupsFailing:
    """The persistent server's backups are failing: its last tries failed and none has been stored since. It clears once a
    backup is stored. `persistent_server.backup_failed` fires when it begins, then at most once a day while it lasts.

        Attributes:
            since (datetime.datetime): When the first of them failed.
            failures (int): Failed tries in a row.
            reason (BackupFailureReason): `too_big`: the saves are over 32 GiB or 200,000 files, the most a backup holds.
                `locked_file`: the game held every save file locked, so nothing could be copied. `read_error`: a save file could
                not be read. `disk_full`: the machine had no room to write the backup, which is ours to fix. `machine_error`:
                anything else on the machine. New reasons may be added (section 1.1).
            detail (str): The newest failure in plain words.
    """

    since: datetime.datetime
    failures: int
    reason: BackupFailureReason
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        since = self.since.isoformat()

        failures = self.failures

        reason = self.reason.value

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "since": since,
                "failures": failures,
                "reason": reason,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        since = datetime.datetime.fromisoformat(d.pop("since"))

        failures = d.pop("failures")

        reason = BackupFailureReason(d.pop("reason"))

        detail = d.pop("detail")

        backups_failing = cls(
            since=since,
            failures=failures,
            reason=reason,
            detail=detail,
        )

        backups_failing.additional_properties = d
        return backups_failing

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_failure_reason import BackupFailureReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupFailure")


@_attrs_define
class BackupFailure:
    """Why a backup failed. A run of the same failure on one run is one failed backup: `times` counts the tries and
    `last_at` is the newest.

        Attributes:
            reason (BackupFailureReason): `too_big`: the saves are over 32 GiB or 200,000 files, the most a backup holds.
                `locked_file`: the game held every save file locked, so nothing could be copied. `read_error`: a save file could
                not be read. `disk_full`: the machine had no room to write the backup, which is ours to fix. `machine_error`:
                anything else on the machine. New reasons may be added (section 1.1).
            detail (str): The reason in plain words, naming save files by their path in the backup.
            times (int): How many tries failed this way.
            last_at (datetime.datetime | None | Unset): When the newest of them failed.
    """

    reason: BackupFailureReason
    detail: str
    times: int
    last_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        detail = self.detail

        times = self.times

        last_at: None | str | Unset
        if isinstance(self.last_at, Unset):
            last_at = UNSET
        elif isinstance(self.last_at, datetime.datetime):
            last_at = self.last_at.isoformat()
        else:
            last_at = self.last_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "detail": detail,
                "times": times,
            }
        )
        if last_at is not UNSET:
            field_dict["last_at"] = last_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reason = BackupFailureReason(d.pop("reason"))

        detail = d.pop("detail")

        times = d.pop("times")

        def _parse_last_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_at = _parse_last_at(d.pop("last_at", UNSET))

        backup_failure = cls(
            reason=reason,
            detail=detail,
            times=times,
            last_at=last_at,
        )

        backup_failure.additional_properties = d
        return backup_failure

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_policy_keep_for import BackupPolicyKeepFor
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupPolicy")


@_attrs_define
class BackupPolicy:
    """
    Attributes:
        every (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        keep_for (BackupPolicyKeepFor | Unset): How long backups are kept. `7d`: any 10 minutes in the last 6 hours, any
            hour in the last 2 days, any day in the last week. `30d`: any 10 minutes in the last 6 hours, any hour in the
            last 2 days, any day in the last 30 days. `1y`: the same, then any week in the last 3 months and any month in
            the last year. Backups by hand, imported and locked ones stay until you delete them. Default:
            BackupPolicyKeepFor.VALUE_1.
    """

    every: int | str | Unset = UNSET
    keep_for: BackupPolicyKeepFor | Unset = BackupPolicyKeepFor.VALUE_1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        every: int | str | Unset
        if isinstance(self.every, Unset):
            every = UNSET
        else:
            every = self.every

        keep_for: str | Unset = UNSET
        if not isinstance(self.keep_for, Unset):
            keep_for = self.keep_for.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if every is not UNSET:
            field_dict["every"] = every
        if keep_for is not UNSET:
            field_dict["keep_for"] = keep_for

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_every(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        every = _parse_every(d.pop("every", UNSET))

        _keep_for = d.pop("keep_for", UNSET)
        keep_for: BackupPolicyKeepFor | Unset
        if isinstance(_keep_for, Unset):
            keep_for = UNSET
        else:
            keep_for = BackupPolicyKeepFor(_keep_for)

        backup_policy = cls(
            every=every,
            keep_for=keep_for,
        )

        backup_policy.additional_properties = d
        return backup_policy

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

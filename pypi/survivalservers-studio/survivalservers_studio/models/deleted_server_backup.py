from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup import Backup


T = TypeVar("T", bound="DeletedServerBackup")


@_attrs_define
class DeletedServerBackup:
    """
    Attributes:
        name (str): The deleted server's name.
        deleted_at (datetime.datetime):
        backup (Backup):
    """

    name: str
    deleted_at: datetime.datetime
    backup: Backup
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        deleted_at = self.deleted_at.isoformat()

        backup = self.backup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "deleted_at": deleted_at,
                "backup": backup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup import Backup

        d = dict(src_dict)
        name = d.pop("name")

        deleted_at = datetime.datetime.fromisoformat(d.pop("deleted_at"))

        backup = Backup.from_dict(d.pop("backup"))

        deleted_server_backup = cls(
            name=name,
            deleted_at=deleted_at,
            backup=backup,
        )

        deleted_server_backup.additional_properties = d
        return deleted_server_backup

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

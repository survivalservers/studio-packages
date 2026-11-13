from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_export_status import BackupExportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupExport")


@_attrs_define
class BackupExport:
    """
    Attributes:
        backup (str): Backup ID.
        status (BackupExportStatus):
        expires_at (datetime.datetime): When the zip is removed.
        url (str | Unset): The zip. Good until `url_expires_at`; ask again for a fresh one.
        url_expires_at (datetime.datetime | Unset):
        bytes_ (int | Unset):
        error (str | Unset): Why it could not be built.
    """

    backup: str
    status: BackupExportStatus
    expires_at: datetime.datetime
    url: str | Unset = UNSET
    url_expires_at: datetime.datetime | Unset = UNSET
    bytes_: int | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup = self.backup

        status = self.status.value

        expires_at = self.expires_at.isoformat()

        url = self.url

        url_expires_at: str | Unset = UNSET
        if not isinstance(self.url_expires_at, Unset):
            url_expires_at = self.url_expires_at.isoformat()

        bytes_ = self.bytes_

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup": backup,
                "status": status,
                "expires_at": expires_at,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if url_expires_at is not UNSET:
            field_dict["url_expires_at"] = url_expires_at
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup = d.pop("backup")

        status = BackupExportStatus(d.pop("status"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        url = d.pop("url", UNSET)

        _url_expires_at = d.pop("url_expires_at", UNSET)
        url_expires_at: datetime.datetime | Unset
        if isinstance(_url_expires_at, Unset):
            url_expires_at = UNSET
        else:
            url_expires_at = datetime.datetime.fromisoformat(_url_expires_at)

        bytes_ = d.pop("bytes", UNSET)

        error = d.pop("error", UNSET)

        backup_export = cls(
            backup=backup,
            status=status,
            expires_at=expires_at,
            url=url,
            url_expires_at=url_expires_at,
            bytes_=bytes_,
            error=error,
        )

        backup_export.additional_properties = d
        return backup_export

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

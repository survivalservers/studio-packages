from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_upload_status import BackupUploadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupUpload")


@_attrs_define
class BackupUpload:
    """
    Attributes:
        id (str): Persistent server file upload ID.
        bytes_ (int):
        status (BackupUploadStatus):
        expires_at (datetime.datetime): When the link stops working.
        url (str | Unset): `PUT` the zip here.
        backup (str | Unset): Backup ID.
        error (None | str | Unset): Why it could not be taken.
    """

    id: str
    bytes_: int
    status: BackupUploadStatus
    expires_at: datetime.datetime
    url: str | Unset = UNSET
    backup: str | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        bytes_ = self.bytes_

        status = self.status.value

        expires_at = self.expires_at.isoformat()

        url = self.url

        backup = self.backup

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bytes": bytes_,
                "status": status,
                "expires_at": expires_at,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if backup is not UNSET:
            field_dict["backup"] = backup
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        bytes_ = d.pop("bytes")

        status = BackupUploadStatus(d.pop("status"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        url = d.pop("url", UNSET)

        backup = d.pop("backup", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        backup_upload = cls(
            id=id,
            bytes_=bytes_,
            status=status,
            expires_at=expires_at,
            url=url,
            backup=backup,
            error=error,
        )

        backup_upload.additional_properties = d
        return backup_upload

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

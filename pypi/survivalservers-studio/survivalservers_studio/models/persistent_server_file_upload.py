from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persistent_server_file_upload_status import (
    PersistentServerFileUploadStatus,
)

T = TypeVar("T", bound="PersistentServerFileUpload")


@_attrs_define
class PersistentServerFileUpload:
    """
    Attributes:
        id (str): Persistent server file upload ID.
        path (str):
        bytes_ (int):
        status (PersistentServerFileUploadStatus):
        url (str): `PUT` the bytes here.
        expires_at (datetime.datetime): When it expires.
    """

    id: str
    path: str
    bytes_: int
    status: PersistentServerFileUploadStatus
    url: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path = self.path

        bytes_ = self.bytes_

        status = self.status.value

        url = self.url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "path": path,
                "bytes": bytes_,
                "status": status,
                "url": url,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        path = d.pop("path")

        bytes_ = d.pop("bytes")

        status = PersistentServerFileUploadStatus(d.pop("status"))

        url = d.pop("url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        persistent_server_file_upload = cls(
            id=id,
            path=path,
            bytes_=bytes_,
            status=status,
            url=url,
            expires_at=expires_at,
        )

        persistent_server_file_upload.additional_properties = d
        return persistent_server_file_upload

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

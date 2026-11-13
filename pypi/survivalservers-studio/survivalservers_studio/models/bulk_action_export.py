from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkActionExport")


@_attrs_define
class BulkActionExport:
    """A bulk export's zip of one server. `url` is there once it is ready, for a caller who can read backups.

    Attributes:
        backup (str): Backup ID.
        saved_at (datetime.datetime): The time of the game state in it.
        url (str | Unset): The zip. Good until `url_expires_at`; read the target again for a fresh one.
        url_expires_at (datetime.datetime | Unset):
        bytes_ (int | Unset):
    """

    backup: str
    saved_at: datetime.datetime
    url: str | Unset = UNSET
    url_expires_at: datetime.datetime | Unset = UNSET
    bytes_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup = self.backup

        saved_at = self.saved_at.isoformat()

        url = self.url

        url_expires_at: str | Unset = UNSET
        if not isinstance(self.url_expires_at, Unset):
            url_expires_at = self.url_expires_at.isoformat()

        bytes_ = self.bytes_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup": backup,
                "saved_at": saved_at,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if url_expires_at is not UNSET:
            field_dict["url_expires_at"] = url_expires_at
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup = d.pop("backup")

        saved_at = datetime.datetime.fromisoformat(d.pop("saved_at"))

        url = d.pop("url", UNSET)

        _url_expires_at = d.pop("url_expires_at", UNSET)
        url_expires_at: datetime.datetime | Unset
        if isinstance(_url_expires_at, Unset):
            url_expires_at = UNSET
        else:
            url_expires_at = datetime.datetime.fromisoformat(_url_expires_at)

        bytes_ = d.pop("bytes", UNSET)

        bulk_action_export = cls(
            backup=backup,
            saved_at=saved_at,
            url=url,
            url_expires_at=url_expires_at,
            bytes_=bytes_,
        )

        bulk_action_export.additional_properties = d
        return bulk_action_export

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

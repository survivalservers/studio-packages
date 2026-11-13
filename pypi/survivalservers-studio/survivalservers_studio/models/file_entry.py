from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_entry_type import FileEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileEntry")


@_attrs_define
class FileEntry:
    """
    Attributes:
        name (str): Its name.
        path (str): Its path as the game sees it: what the list, download and upload calls take.
        type_ (FileEntryType):
        bytes_ (int | Unset):
        modified_at (datetime.datetime | Unset):
    """

    name: str
    path: str
    type_: FileEntryType
    bytes_: int | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        type_ = self.type_.value

        bytes_ = self.bytes_

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "type": type_,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if modified_at is not UNSET:
            field_dict["modified_at"] = modified_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        type_ = FileEntryType(d.pop("type"))

        bytes_ = d.pop("bytes", UNSET)

        _modified_at = d.pop("modified_at", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = datetime.datetime.fromisoformat(_modified_at)

        file_entry = cls(
            name=name,
            path=path,
            type_=type_,
            bytes_=bytes_,
            modified_at=modified_at,
        )

        file_entry.additional_properties = d
        return file_entry

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

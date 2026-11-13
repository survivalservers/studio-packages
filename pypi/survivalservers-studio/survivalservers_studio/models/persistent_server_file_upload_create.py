from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersistentServerFileUploadCreate")


@_attrs_define
class PersistentServerFileUploadCreate:
    """
    Attributes:
        path (str): Where the file goes, as the game sees it, in the same form as the listing's `path`. In a Linux image
            it must be inside one of the persistent server's save paths (`/opt/game/Servers/MyServer/Server/Commands.dat`).
        bytes_ (int):
        sha256 (str):
    """

    path: str
    bytes_: int
    sha256: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        bytes_ = self.bytes_

        sha256 = self.sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "bytes": bytes_,
                "sha256": sha256,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        bytes_ = d.pop("bytes")

        sha256 = d.pop("sha256")

        persistent_server_file_upload_create = cls(
            path=path,
            bytes_=bytes_,
            sha256=sha256,
        )

        persistent_server_file_upload_create.additional_properties = d
        return persistent_server_file_upload_create

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

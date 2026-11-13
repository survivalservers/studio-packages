from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_source_type import UploadSourceType

T = TypeVar("T", bound="UploadSource")


@_attrs_define
class UploadSource:
    """A zip uploaded in parts (Windows).

    Attributes:
        type_ (UploadSourceType):
        filename (str):
        bytes_ (int): At most your studio's zip limit (`GET /v0/studio`).
        sha256 (str):
    """

    type_: UploadSourceType
    filename: str
    bytes_: int
    sha256: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        filename = self.filename

        bytes_ = self.bytes_

        sha256 = self.sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "filename": filename,
                "bytes": bytes_,
                "sha256": sha256,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = UploadSourceType(d.pop("type"))

        filename = d.pop("filename")

        bytes_ = d.pop("bytes")

        sha256 = d.pop("sha256")

        upload_source = cls(
            type_=type_,
            filename=filename,
            bytes_=bytes_,
            sha256=sha256,
        )

        upload_source.additional_properties = d
        return upload_source

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

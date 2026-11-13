from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.profile_config_file_format import ProfileConfigFileFormat

T = TypeVar("T", bound="ProfileConfigFile")


@_attrs_define
class ProfileConfigFile:
    """
    Attributes:
        id (str): What a setting's `at.file` calls it.
        path (str): Windows: relative to the top of the build. Linux: an absolute path in one of the server's save
            paths.
        format_ (ProfileConfigFileFormat): The file's format. `ini` covers Unreal's files too, `cfg` is Source's `key
            "value"`.
    """

    id: str
    path: str
    format_: ProfileConfigFileFormat

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path = self.path

        format_ = self.format_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "path": path,
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        path = d.pop("path")

        format_ = ProfileConfigFileFormat(d.pop("format"))

        profile_config_file = cls(
            id=id,
            path=path,
            format_=format_,
        )

        return profile_config_file

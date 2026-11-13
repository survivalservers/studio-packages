from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LaunchFile")


@_attrs_define
class LaunchFile:
    """
    Attributes:
        path (str): Where the file goes. Windows builds: relative to the build's top folder. Linux images: an absolute
            path inside the container. No `..`.
        content (str): Text, written as UTF-8, with the templates of `args` filled in.
    """

    path: str
    content: str

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        content = d.pop("content")

        launch_file = cls(
            path=path,
            content=content,
        )

        return launch_file

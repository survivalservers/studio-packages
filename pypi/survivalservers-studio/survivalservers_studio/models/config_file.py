from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigFile")


@_attrs_define
class ConfigFile:
    """
    Attributes:
        path (str): Where it is written before every run. Windows builds: relative to the build's top folder. Linux
            images: an absolute path inside one of the persistent server's save paths. No `..`.
        content (str): Text, written as UTF-8. `{{server.name}}`, `{{server.id}}`, `{{region}}` and `{{label.<key>}}`
            are replaced for each persistent server.
    """

    path: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        config_file = cls(
            path=path,
            content=content,
        )

        config_file.additional_properties = d
        return config_file

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

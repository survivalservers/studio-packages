from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_file_change_change import ConfigFileChangeChange
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigFileChange")


@_attrs_define
class ConfigFileChange:
    """
    Attributes:
        path (str): The file.
        change (ConfigFileChangeChange):
        diff (str | Unset): A unified line diff, up to 64 KiB.
    """

    path: str
    change: ConfigFileChangeChange
    diff: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        change = self.change.value

        diff = self.diff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "change": change,
            }
        )
        if diff is not UNSET:
            field_dict["diff"] = diff

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        change = ConfigFileChangeChange(d.pop("change"))

        diff = d.pop("diff", UNSET)

        config_file_change = cls(
            path=path,
            change=change,
            diff=diff,
        )

        config_file_change.additional_properties = d
        return config_file_change

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigChangeOverriddenItem")


@_attrs_define
class ConfigChangeOverriddenItem:
    """
    Attributes:
        name (str): The variable.
        persistent_servers (int): Persistent servers that set it.
    """

    name: str
    persistent_servers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        persistent_servers = self.persistent_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "persistent_servers": persistent_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        persistent_servers = d.pop("persistent_servers")

        config_change_overridden_item = cls(
            name=name,
            persistent_servers=persistent_servers,
        )

        config_change_overridden_item.additional_properties = d
        return config_change_overridden_item

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProfileTemplatePort")


@_attrs_define
class ProfileTemplatePort:
    """
    Attributes:
        name (str): The port name the profile uses. Your version must have it.
        protocol (str): `tcp` or `udp`.
        why (str): What it is for.
    """

    name: str
    protocol: str
    why: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        protocol = self.protocol

        why = self.why

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "protocol": protocol,
                "why": why,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        protocol = d.pop("protocol")

        why = d.pop("why")

        profile_template_port = cls(
            name=name,
            protocol=protocol,
            why=why,
        )

        profile_template_port.additional_properties = d
        return profile_template_port

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

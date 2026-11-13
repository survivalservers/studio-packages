from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ready_check_port_type import ReadyCheckPortType

T = TypeVar("T", bound="ReadyCheckPort")


@_attrs_define
class ReadyCheckPort:
    """The process has bound this named port.

    Attributes:
        type_ (ReadyCheckPortType):
        port (str):
    """

    type_: ReadyCheckPortType
    port: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ReadyCheckPortType(d.pop("type"))

        port = d.pop("port")

        ready_check_port = cls(
            type_=type_,
            port=port,
        )

        ready_check_port.additional_properties = d
        return ready_check_port

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

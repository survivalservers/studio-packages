from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineCreate")


@_attrs_define
class MachineCreate:
    """
    Attributes:
        name (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        os (Os):
        public_ipv4 (str | Unset):
        public_ipv6 (str | Unset):
    """

    name: str
    region: str
    os: Os
    public_ipv4: str | Unset = UNSET
    public_ipv6: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        region = self.region

        os = self.os.value

        public_ipv4 = self.public_ipv4

        public_ipv6 = self.public_ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "region": region,
                "os": os,
            }
        )
        if public_ipv4 is not UNSET:
            field_dict["public_ipv4"] = public_ipv4
        if public_ipv6 is not UNSET:
            field_dict["public_ipv6"] = public_ipv6

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        region = d.pop("region")

        os = Os(d.pop("os"))

        public_ipv4 = d.pop("public_ipv4", UNSET)

        public_ipv6 = d.pop("public_ipv6", UNSET)

        machine_create = cls(
            name=name,
            region=region,
            os=os,
            public_ipv4=public_ipv4,
            public_ipv6=public_ipv6,
        )

        machine_create.additional_properties = d
        return machine_create

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

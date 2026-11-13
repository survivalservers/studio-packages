from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.address_ports import AddressPorts


T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """Final at the reply; players can be sent at once.

    Attributes:
        ipv4 (None | str):
        ipv6 (None | str):
        ports (AddressPorts): Public port per named port. Admin ports (`port_policy` `none`) are never here.
    """

    ipv4: None | str
    ipv6: None | str
    ports: AddressPorts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv4: None | str
        ipv4 = self.ipv4

        ipv6: None | str
        ipv6 = self.ipv6

        ports = self.ports.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv4": ipv4,
                "ipv6": ipv6,
                "ports": ports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.address_ports import AddressPorts

        d = dict(src_dict)

        def _parse_ipv4(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ipv4 = _parse_ipv4(d.pop("ipv4"))

        def _parse_ipv6(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ipv6 = _parse_ipv6(d.pop("ipv6"))

        ports = AddressPorts.from_dict(d.pop("ports"))

        address = cls(
            ipv4=ipv4,
            ipv6=ipv6,
            ports=ports,
        )

        address.additional_properties = d
        return address

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

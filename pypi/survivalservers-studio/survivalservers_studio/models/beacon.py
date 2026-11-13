from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Beacon")


@_attrs_define
class Beacon:
    """A region's ping beacon. It echoes UDP datagrams up to 64 bytes, accepts TCP connects and answers ICMP ping. Measure
    each region that has one (median of 5). A region with no beacon leaves `beacon` out; send `player_ips` with a start
    instead.

        Attributes:
            host (str):
            udp_port (int):
            tcp_port (int):
    """

    host: str
    udp_port: int
    tcp_port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        udp_port = self.udp_port

        tcp_port = self.tcp_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "udp_port": udp_port,
                "tcp_port": tcp_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        host = d.pop("host")

        udp_port = d.pop("udp_port")

        tcp_port = d.pop("tcp_port")

        beacon = cls(
            host=host,
            udp_port=udp_port,
            tcp_port=tcp_port,
        )

        beacon.additional_properties = d
        return beacon

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

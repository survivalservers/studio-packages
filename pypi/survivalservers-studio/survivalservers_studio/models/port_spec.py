from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.port_spec_port_policy import PortSpecPortPolicy
from ..models.protocol import Protocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PortSpec")


@_attrs_define
class PortSpec:
    """
    Attributes:
        name (str):
        protocol (Protocol):
        container_port (int | Unset): Linux - the port the image listens on; the public port is mapped onto it. Required
            on Linux, except for a `passthrough` port, which has none.
        port_policy (PortSpecPortPolicy | Unset): `dynamic` (the default): a public port, a fresh one from the machine's
            game port range on every start, in the game server's address. `none`: an admin port, for RCON or a web admin
            page. It is never opened to the internet and never in the address; only the game server's own machine reaches
            it, which is how the panel's console and players card and RCON or HTTP stop and save commands reach the game.
            Windows - the game listens on `{{port.<name>}}`, a number from the machine's game port range that the firewall
            never opens. Linux - the game listens on its `container_port` inside its own container, and nothing on the
            machine forwards to it. `passthrough` (Linux images only): a public port, like `dynamic`, whose number inside
            the container is the same as the public one, so a game that tells Steam's server list (or any other list) its
            own port tells it the one players reach. The game listens on `{{port.<name>}}` (or `GS_PORT_<NAME>`), a
            different number for each game server, so the port has no `container_port`. Agones uses the same names:
            `portPolicy: None` for a port with no public port, `Passthrough` for this one.
    """

    name: str
    protocol: Protocol
    container_port: int | Unset = UNSET
    port_policy: PortSpecPortPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        protocol = self.protocol.value

        container_port = self.container_port

        port_policy: str | Unset = UNSET
        if not isinstance(self.port_policy, Unset):
            port_policy = self.port_policy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "protocol": protocol,
            }
        )
        if container_port is not UNSET:
            field_dict["container_port"] = container_port
        if port_policy is not UNSET:
            field_dict["port_policy"] = port_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        protocol = Protocol(d.pop("protocol"))

        container_port = d.pop("container_port", UNSET)

        _port_policy = d.pop("port_policy", UNSET)
        port_policy: PortSpecPortPolicy | Unset
        if isinstance(_port_policy, Unset):
            port_policy = UNSET
        else:
            port_policy = PortSpecPortPolicy(_port_policy)

        port_spec = cls(
            name=name,
            protocol=protocol,
            container_port=container_port,
            port_policy=port_policy,
        )

        port_spec.additional_properties = d
        return port_spec

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

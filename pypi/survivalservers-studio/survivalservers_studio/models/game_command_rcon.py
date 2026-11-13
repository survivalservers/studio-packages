from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_command_rcon_type import GameCommandRconType

T = TypeVar("T", bound="GameCommandRcon")


@_attrs_define
class GameCommandRcon:
    """A Source RCON command over TCP (Source and Source 2 servers, Minecraft, Palworld, ARK and others). `port` names one
    of the version's ports: on Linux the command reaches that port's `container_port` inside the container (a
    `passthrough` port's own number), on Windows the port leased to the game server. Make it an admin port
    (`port_policy` `none`) so it is never open to the internet; the command still reaches it from the machine.

        Attributes:
            type_ (GameCommandRconType):
            port (str): One of the version's port names.
            password_env (str): The name of one of the version's `env` values (usually a secret) holding the RCON password.
            command (str):
    """

    type_: GameCommandRconType
    port: str
    password_env: str
    command: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        port = self.port

        password_env = self.password_env

        command = self.command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "port": port,
                "password_env": password_env,
                "command": command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = GameCommandRconType(d.pop("type"))

        port = d.pop("port")

        password_env = d.pop("password_env")

        command = d.pop("command")

        game_command_rcon = cls(
            type_=type_,
            port=port,
            password_env=password_env,
            command=command,
        )

        game_command_rcon.additional_properties = d
        return game_command_rcon

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

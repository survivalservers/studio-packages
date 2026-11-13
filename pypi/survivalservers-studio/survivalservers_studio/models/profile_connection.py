from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.profile_connection_type import ProfileConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_connection_headers import ProfileConnectionHeaders


T = TypeVar("T", bound="ProfileConnection")


@_attrs_define
class ProfileConnection:
    """How to reach a running game. The machine agent connects on the game's own machine, so an admin port never needs to
    be public.

        Attributes:
            type_ (ProfileConnectionType): `console` types into standard input, `rcon` is Source RCON over TCP, `http` calls
                the game's web interface, `a2s` is a Steam query port (for reading players), `isle_rcon` is The Isle Evrima's
                own RCON over TCP (its commands by name: `announce`, `kick`, `ban`, `save`, `playerlist` and the others the game
                lists).
            port (str | Unset): One of the version's port names, for all but `console`.
            password_env (str | Unset): The name of one of the version's `env` values holding the password: for RCON, and
                for HTTP with `user`.
            user (str | Unset): HTTP: the basic auth user.
            headers (ProfileConnectionHeaders | Unset): HTTP: headers sent with every call.
    """

    type_: ProfileConnectionType
    port: str | Unset = UNSET
    password_env: str | Unset = UNSET
    user: str | Unset = UNSET
    headers: ProfileConnectionHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        port = self.port

        password_env = self.password_env

        user = self.user

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if password_env is not UNSET:
            field_dict["password_env"] = password_env
        if user is not UNSET:
            field_dict["user"] = user
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.profile_connection_headers import ProfileConnectionHeaders

        d = dict(src_dict)
        type_ = ProfileConnectionType(d.pop("type"))

        port = d.pop("port", UNSET)

        password_env = d.pop("password_env", UNSET)

        user = d.pop("user", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ProfileConnectionHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ProfileConnectionHeaders.from_dict(_headers)

        profile_connection = cls(
            type_=type_,
            port=port,
            password_env=password_env,
            user=user,
            headers=headers,
        )

        return profile_connection

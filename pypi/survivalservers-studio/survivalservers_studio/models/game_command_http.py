from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_command_http_method import GameCommandHttpMethod
from ..models.game_command_http_type import GameCommandHttpType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_command_http_basic_auth import GameCommandHttpBasicAuth
    from ..models.game_command_http_header_env import GameCommandHttpHeaderEnv
    from ..models.game_command_http_headers import GameCommandHttpHeaders


T = TypeVar("T", bound="GameCommandHttp")


@_attrs_define
class GameCommandHttp:
    """An HTTP call to the game server's own web interface on one of its ports; any 2xx answer counts.

    Attributes:
        type_ (GameCommandHttpType):
        port (str): One of the version's port names.
        path (str):
        method (GameCommandHttpMethod | Unset): Default POST.
        body (str | Unset):
        headers (GameCommandHttpHeaders | Unset):
        header_env (GameCommandHttpHeaderEnv | Unset): Headers whose values come from the version's `env` values, by
            name: a game's API token kept as a secret env value, so it is never in the version's settings. Set after
            `headers` (a name in both takes this value).
        basic_auth (GameCommandHttpBasicAuth | Unset):
    """

    type_: GameCommandHttpType
    port: str
    path: str
    method: GameCommandHttpMethod | Unset = UNSET
    body: str | Unset = UNSET
    headers: GameCommandHttpHeaders | Unset = UNSET
    header_env: GameCommandHttpHeaderEnv | Unset = UNSET
    basic_auth: GameCommandHttpBasicAuth | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        port = self.port

        path = self.path

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        body = self.body

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        header_env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_env, Unset):
            header_env = self.header_env.to_dict()

        basic_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "port": port,
                "path": path,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers
        if header_env is not UNSET:
            field_dict["header_env"] = header_env
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_command_http_basic_auth import GameCommandHttpBasicAuth
        from ..models.game_command_http_header_env import GameCommandHttpHeaderEnv
        from ..models.game_command_http_headers import GameCommandHttpHeaders

        d = dict(src_dict)
        type_ = GameCommandHttpType(d.pop("type"))

        port = d.pop("port")

        path = d.pop("path")

        _method = d.pop("method", UNSET)
        method: GameCommandHttpMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = GameCommandHttpMethod(_method)

        body = d.pop("body", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: GameCommandHttpHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = GameCommandHttpHeaders.from_dict(_headers)

        _header_env = d.pop("header_env", UNSET)
        header_env: GameCommandHttpHeaderEnv | Unset
        if isinstance(_header_env, Unset):
            header_env = UNSET
        else:
            header_env = GameCommandHttpHeaderEnv.from_dict(_header_env)

        _basic_auth = d.pop("basic_auth", UNSET)
        basic_auth: GameCommandHttpBasicAuth | Unset
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = GameCommandHttpBasicAuth.from_dict(_basic_auth)

        game_command_http = cls(
            type_=type_,
            port=port,
            path=path,
            method=method,
            body=body,
            headers=headers,
            header_env=header_env,
            basic_auth=basic_auth,
        )

        game_command_http.additional_properties = d
        return game_command_http

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

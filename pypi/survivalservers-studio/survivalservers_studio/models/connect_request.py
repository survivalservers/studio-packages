from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectRequest")


@_attrs_define
class ConnectRequest:
    """
    Attributes:
        id (str): The one-time handle.
        client_name (str): What the tool calls itself, such as Claude Code. Tools name themselves; the approval page
            also shows `redirect_host`.
        redirect_host (str): The host the sign-in goes back to, such as `localhost`.
        local (bool): `true` when it goes back to this computer (localhost or a loopback address).
        expires_at (datetime.datetime):
        client_uri (None | str | Unset):
    """

    id: str
    client_name: str
    redirect_host: str
    local: bool
    expires_at: datetime.datetime
    client_uri: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_name = self.client_name

        redirect_host = self.redirect_host

        local = self.local

        expires_at = self.expires_at.isoformat()

        client_uri: None | str | Unset
        if isinstance(self.client_uri, Unset):
            client_uri = UNSET
        else:
            client_uri = self.client_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "client_name": client_name,
                "redirect_host": redirect_host,
                "local": local,
                "expires_at": expires_at,
            }
        )
        if client_uri is not UNSET:
            field_dict["client_uri"] = client_uri

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        client_name = d.pop("client_name")

        redirect_host = d.pop("redirect_host")

        local = d.pop("local")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        def _parse_client_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_uri = _parse_client_uri(d.pop("client_uri", UNSET))

        connect_request = cls(
            id=id,
            client_name=client_name,
            redirect_host=redirect_host,
            local=local,
            expires_at=expires_at,
            client_uri=client_uri,
        )

        connect_request.additional_properties = d
        return connect_request

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

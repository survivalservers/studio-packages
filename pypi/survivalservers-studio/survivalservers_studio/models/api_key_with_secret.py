from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scope import Scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyWithSecret")


@_attrs_define
class ApiKeyWithSecret:
    """
    Attributes:
        id (str): API key ID.
        name (str): Its name.
        scopes (list[Scope]):
        key_prefix (str): The non-secret start of the key, to tell keys apart.
        created_at (datetime.datetime): When it was made.
        key (str): Shown only in this reply.
        apps (list[str] | Unset):
        allowed_ips (list[str] | Unset):
        expires_at (datetime.datetime | None | Unset): When it expires.
        last_used_at (datetime.datetime | None | Unset):
        agent (str | Unset): AI agent ID.
    """

    id: str
    name: str
    scopes: list[Scope]
    key_prefix: str
    created_at: datetime.datetime
    key: str
    apps: list[str] | Unset = UNSET
    allowed_ips: list[str] | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    last_used_at: datetime.datetime | None | Unset = UNSET
    agent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        key_prefix = self.key_prefix

        created_at = self.created_at.isoformat()

        key = self.key

        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        allowed_ips: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ips, Unset):
            allowed_ips = self.allowed_ips

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        agent = self.agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "scopes": scopes,
                "key_prefix": key_prefix,
                "created_at": created_at,
                "key": key,
            }
        )
        if apps is not UNSET:
            field_dict["apps"] = apps
        if allowed_ips is not UNSET:
            field_dict["allowed_ips"] = allowed_ips
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if agent is not UNSET:
            field_dict["agent"] = agent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = Scope(scopes_item_data)

            scopes.append(scopes_item)

        key_prefix = d.pop("key_prefix")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        key = d.pop("key")

        apps = cast(list[str], d.pop("apps", UNSET))

        allowed_ips = cast(list[str], d.pop("allowed_ips", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        agent = d.pop("agent", UNSET)

        api_key_with_secret = cls(
            id=id,
            name=name,
            scopes=scopes,
            key_prefix=key_prefix,
            created_at=created_at,
            key=key,
            apps=apps,
            allowed_ips=allowed_ips,
            expires_at=expires_at,
            last_used_at=last_used_at,
            agent=agent,
        )

        api_key_with_secret.additional_properties = d
        return api_key_with_secret

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegistryToken")


@_attrs_define
class RegistryToken:
    """
    Attributes:
        registry (str):
        repository (str):
        username (str):
        password (str):
        expires_at (datetime.datetime): When it expires.
    """

    registry: str
    repository: str
    username: str
    password: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registry = self.registry

        repository = self.repository

        username = self.username

        password = self.password

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registry": registry,
                "repository": repository,
                "username": username,
                "password": password,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registry = d.pop("registry")

        repository = d.pop("repository")

        username = d.pop("username")

        password = d.pop("password")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        registry_token = cls(
            registry=registry,
            repository=repository,
            username=username,
            password=password,
            expires_at=expires_at,
        )

        registry_token.additional_properties = d
        return registry_token

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

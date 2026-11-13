from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_set_version import ConfigSetVersion


T = TypeVar("T", bound="ConfigSet")


@_attrs_define
class ConfigSet:
    """
    Attributes:
        id (str): Config set ID.
        app (str): App ID.
        name (str): Its name.
        latest_version (int):
        persistent_servers (int): Persistent servers using any version of it.
        current (ConfigSetVersion):
        created_at (datetime.datetime): When it was made.
        updated_at (datetime.datetime): When it last changed.
        description (None | str | Unset):
    """

    id: str
    app: str
    name: str
    latest_version: int
    persistent_servers: int
    current: ConfigSetVersion
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        app = self.app

        name = self.name

        latest_version = self.latest_version

        persistent_servers = self.persistent_servers

        current = self.current.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app": app,
                "name": name,
                "latest_version": latest_version,
                "persistent_servers": persistent_servers,
                "current": current,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_set_version import ConfigSetVersion

        d = dict(src_dict)
        id = d.pop("id")

        app = d.pop("app")

        name = d.pop("name")

        latest_version = d.pop("latest_version")

        persistent_servers = d.pop("persistent_servers")

        current = ConfigSetVersion.from_dict(d.pop("current"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        config_set = cls(
            id=id,
            app=app,
            name=name,
            latest_version=latest_version,
            persistent_servers=persistent_servers,
            current=current,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        config_set.additional_properties = d
        return config_set

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

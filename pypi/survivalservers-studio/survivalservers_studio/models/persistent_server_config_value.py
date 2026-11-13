from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persistent_server_config_value_source import (
    PersistentServerConfigValueSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersistentServerConfigValue")


@_attrs_define
class PersistentServerConfigValue:
    """
    Attributes:
        id (str): The setting's ID.
        source (PersistentServerConfigValueSource): Where the value comes from.
        pending (bool): It differs from what the current run started with
        value (Any | Unset): Its value. Left out when nobody set it and the game has no known default.
        not_applied (bool | Unset): The current run started with this value, but its machine did not make the change in
            the game's file. See `not_applied` on the settings.
    """

    id: str
    source: PersistentServerConfigValueSource
    pending: bool
    value: Any | Unset = UNSET
    not_applied: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source = self.source.value

        pending = self.pending

        value = self.value

        not_applied = self.not_applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "pending": pending,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if not_applied is not UNSET:
            field_dict["not_applied"] = not_applied

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        source = PersistentServerConfigValueSource(d.pop("source"))

        pending = d.pop("pending")

        value = d.pop("value", UNSET)

        not_applied = d.pop("not_applied", UNSET)

        persistent_server_config_value = cls(
            id=id,
            source=source,
            pending=pending,
            value=value,
            not_applied=not_applied,
        )

        persistent_server_config_value.additional_properties = d
        return persistent_server_config_value

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

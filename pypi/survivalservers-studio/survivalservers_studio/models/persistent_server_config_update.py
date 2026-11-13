from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setting_values import SettingValues


T = TypeVar("T", bound="PersistentServerConfigUpdate")


@_attrs_define
class PersistentServerConfigUpdate:
    """
    Attributes:
        values (SettingValues): Values by setting ID, each its setting's type.
        live (bool | Unset): Also send the settings that can change in the running game.
    """

    values: SettingValues
    live: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values.to_dict()

        live = self.live

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )
        if live is not UNSET:
            field_dict["live"] = live

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.setting_values import SettingValues

        d = dict(src_dict)
        values = SettingValues.from_dict(d.pop("values"))

        live = d.pop("live", UNSET)

        persistent_server_config_update = cls(
            values=values,
            live=live,
        )

        persistent_server_config_update.additional_properties = d
        return persistent_server_config_update

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_change_overridden_item import ConfigChangeOverriddenItem
    from ..models.config_diff import ConfigDiff
    from ..models.config_set_ref_type_0 import ConfigSetRefType0


T = TypeVar("T", bound="ConfigChange")


@_attrs_define
class ConfigChange:
    """
    Attributes:
        persistent_servers (int): Persistent servers in this group.
        persistent_server_ids (list[str]): Up to 20 of them.
        diff (ConfigDiff):
        from_ (ConfigSetRefType0 | None | Unset):
        overridden (list[ConfigChangeOverriddenItem] | Unset): Variables the set changes that some of these persistent
            servers set themselves (the set's value replaces theirs).
    """

    persistent_servers: int
    persistent_server_ids: list[str]
    diff: ConfigDiff
    from_: ConfigSetRefType0 | None | Unset = UNSET
    overridden: list[ConfigChangeOverriddenItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_set_ref_type_0 import ConfigSetRefType0

        persistent_servers = self.persistent_servers

        persistent_server_ids = self.persistent_server_ids

        diff = self.diff.to_dict()

        from_: dict[str, Any] | None | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, ConfigSetRefType0):
            from_ = self.from_.to_dict()
        else:
            from_ = self.from_

        overridden: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overridden, Unset):
            overridden = []
            for overridden_item_data in self.overridden:
                overridden_item = overridden_item_data.to_dict()
                overridden.append(overridden_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "persistent_servers": persistent_servers,
                "persistent_server_ids": persistent_server_ids,
                "diff": diff,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if overridden is not UNSET:
            field_dict["overridden"] = overridden

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_change_overridden_item import ConfigChangeOverriddenItem
        from ..models.config_diff import ConfigDiff
        from ..models.config_set_ref_type_0 import ConfigSetRefType0

        d = dict(src_dict)
        persistent_servers = d.pop("persistent_servers")

        persistent_server_ids = cast(list[str], d.pop("persistent_server_ids"))

        diff = ConfigDiff.from_dict(d.pop("diff"))

        def _parse_from_(data: object) -> ConfigSetRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_config_set_ref_type_0 = ConfigSetRefType0.from_dict(
                    data
                )

                return componentsschemas_config_set_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigSetRefType0 | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        _overridden = d.pop("overridden", UNSET)
        overridden: list[ConfigChangeOverriddenItem] | Unset = UNSET
        if _overridden is not UNSET:
            overridden = []
            for overridden_item_data in _overridden:
                overridden_item = ConfigChangeOverriddenItem.from_dict(
                    overridden_item_data
                )

                overridden.append(overridden_item)

        config_change = cls(
            persistent_servers=persistent_servers,
            persistent_server_ids=persistent_server_ids,
            diff=diff,
            from_=from_,
            overridden=overridden,
        )

        config_change.additional_properties = d
        return config_change

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

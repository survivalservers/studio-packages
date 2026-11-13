from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_set_ref_type_0 import ConfigSetRefType0


T = TypeVar("T", bound="BulkActionChangeFrom")


@_attrs_define
class BulkActionChangeFrom:
    """What a target had before the bulk action changed it.

    Attributes:
        version (None | str | Unset): Its version name.
        branch (None | str | Unset):
        config_set (ConfigSetRefType0 | None | Unset):
        backup (str | Unset): Backup ID.
    """

    version: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    config_set: ConfigSetRefType0 | None | Unset = UNSET
    backup: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_set_ref_type_0 import ConfigSetRefType0

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        config_set: dict[str, Any] | None | Unset
        if isinstance(self.config_set, Unset):
            config_set = UNSET
        elif isinstance(self.config_set, ConfigSetRefType0):
            config_set = self.config_set.to_dict()
        else:
            config_set = self.config_set

        backup = self.backup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if backup is not UNSET:
            field_dict["backup"] = backup

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_set_ref_type_0 import ConfigSetRefType0

        d = dict(src_dict)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_config_set(data: object) -> ConfigSetRefType0 | None | Unset:
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

        config_set = _parse_config_set(d.pop("config_set", UNSET))

        backup = d.pop("backup", UNSET)

        bulk_action_change_from = cls(
            version=version,
            branch=branch,
            config_set=config_set,
            backup=backup,
        )

        bulk_action_change_from.additional_properties = d
        return bulk_action_change_from

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

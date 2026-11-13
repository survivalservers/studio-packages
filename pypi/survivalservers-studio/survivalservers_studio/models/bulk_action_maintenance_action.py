from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_maintenance_action_type import BulkActionMaintenanceActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkActionMaintenanceAction")


@_attrs_define
class BulkActionMaintenanceAction:
    """
    Attributes:
        type_ (BulkActionMaintenanceActionType): Restart, move to `version` or `branch`, or apply `config_set` at
            `config_version`.
        version (str | Unset):
        branch (str | Unset): Branch name, for example `live`.
        config_set (str | Unset): Config set ID.
        config_version (int | Unset): Default the set's latest.
    """

    type_: BulkActionMaintenanceActionType
    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    config_set: str | Unset = UNSET
    config_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        version = self.version

        branch = self.branch

        config_set = self.config_set

        config_version = self.config_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if config_version is not UNSET:
            field_dict["config_version"] = config_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = BulkActionMaintenanceActionType(d.pop("type"))

        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

        config_set = d.pop("config_set", UNSET)

        config_version = d.pop("config_version", UNSET)

        bulk_action_maintenance_action = cls(
            type_=type_,
            version=version,
            branch=branch,
            config_set=config_set,
            config_version=config_version,
        )

        bulk_action_maintenance_action.additional_properties = d
        return bulk_action_maintenance_action

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

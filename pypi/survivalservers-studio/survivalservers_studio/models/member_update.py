from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role import Role
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberUpdate")


@_attrs_define
class MemberUpdate:
    """Send `role`, `crash_dumps` or both (`422` with neither).

    Attributes:
        role (Role | Unset):
        crash_dumps (bool | Unset): Lets this member list and download crash dumps, from the panel. Only an owner turns
            it on, from the panel, and never for themselves (`403 key_restricted`); admins and keys can only turn it off.
            For owners and admins only (`409 invalid_state` for another role); a role change below admin turns it off. No
            API key can ever download one.
    """

    role: Role | Unset = UNSET
    crash_dumps: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        crash_dumps = self.crash_dumps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if crash_dumps is not UNSET:
            field_dict["crash_dumps"] = crash_dumps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: Role | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Role(_role)

        crash_dumps = d.pop("crash_dumps", UNSET)

        member_update = cls(
            role=role,
            crash_dumps=crash_dumps,
        )

        member_update.additional_properties = d
        return member_update

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

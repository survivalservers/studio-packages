from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role import Role
from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """
    Attributes:
        user (str): Person ID.
        email (str):
        role (Role):
        joined_at (datetime.datetime):
        name (None | str | Unset):
        mfa_enabled (bool | Unset):
        crash_dumps (bool | Unset): Whether this owner or admin may list and download crash dumps. Off unless an owner
            or admin turns it on; a crash dump holds the game's whole memory.
    """

    user: str
    email: str
    role: Role
    joined_at: datetime.datetime
    name: None | str | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    crash_dumps: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        email = self.email

        role = self.role.value

        joined_at = self.joined_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        mfa_enabled = self.mfa_enabled

        crash_dumps = self.crash_dumps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "email": email,
                "role": role,
                "joined_at": joined_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if mfa_enabled is not UNSET:
            field_dict["mfa_enabled"] = mfa_enabled
        if crash_dumps is not UNSET:
            field_dict["crash_dumps"] = crash_dumps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user = d.pop("user")

        email = d.pop("email")

        role = Role(d.pop("role"))

        joined_at = datetime.datetime.fromisoformat(d.pop("joined_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        mfa_enabled = d.pop("mfa_enabled", UNSET)

        crash_dumps = d.pop("crash_dumps", UNSET)

        member = cls(
            user=user,
            email=email,
            role=role,
            joined_at=joined_at,
            name=name,
            mfa_enabled=mfa_enabled,
            crash_dumps=crash_dumps,
        )

        member.additional_properties = d
        return member

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

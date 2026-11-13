from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SsoMoving")


@_attrs_define
class SsoMoving:
    """Accounts with an email in a proven domain that still have a password, other than the emergency owner. Switching on
    moves them to your provider (they lose the password); while on, this stays at zero.

        Attributes:
            members (int): Members of this studio.
            others (int): Other accounts with an email in your domains.
    """

    members: int
    others: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = self.members

        others = self.others

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
                "others": others,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        members = d.pop("members")

        others = d.pop("others")

        sso_moving = cls(
            members=members,
            others=others,
        )

        sso_moving.additional_properties = d
        return sso_moving

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

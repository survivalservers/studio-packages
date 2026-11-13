from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayersChange")


@_attrs_define
class PlayersChange:
    """
    Attributes:
        join (list[str] | Unset):
        leave (list[str] | Unset):
    """

    join: list[str] | Unset = UNSET
    leave: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        join: list[str] | Unset = UNSET
        if not isinstance(self.join, Unset):
            join = self.join

        leave: list[str] | Unset = UNSET
        if not isinstance(self.leave, Unset):
            leave = self.leave

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if join is not UNSET:
            field_dict["join"] = join
        if leave is not UNSET:
            field_dict["leave"] = leave

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        join = cast(list[str], d.pop("join", UNSET))

        leave = cast(list[str], d.pop("leave", UNSET))

        players_change = cls(
            join=join,
            leave=leave,
        )

        players_change.additional_properties = d
        return players_change

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

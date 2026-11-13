from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlacementResult")


@_attrs_define
class PlacementResult:
    """
    Attributes:
        fallback_used (bool | Unset):
        worst_ping_ms (int | None | Unset):
    """

    fallback_used: bool | Unset = UNSET
    worst_ping_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fallback_used = self.fallback_used

        worst_ping_ms: int | None | Unset
        if isinstance(self.worst_ping_ms, Unset):
            worst_ping_ms = UNSET
        else:
            worst_ping_ms = self.worst_ping_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fallback_used is not UNSET:
            field_dict["fallback_used"] = fallback_used
        if worst_ping_ms is not UNSET:
            field_dict["worst_ping_ms"] = worst_ping_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fallback_used = d.pop("fallback_used", UNSET)

        def _parse_worst_ping_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        worst_ping_ms = _parse_worst_ping_ms(d.pop("worst_ping_ms", UNSET))

        placement_result = cls(
            fallback_used=fallback_used,
            worst_ping_ms=worst_ping_ms,
        )

        placement_result.additional_properties = d
        return placement_result

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Timings")


@_attrs_define
class Timings:
    """Milliseconds spent on the start, measured at our API edge.

    Attributes:
        total (int | Unset):
        placement (int | Unset):
        machine (int | Unset):
    """

    total: int | Unset = UNSET
    placement: int | Unset = UNSET
    machine: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        placement = self.placement

        machine = self.machine

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if placement is not UNSET:
            field_dict["placement"] = placement
        if machine is not UNSET:
            field_dict["machine"] = machine

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        placement = d.pop("placement", UNSET)

        machine = d.pop("machine", UNSET)

        timings = cls(
            total=total,
            placement=placement,
            machine=machine,
        )

        timings.additional_properties = d
        return timings

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

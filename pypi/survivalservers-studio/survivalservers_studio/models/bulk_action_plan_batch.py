from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkActionPlanBatch")


@_attrs_define
class BulkActionPlanBatch:
    """
    Attributes:
        batch (int): From 1.
        size (int): Targets in it.
        pause_after (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
    """

    batch: int
    size: int
    pause_after: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch = self.batch

        size = self.size

        pause_after: int | str | Unset
        if isinstance(self.pause_after, Unset):
            pause_after = UNSET
        else:
            pause_after = self.pause_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch": batch,
                "size": size,
            }
        )
        if pause_after is not UNSET:
            field_dict["pause_after"] = pause_after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        batch = d.pop("batch")

        size = d.pop("size")

        def _parse_pause_after(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        pause_after = _parse_pause_after(d.pop("pause_after", UNSET))

        bulk_action_plan_batch = cls(
            batch=batch,
            size=size,
            pause_after=pause_after,
        )

        bulk_action_plan_batch.additional_properties = d
        return bulk_action_plan_batch

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

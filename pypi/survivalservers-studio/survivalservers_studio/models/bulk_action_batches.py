from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkActionBatches")


@_attrs_define
class BulkActionBatches:
    """
    Attributes:
        total (int): How many batches.
        current (int): The batch under way or last run, from 1; 0 before the first.
        size (int): Targets per batch.
        next_at (datetime.datetime | None | Unset): When the next batch starts, during a pause.
    """

    total: int
    current: int
    size: int
    next_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        current = self.current

        size = self.size

        next_at: None | str | Unset
        if isinstance(self.next_at, Unset):
            next_at = UNSET
        elif isinstance(self.next_at, datetime.datetime):
            next_at = self.next_at.isoformat()
        else:
            next_at = self.next_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "current": current,
                "size": size,
            }
        )
        if next_at is not UNSET:
            field_dict["next_at"] = next_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total")

        current = d.pop("current")

        size = d.pop("size")

        def _parse_next_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_at = _parse_next_at(d.pop("next_at", UNSET))

        bulk_action_batches = cls(
            total=total,
            current=current,
            size=size,
            next_at=next_at,
        )

        bulk_action_batches.additional_properties = d
        return bulk_action_batches

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoredBackups")


@_attrs_define
class StoredBackups:
    """What a persistent server's backups hold. A chunk shared by many backups counts once.

    Attributes:
        bytes_ (int):
        count (int):
        oldest_at (datetime.datetime | None | Unset): The time of the game state in its oldest backup.
    """

    bytes_: int
    count: int
    oldest_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_ = self.bytes_

        count = self.count

        oldest_at: None | str | Unset
        if isinstance(self.oldest_at, Unset):
            oldest_at = UNSET
        elif isinstance(self.oldest_at, datetime.datetime):
            oldest_at = self.oldest_at.isoformat()
        else:
            oldest_at = self.oldest_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bytes": bytes_,
                "count": count,
            }
        )
        if oldest_at is not UNSET:
            field_dict["oldest_at"] = oldest_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        count = d.pop("count")

        def _parse_oldest_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oldest_at_type_0 = datetime.datetime.fromisoformat(data)

                return oldest_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        oldest_at = _parse_oldest_at(d.pop("oldest_at", UNSET))

        stored_backups = cls(
            bytes_=bytes_,
            count=count,
            oldest_at=oldest_at,
        )

        stored_backups.additional_properties = d
        return stored_backups

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

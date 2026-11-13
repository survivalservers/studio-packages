from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionUsage")


@_attrs_define
class VersionUsage:
    """
    Attributes:
        runs (int): Game servers counted.
        peak_memory_mb (int): The highest any of them used (one stopped for going over its size used all of it).
        peak_memory_at (datetime.datetime): When that was.
        p95_memory_mb (int): 95 in 100 of them stayed at or under this at their highest.
    """

    runs: int
    peak_memory_mb: int
    peak_memory_at: datetime.datetime
    p95_memory_mb: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs = self.runs

        peak_memory_mb = self.peak_memory_mb

        peak_memory_at = self.peak_memory_at.isoformat()

        p95_memory_mb = self.p95_memory_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runs": runs,
                "peak_memory_mb": peak_memory_mb,
                "peak_memory_at": peak_memory_at,
                "p95_memory_mb": p95_memory_mb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        runs = d.pop("runs")

        peak_memory_mb = d.pop("peak_memory_mb")

        peak_memory_at = datetime.datetime.fromisoformat(d.pop("peak_memory_at"))

        p95_memory_mb = d.pop("p95_memory_mb")

        version_usage = cls(
            runs=runs,
            peak_memory_mb=peak_memory_mb,
            peak_memory_at=peak_memory_at,
            p95_memory_mb=p95_memory_mb,
        )

        version_usage.additional_properties = d
        return version_usage

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

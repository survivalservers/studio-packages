from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkActionCounts")


@_attrs_define
class BulkActionCounts:
    """
    Attributes:
        total (int):
        pending (int):
        running (int):
        succeeded (int):
        failed (int):
        skipped (int):
        cancelled (int):
    """

    total: int
    pending: int
    running: int
    succeeded: int
    failed: int
    skipped: int
    cancelled: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        running = self.running

        succeeded = self.succeeded

        failed = self.failed

        skipped = self.skipped

        cancelled = self.cancelled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "pending": pending,
                "running": running,
                "succeeded": succeeded,
                "failed": failed,
                "skipped": skipped,
                "cancelled": cancelled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total")

        pending = d.pop("pending")

        running = d.pop("running")

        succeeded = d.pop("succeeded")

        failed = d.pop("failed")

        skipped = d.pop("skipped")

        cancelled = d.pop("cancelled")

        bulk_action_counts = cls(
            total=total,
            pending=pending,
            running=running,
            succeeded=succeeded,
            failed=failed,
            skipped=skipped,
            cancelled=cancelled,
        )

        bulk_action_counts.additional_properties = d
        return bulk_action_counts

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

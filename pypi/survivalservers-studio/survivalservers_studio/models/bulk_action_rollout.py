from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_rollout_first import BulkActionRolloutFirst


T = TypeVar("T", bound="BulkActionRollout")


@_attrs_define
class BulkActionRollout:
    """How targets are taken in batches. Give `batch_size` or `batch_percent`, not both.

    Attributes:
        batch_size (int | Unset): Targets per batch. Default 50 for commands, all of them for maintenance.
        batch_percent (int | Unset): A share of the targets per batch, at least one. Default 10 for restarts, rollouts
            and config changes.
        per_machine (int | Unset): At most this many persistent servers on one machine restart at once. Default 3.
        pause (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        healthy_for (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        max_failures (int | Unset): The action stops once more targets than this have failed. Default 0 (the first
            failure stops it); commands and rollbacks default to no limit.
        first (BulkActionRolloutFirst | Unset): Try it on a few first. These targets go alone as the first batch; after
            `wait` the action pauses and says so in `stop_reason`, and `POST /v0/bulk-actions/{id}/resume` takes it on to
            the rest. Undo puts the few back.
    """

    batch_size: int | Unset = UNSET
    batch_percent: int | Unset = UNSET
    per_machine: int | Unset = UNSET
    pause: int | str | Unset = UNSET
    healthy_for: int | str | Unset = UNSET
    max_failures: int | Unset = UNSET
    first: BulkActionRolloutFirst | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_size = self.batch_size

        batch_percent = self.batch_percent

        per_machine = self.per_machine

        pause: int | str | Unset
        if isinstance(self.pause, Unset):
            pause = UNSET
        else:
            pause = self.pause

        healthy_for: int | str | Unset
        if isinstance(self.healthy_for, Unset):
            healthy_for = UNSET
        else:
            healthy_for = self.healthy_for

        max_failures = self.max_failures

        first: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if batch_percent is not UNSET:
            field_dict["batch_percent"] = batch_percent
        if per_machine is not UNSET:
            field_dict["per_machine"] = per_machine
        if pause is not UNSET:
            field_dict["pause"] = pause
        if healthy_for is not UNSET:
            field_dict["healthy_for"] = healthy_for
        if max_failures is not UNSET:
            field_dict["max_failures"] = max_failures
        if first is not UNSET:
            field_dict["first"] = first

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_rollout_first import BulkActionRolloutFirst

        d = dict(src_dict)
        batch_size = d.pop("batch_size", UNSET)

        batch_percent = d.pop("batch_percent", UNSET)

        per_machine = d.pop("per_machine", UNSET)

        def _parse_pause(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        pause = _parse_pause(d.pop("pause", UNSET))

        def _parse_healthy_for(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        healthy_for = _parse_healthy_for(d.pop("healthy_for", UNSET))

        max_failures = d.pop("max_failures", UNSET)

        _first = d.pop("first", UNSET)
        first: BulkActionRolloutFirst | Unset
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = BulkActionRolloutFirst.from_dict(_first)

        bulk_action_rollout = cls(
            batch_size=batch_size,
            batch_percent=batch_percent,
            per_machine=per_machine,
            pause=pause,
            healthy_for=healthy_for,
            max_failures=max_failures,
            first=first,
        )

        bulk_action_rollout.additional_properties = d
        return bulk_action_rollout

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

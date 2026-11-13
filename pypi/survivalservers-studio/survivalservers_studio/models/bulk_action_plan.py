from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_type import BulkActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_plan_batch import BulkActionPlanBatch
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_selector import BulkActionSelector
    from ..models.bulk_action_target import BulkActionTarget
    from ..models.config_change import ConfigChange


T = TypeVar("T", bound="BulkActionPlan")


@_attrs_define
class BulkActionPlan:
    """What a bulk action would do, without doing it.

    Attributes:
        type_ (BulkActionType):
        selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
            filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        rollout (BulkActionRollout): How targets are taken in batches. Give `batch_size` or `batch_percent`, not both.
        total (int): Targets it would act on.
        players (int): Players on them now.
        batches (list[BulkActionPlanBatch]):
        targets (list[BulkActionTarget]): Every target, in batch order.
        skipped (list[BulkActionTarget]): Matched but left alone, each with its `reason`.
        id (str | Unset): A preview's ID.
        expires_at (datetime.datetime | Unset): A rollback's preview: when `id` stops working.
        changes (list[ConfigChange] | Unset): Config: the persistent servers grouped by the config set version they have
            now, with the diff for each group.
        warnings_at (list[datetime.datetime] | Unset): Maintenance: when each warning would be sent.
        starts_at (datetime.datetime | None | Unset): When it would start (scheduled ones).
    """

    type_: BulkActionType
    selector: BulkActionSelector
    rollout: BulkActionRollout
    total: int
    players: int
    batches: list[BulkActionPlanBatch]
    targets: list[BulkActionTarget]
    skipped: list[BulkActionTarget]
    id: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    changes: list[ConfigChange] | Unset = UNSET
    warnings_at: list[datetime.datetime] | Unset = UNSET
    starts_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        selector = self.selector.to_dict()

        rollout = self.rollout.to_dict()

        total = self.total

        players = self.players

        batches = []
        for batches_item_data in self.batches:
            batches_item = batches_item_data.to_dict()
            batches.append(batches_item)

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        id = self.id

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        warnings_at: list[str] | Unset = UNSET
        if not isinstance(self.warnings_at, Unset):
            warnings_at = []
            for warnings_at_item_data in self.warnings_at:
                warnings_at_item = warnings_at_item_data.isoformat()
                warnings_at.append(warnings_at_item)

        starts_at: None | str | Unset
        if isinstance(self.starts_at, Unset):
            starts_at = UNSET
        elif isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "selector": selector,
                "rollout": rollout,
                "total": total,
                "players": players,
                "batches": batches,
                "targets": targets,
                "skipped": skipped,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if changes is not UNSET:
            field_dict["changes"] = changes
        if warnings_at is not UNSET:
            field_dict["warnings_at"] = warnings_at
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_plan_batch import BulkActionPlanBatch
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_selector import BulkActionSelector
        from ..models.bulk_action_target import BulkActionTarget
        from ..models.config_change import ConfigChange

        d = dict(src_dict)
        type_ = BulkActionType(d.pop("type"))

        selector = BulkActionSelector.from_dict(d.pop("selector"))

        rollout = BulkActionRollout.from_dict(d.pop("rollout"))

        total = d.pop("total")

        players = d.pop("players")

        batches = []
        _batches = d.pop("batches")
        for batches_item_data in _batches:
            batches_item = BulkActionPlanBatch.from_dict(batches_item_data)

            batches.append(batches_item)

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = BulkActionTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = BulkActionTarget.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        id = d.pop("id", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _changes = d.pop("changes", UNSET)
        changes: list[ConfigChange] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = ConfigChange.from_dict(changes_item_data)

                changes.append(changes_item)

        _warnings_at = d.pop("warnings_at", UNSET)
        warnings_at: list[datetime.datetime] | Unset = UNSET
        if _warnings_at is not UNSET:
            warnings_at = []
            for warnings_at_item_data in _warnings_at:
                warnings_at_item = datetime.datetime.fromisoformat(
                    warnings_at_item_data
                )

                warnings_at.append(warnings_at_item)

        def _parse_starts_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        starts_at = _parse_starts_at(d.pop("starts_at", UNSET))

        bulk_action_plan = cls(
            type_=type_,
            selector=selector,
            rollout=rollout,
            total=total,
            players=players,
            batches=batches,
            targets=targets,
            skipped=skipped,
            id=id,
            expires_at=expires_at,
            changes=changes,
            warnings_at=warnings_at,
            starts_at=starts_at,
        )

        bulk_action_plan.additional_properties = d
        return bulk_action_plan

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

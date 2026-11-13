from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_rollout_create_apply import BulkActionRolloutCreateApply
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_selector import BulkActionSelector


T = TypeVar("T", bound="BulkActionRolloutCreate")


@_attrs_define
class BulkActionRolloutCreate:
    """
    Attributes:
        selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
            filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        version (str | Unset): Version name or ID. Give this or `branch`.
        branch (str | Unset): Branch name, for example `live`.
        apply (BulkActionRolloutCreateApply | Unset): Persistent servers: at each one's next run, or now in rolling
            batches. Pools always change now, in rolling batches. Default: BulkActionRolloutCreateApply.NEXT_RESTART.
        rollout (BulkActionRollout | Unset): How targets are taken in batches. Give `batch_size` or `batch_percent`, not
            both.
        at (datetime.datetime | Unset): Start then instead of now.
        note (str | Unset):
        dry_run (bool | Unset):  Default: False.
    """

    selector: BulkActionSelector
    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    apply: BulkActionRolloutCreateApply | Unset = (
        BulkActionRolloutCreateApply.NEXT_RESTART
    )
    rollout: BulkActionRollout | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector.to_dict()

        version = self.version

        branch = self.branch

        apply: str | Unset = UNSET
        if not isinstance(self.apply, Unset):
            apply = self.apply.value

        rollout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.to_dict()

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        note = self.note

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if apply is not UNSET:
            field_dict["apply"] = apply
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if at is not UNSET:
            field_dict["at"] = at
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_selector import BulkActionSelector

        d = dict(src_dict)
        selector = BulkActionSelector.from_dict(d.pop("selector"))

        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

        _apply = d.pop("apply", UNSET)
        apply: BulkActionRolloutCreateApply | Unset
        if isinstance(_apply, Unset):
            apply = UNSET
        else:
            apply = BulkActionRolloutCreateApply(_apply)

        _rollout = d.pop("rollout", UNSET)
        rollout: BulkActionRollout | Unset
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = BulkActionRollout.from_dict(_rollout)

        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        bulk_action_rollout_create = cls(
            selector=selector,
            version=version,
            branch=branch,
            apply=apply,
            rollout=rollout,
            at=at,
            note=note,
            dry_run=dry_run,
        )

        bulk_action_rollout_create.additional_properties = d
        return bulk_action_rollout_create

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

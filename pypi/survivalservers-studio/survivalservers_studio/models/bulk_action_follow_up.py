from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_follow_up_apply import BulkActionFollowUpApply
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_rollout import BulkActionRollout


T = TypeVar("T", bound="BulkActionFollowUp")


@_attrs_define
class BulkActionFollowUp:
    """
    Attributes:
        apply (BulkActionFollowUpApply | Unset): Default the original bulk action's.
        rollout (BulkActionRollout | Unset): How targets are taken in batches. Give `batch_size` or `batch_percent`, not
            both.
        note (str | Unset):
        dry_run (bool | Unset):  Default: False.
    """

    apply: BulkActionFollowUpApply | Unset = UNSET
    rollout: BulkActionRollout | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apply: str | Unset = UNSET
        if not isinstance(self.apply, Unset):
            apply = self.apply.value

        rollout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.to_dict()

        note = self.note

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apply is not UNSET:
            field_dict["apply"] = apply
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_rollout import BulkActionRollout

        d = dict(src_dict)
        _apply = d.pop("apply", UNSET)
        apply: BulkActionFollowUpApply | Unset
        if isinstance(_apply, Unset):
            apply = UNSET
        else:
            apply = BulkActionFollowUpApply(_apply)

        _rollout = d.pop("rollout", UNSET)
        rollout: BulkActionRollout | Unset
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = BulkActionRollout.from_dict(_rollout)

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        bulk_action_follow_up = cls(
            apply=apply,
            rollout=rollout,
            note=note,
            dry_run=dry_run,
        )

        bulk_action_follow_up.additional_properties = d
        return bulk_action_follow_up

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

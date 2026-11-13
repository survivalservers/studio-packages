from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action import BulkAction
    from ..models.bulk_action_plan import BulkActionPlan


T = TypeVar("T", bound="BulkActionResult")


@_attrs_define
class BulkActionResult:
    """What a bulk action call made: the plan, and the bulk action unless it was a dry run (200 for a dry run, 202 when
    made).

        Attributes:
            plan (BulkActionPlan): What a bulk action would do, without doing it.
            bulk_action (BulkAction | Unset):
    """

    plan: BulkActionPlan
    bulk_action: BulkAction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.to_dict()

        bulk_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bulk_action, Unset):
            bulk_action = self.bulk_action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
            }
        )
        if bulk_action is not UNSET:
            field_dict["bulk_action"] = bulk_action

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action import BulkAction
        from ..models.bulk_action_plan import BulkActionPlan

        d = dict(src_dict)
        plan = BulkActionPlan.from_dict(d.pop("plan"))

        _bulk_action = d.pop("bulk_action", UNSET)
        bulk_action: BulkAction | Unset
        if isinstance(_bulk_action, Unset):
            bulk_action = UNSET
        else:
            bulk_action = BulkAction.from_dict(_bulk_action)

        bulk_action_result = cls(
            plan=plan,
            bulk_action=bulk_action,
        )

        bulk_action_result.additional_properties = d
        return bulk_action_result

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

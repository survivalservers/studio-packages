from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saved_action_kind import SavedActionKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_action_create_request import SavedActionCreateRequest
    from ..models.saved_action_schedule import SavedActionSchedule


T = TypeVar("T", bound="SavedActionCreate")


@_attrs_define
class SavedActionCreate:
    """
    Attributes:
        name (str): Unique in the studio.
        action (SavedActionKind): The bulk action it runs.
        request (SavedActionCreateRequest): The body of the bulk action's own call, without `dry_run` or `at`: `POST
            /v0/bulk-actions/commands`, `/restarts`, `/rollouts`, or `POST /v0/config-sets/{id}/apply` with `config_set`
            naming the set.
        config_set (str | Unset): Config set ID.
        schedule (SavedActionSchedule | Unset):
    """

    name: str
    action: SavedActionKind
    request: SavedActionCreateRequest
    config_set: str | Unset = UNSET
    schedule: SavedActionSchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action = self.action.value

        request = self.request.to_dict()

        config_set = self.config_set

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action": action,
                "request": request,
            }
        )
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.saved_action_create_request import SavedActionCreateRequest
        from ..models.saved_action_schedule import SavedActionSchedule

        d = dict(src_dict)
        name = d.pop("name")

        action = SavedActionKind(d.pop("action"))

        request = SavedActionCreateRequest.from_dict(d.pop("request"))

        config_set = d.pop("config_set", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: SavedActionSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = SavedActionSchedule.from_dict(_schedule)

        saved_action_create = cls(
            name=name,
            action=action,
            request=request,
            config_set=config_set,
            schedule=schedule,
        )

        saved_action_create.additional_properties = d
        return saved_action_create

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

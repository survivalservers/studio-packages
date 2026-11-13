from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_action_schedule import SavedActionSchedule


T = TypeVar("T", bound="SavedActionUpdate")


@_attrs_define
class SavedActionUpdate:
    """
    Attributes:
        name (str | Unset):
        schedule (None | SavedActionSchedule | Unset): The new schedule, or null to run only by hand.
        paused (bool | Unset):
    """

    name: str | Unset = UNSET
    schedule: None | SavedActionSchedule | Unset = UNSET
    paused: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.saved_action_schedule import SavedActionSchedule

        name = self.name

        schedule: dict[str, Any] | None | Unset
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, SavedActionSchedule):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

        paused = self.paused

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if paused is not UNSET:
            field_dict["paused"] = paused

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.saved_action_schedule import SavedActionSchedule

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_schedule(data: object) -> None | SavedActionSchedule | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = SavedActionSchedule.from_dict(data)

                return schedule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SavedActionSchedule | Unset, data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        paused = d.pop("paused", UNSET)

        saved_action_update = cls(
            name=name,
            schedule=schedule,
            paused=paused,
        )

        saved_action_update.additional_properties = d
        return saved_action_update

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

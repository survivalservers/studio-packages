from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saved_action_kind import SavedActionKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_action_request import SavedActionRequest
    from ..models.saved_action_schedule import SavedActionSchedule


T = TypeVar("T", bound="SavedAction")


@_attrs_define
class SavedAction:
    """
    Attributes:
        id (str): Saved action ID.
        name (str): Its name.
        action (SavedActionKind): The bulk action it runs.
        request (SavedActionRequest): The body of the bulk action's own call.
        paused (bool): Its schedule is on hold; it still runs by hand.
        created_by (str): The key or member that saved it.
        created_at (datetime.datetime): When it was saved.
        updated_at (datetime.datetime): When it last changed.
        config_set (str | Unset): Config set ID.
        schedule (SavedActionSchedule | Unset):
        next_run_at (datetime.datetime | None | Unset): When its schedule runs next.
        last_run_at (datetime.datetime | None | Unset): When it last ran.
        last_bulk_action (None | str | Unset): The bulk action its last run made.
        last_error (None | str | Unset): Why its last scheduled run did not start, in a sentence.
    """

    id: str
    name: str
    action: SavedActionKind
    request: SavedActionRequest
    paused: bool
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    config_set: str | Unset = UNSET
    schedule: SavedActionSchedule | Unset = UNSET
    next_run_at: datetime.datetime | None | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    last_bulk_action: None | str | Unset = UNSET
    last_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        action = self.action.value

        request = self.request.to_dict()

        paused = self.paused

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        config_set = self.config_set

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        next_run_at: None | str | Unset
        if isinstance(self.next_run_at, Unset):
            next_run_at = UNSET
        elif isinstance(self.next_run_at, datetime.datetime):
            next_run_at = self.next_run_at.isoformat()
        else:
            next_run_at = self.next_run_at

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        last_bulk_action: None | str | Unset
        if isinstance(self.last_bulk_action, Unset):
            last_bulk_action = UNSET
        else:
            last_bulk_action = self.last_bulk_action

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "action": action,
                "request": request,
                "paused": paused,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if next_run_at is not UNSET:
            field_dict["next_run_at"] = next_run_at
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if last_bulk_action is not UNSET:
            field_dict["last_bulk_action"] = last_bulk_action
        if last_error is not UNSET:
            field_dict["last_error"] = last_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.saved_action_request import SavedActionRequest
        from ..models.saved_action_schedule import SavedActionSchedule

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        action = SavedActionKind(d.pop("action"))

        request = SavedActionRequest.from_dict(d.pop("request"))

        paused = d.pop("paused")

        created_by = d.pop("created_by")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        config_set = d.pop("config_set", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: SavedActionSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = SavedActionSchedule.from_dict(_schedule)

        def _parse_next_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_run_at = _parse_next_run_at(d.pop("next_run_at", UNSET))

        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("last_run_at", UNSET))

        def _parse_last_bulk_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_bulk_action = _parse_last_bulk_action(d.pop("last_bulk_action", UNSET))

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        saved_action = cls(
            id=id,
            name=name,
            action=action,
            request=request,
            paused=paused,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            config_set=config_set,
            schedule=schedule,
            next_run_at=next_run_at,
            last_run_at=last_run_at,
            last_bulk_action=last_bulk_action,
            last_error=last_error,
        )

        saved_action.additional_properties = d
        return saved_action

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

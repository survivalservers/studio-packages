from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_object_meta_object import EventObjectMetaObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_failed_start import PoolFailedStart


T = TypeVar("T", bound="PoolStartsFailingEventData")


@_attrs_define
class PoolStartsFailingEventData:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
        app (str): App ID.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        version (str): Version name, unique in its app, for example `2.3.1`.
        failed_starts (int): Starts on that version that failed in a row.
        held (bool): It stopped starting game servers on that version.
        reason (str | Unset): Held: why, as `status.held.reason` says it.
        next_start_at (datetime.datetime | Unset): Backing off: the earliest it starts the next one.
        last_failure (PoolFailedStart | Unset):
    """

    object_: EventObjectMetaObject
    sequence: int
    app: str
    region: str
    version: str
    failed_starts: int
    held: bool
    reason: str | Unset = UNSET
    next_start_at: datetime.datetime | Unset = UNSET
    last_failure: PoolFailedStart | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        sequence = self.sequence

        app = self.app

        region = self.region

        version = self.version

        failed_starts = self.failed_starts

        held = self.held

        reason = self.reason

        next_start_at: str | Unset = UNSET
        if not isinstance(self.next_start_at, Unset):
            next_start_at = self.next_start_at.isoformat()

        last_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_failure, Unset):
            last_failure = self.last_failure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
                "app": app,
                "region": region,
                "version": version,
                "failed_starts": failed_starts,
                "held": held,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if next_start_at is not UNSET:
            field_dict["next_start_at"] = next_start_at
        if last_failure is not UNSET:
            field_dict["last_failure"] = last_failure

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pool_failed_start import PoolFailedStart

        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        app = d.pop("app")

        region = d.pop("region")

        version = d.pop("version")

        failed_starts = d.pop("failed_starts")

        held = d.pop("held")

        reason = d.pop("reason", UNSET)

        _next_start_at = d.pop("next_start_at", UNSET)
        next_start_at: datetime.datetime | Unset
        if isinstance(_next_start_at, Unset):
            next_start_at = UNSET
        else:
            next_start_at = datetime.datetime.fromisoformat(_next_start_at)

        _last_failure = d.pop("last_failure", UNSET)
        last_failure: PoolFailedStart | Unset
        if isinstance(_last_failure, Unset):
            last_failure = UNSET
        else:
            last_failure = PoolFailedStart.from_dict(_last_failure)

        pool_starts_failing_event_data = cls(
            object_=object_,
            sequence=sequence,
            app=app,
            region=region,
            version=version,
            failed_starts=failed_starts,
            held=held,
            reason=reason,
            next_start_at=next_start_at,
            last_failure=last_failure,
        )

        pool_starts_failing_event_data.additional_properties = d
        return pool_starts_failing_event_data

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

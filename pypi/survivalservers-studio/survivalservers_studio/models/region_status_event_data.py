from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_object_meta_object import EventObjectMetaObject
from ..models.region_status_event_data_status import RegionStatusEventDataStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegionStatusEventData")


@_attrs_define
class RegionStatusEventData:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        status (RegionStatusEventDataStatus): `down`: new game servers may not start there. `up`: it is back.
        since (datetime.datetime): When this status began.
        down_minutes (int | Unset): `up` only. How long it was down.
    """

    object_: EventObjectMetaObject
    sequence: int
    region: str
    status: RegionStatusEventDataStatus
    since: datetime.datetime
    down_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        sequence = self.sequence

        region = self.region

        status = self.status.value

        since = self.since.isoformat()

        down_minutes = self.down_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
                "region": region,
                "status": status,
                "since": since,
            }
        )
        if down_minutes is not UNSET:
            field_dict["down_minutes"] = down_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        region = d.pop("region")

        status = RegionStatusEventDataStatus(d.pop("status"))

        since = datetime.datetime.fromisoformat(d.pop("since"))

        down_minutes = d.pop("down_minutes", UNSET)

        region_status_event_data = cls(
            object_=object_,
            sequence=sequence,
            region=region,
            status=status,
            since=since,
            down_minutes=down_minutes,
        )

        region_status_event_data.additional_properties = d
        return region_status_event_data

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

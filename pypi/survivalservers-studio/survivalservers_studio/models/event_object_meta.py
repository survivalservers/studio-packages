from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_object_meta_object import EventObjectMetaObject

T = TypeVar("T", bound="EventObjectMeta")


@_attrs_define
class EventObjectMeta:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
    """

    object_: EventObjectMetaObject
    sequence: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        sequence = self.sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        event_object_meta = cls(
            object_=object_,
            sequence=sequence,
        )

        event_object_meta.additional_properties = d
        return event_object_meta

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

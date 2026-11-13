from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_object_meta_object import EventObjectMetaObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolExhaustedEventData")


@_attrs_define
class PoolExhaustedEventData:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
        app (str): App ID.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        version (str): Version name, unique in its app, for example `2.3.1`.
        game_server (str | Unset): Game server ID.
    """

    object_: EventObjectMetaObject
    sequence: int
    app: str
    region: str
    version: str
    game_server: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        sequence = self.sequence

        app = self.app

        region = self.region

        version = self.version

        game_server = self.game_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
                "app": app,
                "region": region,
                "version": version,
            }
        )
        if game_server is not UNSET:
            field_dict["game_server"] = game_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        app = d.pop("app")

        region = d.pop("region")

        version = d.pop("version")

        game_server = d.pop("game_server", UNSET)

        pool_exhausted_event_data = cls(
            object_=object_,
            sequence=sequence,
            app=app,
            region=region,
            version=version,
            game_server=game_server,
        )

        pool_exhausted_event_data.additional_properties = d
        return pool_exhausted_event_data

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

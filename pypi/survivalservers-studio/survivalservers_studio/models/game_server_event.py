from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_type import EventType

if TYPE_CHECKING:
    from ..models.game_server_event_data import GameServerEventData


T = TypeVar("T", bound="GameServerEvent")


@_attrs_define
class GameServerEvent:
    """
    Attributes:
        id (str): Event ID; also the `webhook-id` of its webhooks.
        type_ (EventType): `game_server.starting`, `game_server.stopping`, `game_server.players_changed`,
            `persistent_server.starting`, `persistent_server.stopping`, `persistent_server.paused`,
            `persistent_server.resuming`, `persistent_server.resumed` and `bulk_action.progress` are for watching: in the
            event stream only, never sent to webhook endpoints (so never among deliveries). New types may be added (section
            1.1).
        created_at (datetime.datetime): When it was made.
        studio (str): Studio ID.
        data (GameServerEventData):
    """

    id: str
    type_: EventType
    created_at: datetime.datetime
    studio: str
    data: GameServerEventData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        created_at = self.created_at.isoformat()

        studio = self.studio

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "created_at": created_at,
                "studio": studio,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_server_event_data import GameServerEventData

        d = dict(src_dict)
        id = d.pop("id")

        type_ = EventType(d.pop("type"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        studio = d.pop("studio")

        data = GameServerEventData.from_dict(d.pop("data"))

        game_server_event = cls(
            id=id,
            type_=type_,
            created_at=created_at,
            studio=studio,
            data=data,
        )

        game_server_event.additional_properties = d
        return game_server_event

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

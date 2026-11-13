from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery_status import DeliveryStatus
from ..models.event_type import EventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        id (str): Delivery attempt ID.
        event (str): Event ID; also the `webhook-id` of its webhooks.
        type_ (EventType): `game_server.starting`, `game_server.stopping`, `game_server.players_changed`,
            `persistent_server.starting`, `persistent_server.stopping`, `persistent_server.paused`,
            `persistent_server.resuming`, `persistent_server.resumed` and `bulk_action.progress` are for watching: in the
            event stream only, never sent to webhook endpoints (so never among deliveries). New types may be added (section
            1.1).
        url (str):
        attempt (int):
        status (DeliveryStatus):
        created_at (datetime.datetime): When it was made.
        endpoint (None | str | Unset): `null` for a per-request `webhook_url`.
        http_status (int | None | Unset):
        duration_ms (int | None | Unset):
        response_snippet (None | str | Unset): First 512 bytes of the reply.
        next_attempt_at (datetime.datetime | None | Unset):
    """

    id: str
    event: str
    type_: EventType
    url: str
    attempt: int
    status: DeliveryStatus
    created_at: datetime.datetime
    endpoint: None | str | Unset = UNSET
    http_status: int | None | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    response_snippet: None | str | Unset = UNSET
    next_attempt_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event = self.event

        type_ = self.type_.value

        url = self.url

        attempt = self.attempt

        status = self.status.value

        created_at = self.created_at.isoformat()

        endpoint: None | str | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        response_snippet: None | str | Unset
        if isinstance(self.response_snippet, Unset):
            response_snippet = UNSET
        else:
            response_snippet = self.response_snippet

        next_attempt_at: None | str | Unset
        if isinstance(self.next_attempt_at, Unset):
            next_attempt_at = UNSET
        elif isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event": event,
                "type": type_,
                "url": url,
                "attempt": attempt,
                "status": status,
                "created_at": created_at,
            }
        )
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if response_snippet is not UNSET:
            field_dict["response_snippet"] = response_snippet
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        event = d.pop("event")

        type_ = EventType(d.pop("type"))

        url = d.pop("url")

        attempt = d.pop("attempt")

        status = DeliveryStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("http_status", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_response_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_snippet = _parse_response_snippet(d.pop("response_snippet", UNSET))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at", UNSET))

        webhook_delivery = cls(
            id=id,
            event=event,
            type_=type_,
            url=url,
            attempt=attempt,
            status=status,
            created_at=created_at,
            endpoint=endpoint,
            http_status=http_status,
            duration_ms=duration_ms,
            response_snippet=response_snippet,
            next_attempt_at=next_attempt_at,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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

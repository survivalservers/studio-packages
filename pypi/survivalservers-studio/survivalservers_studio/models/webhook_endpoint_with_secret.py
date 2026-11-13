from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_endpoint_status import WebhookEndpointStatus
from ..models.webhook_format import WebhookFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quiet_hours import QuietHours


T = TypeVar("T", bound="WebhookEndpointWithSecret")


@_attrs_define
class WebhookEndpointWithSecret:
    """
    Attributes:
        id (str): Webhook endpoint ID.
        format_ (WebhookFormat): `standard`: signed JSON to your own backend. `slack` and `discord`: a short message to
            a channel, from its webhook URL there. It is fixed once made.
        url (str): `slack` and `discord`: masked. The URL is the secret, so it is never shown again.
        events (list[str]):
        default (bool):
        enabled (bool):
        status (WebhookEndpointStatus): An endpoint failing for 3 days in a row is disabled and the studio's owners are
            emailed. A channel Slack or Discord says is gone or closed to us is disabled at once.
        created_at (datetime.datetime): When it was made.
        apps (list[str] | Unset): Empty takes every app.
        regions (list[str] | Unset): Empty takes every region.
        quiet_hours (QuietHours | Unset): `slack` and `discord` only. Critical alerts still go; the rest wait and go as
            one summary when quiet hours end.
        disabled_reason (None | str | Unset):
        failing_since (datetime.datetime | None | Unset): When its current run of failed sends began.
        description (None | str | Unset):
        secret (str | Unset): Shown only in this reply. `standard` only: a channel's URL is its secret.
    """

    id: str
    format_: WebhookFormat
    url: str
    events: list[str]
    default: bool
    enabled: bool
    status: WebhookEndpointStatus
    created_at: datetime.datetime
    apps: list[str] | Unset = UNSET
    regions: list[str] | Unset = UNSET
    quiet_hours: QuietHours | Unset = UNSET
    disabled_reason: None | str | Unset = UNSET
    failing_since: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        format_ = self.format_.value

        url = self.url

        events = self.events

        default = self.default

        enabled = self.enabled

        status = self.status.value

        created_at = self.created_at.isoformat()

        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        quiet_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quiet_hours, Unset):
            quiet_hours = self.quiet_hours.to_dict()

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        else:
            disabled_reason = self.disabled_reason

        failing_since: None | str | Unset
        if isinstance(self.failing_since, Unset):
            failing_since = UNSET
        elif isinstance(self.failing_since, datetime.datetime):
            failing_since = self.failing_since.isoformat()
        else:
            failing_since = self.failing_since

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "format": format_,
                "url": url,
                "events": events,
                "default": default,
                "enabled": enabled,
                "status": status,
                "created_at": created_at,
            }
        )
        if apps is not UNSET:
            field_dict["apps"] = apps
        if regions is not UNSET:
            field_dict["regions"] = regions
        if quiet_hours is not UNSET:
            field_dict["quiet_hours"] = quiet_hours
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if failing_since is not UNSET:
            field_dict["failing_since"] = failing_since
        if description is not UNSET:
            field_dict["description"] = description
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.quiet_hours import QuietHours

        d = dict(src_dict)
        id = d.pop("id")

        format_ = WebhookFormat(d.pop("format"))

        url = d.pop("url")

        events = cast(list[str], d.pop("events"))

        default = d.pop("default")

        enabled = d.pop("enabled")

        status = WebhookEndpointStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        apps = cast(list[str], d.pop("apps", UNSET))

        regions = cast(list[str], d.pop("regions", UNSET))

        _quiet_hours = d.pop("quiet_hours", UNSET)
        quiet_hours: QuietHours | Unset
        if isinstance(_quiet_hours, Unset):
            quiet_hours = UNSET
        else:
            quiet_hours = QuietHours.from_dict(_quiet_hours)

        def _parse_disabled_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason", UNSET))

        def _parse_failing_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failing_since_type_0 = datetime.datetime.fromisoformat(data)

                return failing_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failing_since = _parse_failing_since(d.pop("failing_since", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        secret = d.pop("secret", UNSET)

        webhook_endpoint_with_secret = cls(
            id=id,
            format_=format_,
            url=url,
            events=events,
            default=default,
            enabled=enabled,
            status=status,
            created_at=created_at,
            apps=apps,
            regions=regions,
            quiet_hours=quiet_hours,
            disabled_reason=disabled_reason,
            failing_since=failing_since,
            description=description,
            secret=secret,
        )

        webhook_endpoint_with_secret.additional_properties = d
        return webhook_endpoint_with_secret

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

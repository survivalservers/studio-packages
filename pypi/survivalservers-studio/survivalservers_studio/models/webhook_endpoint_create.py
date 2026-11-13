from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_format import WebhookFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quiet_hours import QuietHours


T = TypeVar("T", bound="WebhookEndpointCreate")


@_attrs_define
class WebhookEndpointCreate:
    """
    Attributes:
        url (str): HTTPS only: a `https://hooks.slack.com/services/` address for `slack`, or a
            `https://discord.com/api/webhooks/` address for `discord`.
        format_ (WebhookFormat | Unset): `standard`: signed JSON to your own backend. `slack` and `discord`: a short
            message to a channel, from its webhook URL there. It is fixed once made. Default: WebhookFormat.STANDARD.
        events (list[str] | Unset): Event types; `game_server.*` style wildcards allowed. Default every event, or for
            `slack` and `discord` the alerts a team wants (failures, moved persistent servers, bulk actions stopped or
            finished, builds that failed, no ready servers, budget alerts).
        apps (list[str] | Unset): Only events about these apps (IDs or slugs), plus studio-wide ones such as billing.
            Empty takes every app.
        regions (list[str] | Unset): Only events in these regions, plus ones with no region. Empty takes every region.
        quiet_hours (QuietHours | Unset): `slack` and `discord` only. Critical alerts still go; the rest wait and go as
            one summary when quiet hours end.
        default (bool | Unset): `standard` only. Its secret also signs per-request `webhook_url` deliveries. Default:
            False.
        description (str | Unset): A note for your team; a channel's name in the panel.
    """

    url: str
    format_: WebhookFormat | Unset = WebhookFormat.STANDARD
    events: list[str] | Unset = UNSET
    apps: list[str] | Unset = UNSET
    regions: list[str] | Unset = UNSET
    quiet_hours: QuietHours | Unset = UNSET
    default: bool | Unset = False
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        quiet_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quiet_hours, Unset):
            quiet_hours = self.quiet_hours.to_dict()

        default = self.default

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if events is not UNSET:
            field_dict["events"] = events
        if apps is not UNSET:
            field_dict["apps"] = apps
        if regions is not UNSET:
            field_dict["regions"] = regions
        if quiet_hours is not UNSET:
            field_dict["quiet_hours"] = quiet_hours
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.quiet_hours import QuietHours

        d = dict(src_dict)
        url = d.pop("url")

        _format_ = d.pop("format", UNSET)
        format_: WebhookFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = WebhookFormat(_format_)

        events = cast(list[str], d.pop("events", UNSET))

        apps = cast(list[str], d.pop("apps", UNSET))

        regions = cast(list[str], d.pop("regions", UNSET))

        _quiet_hours = d.pop("quiet_hours", UNSET)
        quiet_hours: QuietHours | Unset
        if isinstance(_quiet_hours, Unset):
            quiet_hours = UNSET
        else:
            quiet_hours = QuietHours.from_dict(_quiet_hours)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        webhook_endpoint_create = cls(
            url=url,
            format_=format_,
            events=events,
            apps=apps,
            regions=regions,
            quiet_hours=quiet_hours,
            default=default,
            description=description,
        )

        webhook_endpoint_create.additional_properties = d
        return webhook_endpoint_create

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

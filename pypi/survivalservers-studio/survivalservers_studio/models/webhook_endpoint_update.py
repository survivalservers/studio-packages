from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quiet_hours import QuietHours


T = TypeVar("T", bound="WebhookEndpointUpdate")


@_attrs_define
class WebhookEndpointUpdate:
    """
    Attributes:
        url (str | Unset):
        events (list[str] | Unset):
        apps (list[str] | Unset):
        regions (list[str] | Unset):
        quiet_hours (None | QuietHours | Unset): `null` turns them off.
        default (bool | Unset):
        enabled (bool | Unset):
        description (str | Unset):
    """

    url: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    apps: list[str] | Unset = UNSET
    regions: list[str] | Unset = UNSET
    quiet_hours: None | QuietHours | Unset = UNSET
    default: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quiet_hours import QuietHours

        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        quiet_hours: dict[str, Any] | None | Unset
        if isinstance(self.quiet_hours, Unset):
            quiet_hours = UNSET
        elif isinstance(self.quiet_hours, QuietHours):
            quiet_hours = self.quiet_hours.to_dict()
        else:
            quiet_hours = self.quiet_hours

        default = self.default

        enabled = self.enabled

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.quiet_hours import QuietHours

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        apps = cast(list[str], d.pop("apps", UNSET))

        regions = cast(list[str], d.pop("regions", UNSET))

        def _parse_quiet_hours(data: object) -> None | QuietHours | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quiet_hours_type_0 = QuietHours.from_dict(data)

                return quiet_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuietHours | Unset, data)

        quiet_hours = _parse_quiet_hours(d.pop("quiet_hours", UNSET))

        default = d.pop("default", UNSET)

        enabled = d.pop("enabled", UNSET)

        description = d.pop("description", UNSET)

        webhook_endpoint_update = cls(
            url=url,
            events=events,
            apps=apps,
            regions=regions,
            quiet_hours=quiet_hours,
            default=default,
            enabled=enabled,
            description=description,
        )

        webhook_endpoint_update.additional_properties = d
        return webhook_endpoint_update

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

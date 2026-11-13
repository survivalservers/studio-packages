from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.studio_status import StudioStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.icon import Icon
    from ..models.studio_closed import StudioClosed
    from ..models.studio_free_tier import StudioFreeTier
    from ..models.studio_limits import StudioLimits
    from ..models.studio_suspension import StudioSuspension


T = TypeVar("T", bound="Studio")


@_attrs_define
class Studio:
    """
    Attributes:
        id (str): Studio ID.
        name (str): Its name.
        slug (str): Short name of lowercase letters, digits and dashes.
        status (StudioStatus):
        card_on_file (bool):
        card_needed (bool): True when new starts need a card (`402 card_required`) because the studio has no card on
            file and pays no other way agreed with us. False with a card on file, or when the studio pays another way agreed
            with us.
        free_tier (StudioFreeTier): This month's free vCPU-hours and how many are used. For a key limited to some apps,
            `cpu_hours_used` counts its apps' usage alone.
        limits (StudioLimits):
        price_locked_until (datetime.datetime):
        time_zone (str): A time zone by its IANA name (`America/Los_Angeles`, `Europe/Paris`, `UTC`). Only for showing
            times to people: the panel and emails show times in it, while the API always answers and takes times in UTC.
        created_at (datetime.datetime): When it was made.
        icon (Icon | None | Unset): Its icon; `null` when it has none.
        accent_color (None | str | Unset): The color of the studio's highlights and the first line of its charts in the
            panel; `null` when it has none (the panel's own).
        crash_dump_retention_hours (int | Unset): How long a crash dump is kept after it is stored, in hours (72 by
            default, at most 14 days).
        notice_contacts (list[str] | Unset): Up to 3 addresses that get notices of a data breach or a sub-processor
            change along with the Owners (DPA 7.3 and 9.1). Owners set them with `PATCH /v0/studio`.
        tax_number (str | Unset): The studio's tax registration number (a VAT, GST or EIN number), shown on every
            invoice made after it is set. Owners set it with `PATCH /v0/studio`. Left out when the studio has none, and for
            a key limited to some apps.
        suspension (None | StudioSuspension | Unset): For a suspended studio, when we suspended it and why, in the words
            our staff wrote for you (the email to its Owners says the same). Reads, downloads, `POST /v0/billing/portal-
            session` (to pay), and stopping or deleting its game servers, persistent servers and pools still work; nothing
            else can be started or changed until the suspension is lifted (`403 studio_suspended`). `null` while it is not
            suspended; `message` is `null` when no reason was given.
        closed (None | StudioClosed | Unset): For a closed studio, when it closed and what happens next: its Owners can
            read and download its data until `readable_until` (30 days), then everything is deleted by `deleted_by` (30 days
            more), except invoices, usage and the audit log, which are kept as the Data Retention Schedule says. `null`
            while it is not closed.
    """

    id: str
    name: str
    slug: str
    status: StudioStatus
    card_on_file: bool
    card_needed: bool
    free_tier: StudioFreeTier
    limits: StudioLimits
    price_locked_until: datetime.datetime
    time_zone: str
    created_at: datetime.datetime
    icon: Icon | None | Unset = UNSET
    accent_color: None | str | Unset = UNSET
    crash_dump_retention_hours: int | Unset = UNSET
    notice_contacts: list[str] | Unset = UNSET
    tax_number: str | Unset = UNSET
    suspension: None | StudioSuspension | Unset = UNSET
    closed: None | StudioClosed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.icon import Icon
        from ..models.studio_closed import StudioClosed
        from ..models.studio_suspension import StudioSuspension

        id = self.id

        name = self.name

        slug = self.slug

        status = self.status.value

        card_on_file = self.card_on_file

        card_needed = self.card_needed

        free_tier = self.free_tier.to_dict()

        limits = self.limits.to_dict()

        price_locked_until = self.price_locked_until.isoformat()

        time_zone = self.time_zone

        created_at = self.created_at.isoformat()

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, Icon):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        accent_color: None | str | Unset
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        crash_dump_retention_hours = self.crash_dump_retention_hours

        notice_contacts: list[str] | Unset = UNSET
        if not isinstance(self.notice_contacts, Unset):
            notice_contacts = self.notice_contacts

        tax_number = self.tax_number

        suspension: dict[str, Any] | None | Unset
        if isinstance(self.suspension, Unset):
            suspension = UNSET
        elif isinstance(self.suspension, StudioSuspension):
            suspension = self.suspension.to_dict()
        else:
            suspension = self.suspension

        closed: dict[str, Any] | None | Unset
        if isinstance(self.closed, Unset):
            closed = UNSET
        elif isinstance(self.closed, StudioClosed):
            closed = self.closed.to_dict()
        else:
            closed = self.closed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "status": status,
                "card_on_file": card_on_file,
                "card_needed": card_needed,
                "free_tier": free_tier,
                "limits": limits,
                "price_locked_until": price_locked_until,
                "time_zone": time_zone,
                "created_at": created_at,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if accent_color is not UNSET:
            field_dict["accent_color"] = accent_color
        if crash_dump_retention_hours is not UNSET:
            field_dict["crash_dump_retention_hours"] = crash_dump_retention_hours
        if notice_contacts is not UNSET:
            field_dict["notice_contacts"] = notice_contacts
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number
        if suspension is not UNSET:
            field_dict["suspension"] = suspension
        if closed is not UNSET:
            field_dict["closed"] = closed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.icon import Icon
        from ..models.studio_closed import StudioClosed
        from ..models.studio_free_tier import StudioFreeTier
        from ..models.studio_limits import StudioLimits
        from ..models.studio_suspension import StudioSuspension

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        status = StudioStatus(d.pop("status"))

        card_on_file = d.pop("card_on_file")

        card_needed = d.pop("card_needed")

        free_tier = StudioFreeTier.from_dict(d.pop("free_tier"))

        limits = StudioLimits.from_dict(d.pop("limits"))

        price_locked_until = datetime.datetime.fromisoformat(
            d.pop("price_locked_until")
        )

        time_zone = d.pop("time_zone")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_icon(data: object) -> Icon | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icon_type_0 = Icon.from_dict(data)

                return icon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Icon | None | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_accent_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accent_color = _parse_accent_color(d.pop("accent_color", UNSET))

        crash_dump_retention_hours = d.pop("crash_dump_retention_hours", UNSET)

        notice_contacts = cast(list[str], d.pop("notice_contacts", UNSET))

        tax_number = d.pop("tax_number", UNSET)

        def _parse_suspension(data: object) -> None | StudioSuspension | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                suspension_type_0 = StudioSuspension.from_dict(data)

                return suspension_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StudioSuspension | Unset, data)

        suspension = _parse_suspension(d.pop("suspension", UNSET))

        def _parse_closed(data: object) -> None | StudioClosed | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                closed_type_0 = StudioClosed.from_dict(data)

                return closed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StudioClosed | Unset, data)

        closed = _parse_closed(d.pop("closed", UNSET))

        studio = cls(
            id=id,
            name=name,
            slug=slug,
            status=status,
            card_on_file=card_on_file,
            card_needed=card_needed,
            free_tier=free_tier,
            limits=limits,
            price_locked_until=price_locked_until,
            time_zone=time_zone,
            created_at=created_at,
            icon=icon,
            accent_color=accent_color,
            crash_dump_retention_hours=crash_dump_retention_hours,
            notice_contacts=notice_contacts,
            tax_number=tax_number,
            suspension=suspension,
            closed=closed,
        )

        studio.additional_properties = d
        return studio

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

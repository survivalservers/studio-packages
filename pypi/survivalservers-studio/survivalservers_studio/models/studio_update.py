from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StudioUpdate")


@_attrs_define
class StudioUpdate:
    """
    Attributes:
        name (str | Unset): The new display name.
        accent_color (None | str | Unset): The new accent color, or `null` to go back to the panel's own.
        time_zone (str | Unset): A time zone by its IANA name (`America/Los_Angeles`, `Europe/Paris`, `UTC`). Only for
            showing times to people: the panel and emails show times in it, while the API always answers and takes times in
            UTC.
        crash_dump_retention_hours (int | Unset): How long crash dumps are kept, in hours (1 to 336, 14 days). Lower, it
            shortens the dumps already kept too, each to the time it was stored plus the new hours (never later than
            before); those then due go within the hour.
        notice_contacts (list[str] | Unset): The whole new list of notice contacts (up to 3 addresses; `[]` for none):
            they get notices of a data breach or a sub-processor change along with the Owners. Owners only, from the panel
            (`403 key_restricted` otherwise).
        tax_number (None | str | Unset): The studio's tax registration number, as it should read on its invoices (up to
            40 characters), or `null` to remove it. Every invoice made after the change shows it. Owners only, from the
            panel (`403 key_restricted` otherwise).
    """

    name: str | Unset = UNSET
    accent_color: None | str | Unset = UNSET
    time_zone: str | Unset = UNSET
    crash_dump_retention_hours: int | Unset = UNSET
    notice_contacts: list[str] | Unset = UNSET
    tax_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        accent_color: None | str | Unset
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        time_zone = self.time_zone

        crash_dump_retention_hours = self.crash_dump_retention_hours

        notice_contacts: list[str] | Unset = UNSET
        if not isinstance(self.notice_contacts, Unset):
            notice_contacts = self.notice_contacts

        tax_number: None | str | Unset
        if isinstance(self.tax_number, Unset):
            tax_number = UNSET
        else:
            tax_number = self.tax_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if accent_color is not UNSET:
            field_dict["accent_color"] = accent_color
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if crash_dump_retention_hours is not UNSET:
            field_dict["crash_dump_retention_hours"] = crash_dump_retention_hours
        if notice_contacts is not UNSET:
            field_dict["notice_contacts"] = notice_contacts
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_accent_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accent_color = _parse_accent_color(d.pop("accent_color", UNSET))

        time_zone = d.pop("time_zone", UNSET)

        crash_dump_retention_hours = d.pop("crash_dump_retention_hours", UNSET)

        notice_contacts = cast(list[str], d.pop("notice_contacts", UNSET))

        def _parse_tax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_number = _parse_tax_number(d.pop("tax_number", UNSET))

        studio_update = cls(
            name=name,
            accent_color=accent_color,
            time_zone=time_zone,
            crash_dump_retention_hours=crash_dump_retention_hours,
            notice_contacts=notice_contacts,
            tax_number=tax_number,
        )

        studio_update.additional_properties = d
        return studio_update

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

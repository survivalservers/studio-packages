from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_status import MembershipStatus
from ..models.role import Role
from ..models.scope import Scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.icon import Icon


T = TypeVar("T", bound="Membership")


@_attrs_define
class Membership:
    """One studio a person belongs to, with their role and what the role allows.

    Attributes:
        id (str): Studio ID.
        name (str): Its name.
        slug (str): Short name of lowercase letters, digits and dashes.
        role (Role):
        time_zone (str): A time zone by its IANA name (`America/Los_Angeles`, `Europe/Paris`, `UTC`). Only for showing
            times to people: the panel and emails show times in it, while the API always answers and takes times in UTC.
        scopes (list[Scope]):
        crash_dumps (bool | Unset): Whether you may list and download its crash dumps (an owner or admin with the crash-
            dump permission).
        icon (Icon | None | Unset): Its icon; `null` when it has none.
        accent_color (None | str | Unset): The color of the studio's highlights and the first line of its charts in the
            panel; `null` when it has none (the panel's own).
        status (MembershipStatus | Unset): The studio's state. A closed studio is listed only for its Owners, while it
            is readable (see `closed` on `GET /v0/studio`).
    """

    id: str
    name: str
    slug: str
    role: Role
    time_zone: str
    scopes: list[Scope]
    crash_dumps: bool | Unset = UNSET
    icon: Icon | None | Unset = UNSET
    accent_color: None | str | Unset = UNSET
    status: MembershipStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.icon import Icon

        id = self.id

        name = self.name

        slug = self.slug

        role = self.role.value

        time_zone = self.time_zone

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        crash_dumps = self.crash_dumps

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "role": role,
                "time_zone": time_zone,
                "scopes": scopes,
            }
        )
        if crash_dumps is not UNSET:
            field_dict["crash_dumps"] = crash_dumps
        if icon is not UNSET:
            field_dict["icon"] = icon
        if accent_color is not UNSET:
            field_dict["accent_color"] = accent_color
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.icon import Icon

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        role = Role(d.pop("role"))

        time_zone = d.pop("time_zone")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = Scope(scopes_item_data)

            scopes.append(scopes_item)

        crash_dumps = d.pop("crash_dumps", UNSET)

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

        _status = d.pop("status", UNSET)
        status: MembershipStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MembershipStatus(_status)

        membership = cls(
            id=id,
            name=name,
            slug=slug,
            role=role,
            time_zone=time_zone,
            scopes=scopes,
            crash_dumps=crash_dumps,
            icon=icon,
            accent_color=accent_color,
            status=status,
        )

        membership.additional_properties = d
        return membership

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

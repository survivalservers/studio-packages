from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..models.tier import Tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.banner import Banner
    from ..models.branch_map import BranchMap
    from ..models.default_placement import DefaultPlacement
    from ..models.icon import Icon


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """
    Attributes:
        id (str): App ID.
        name (str): Its name.
        slug (str): Short name of lowercase letters, digits and dashes.
        os (Os):
        tier (Tier): Public hardware tier.
        default_placement (DefaultPlacement): Used by starts that send no `placement`.
        branches (BranchMap): Branch name to version name.
        created_at (datetime.datetime): When it was made.
        updated_at (datetime.datetime): When it last changed.
        icon (Icon | None | Unset): Its icon; `null` when it has none.
        color (None | str | Unset): Its color in the panel's charts, tags and rows; `null` when it has none (the panel
            makes one from the name).
        banner (Banner | None | Unset): Its banner; `null` when it has none.
        deleted_at (datetime.datetime | None | Unset): When it was deleted; `null` while it exists. Only listed with
            `include_deleted=true`.
    """

    id: str
    name: str
    slug: str
    os: Os
    tier: Tier
    default_placement: DefaultPlacement
    branches: BranchMap
    created_at: datetime.datetime
    updated_at: datetime.datetime
    icon: Icon | None | Unset = UNSET
    color: None | str | Unset = UNSET
    banner: Banner | None | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.banner import Banner
        from ..models.icon import Icon

        id = self.id

        name = self.name

        slug = self.slug

        os = self.os.value

        tier = self.tier.value

        default_placement = self.default_placement.to_dict()

        branches = self.branches.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, Icon):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        banner: dict[str, Any] | None | Unset
        if isinstance(self.banner, Unset):
            banner = UNSET
        elif isinstance(self.banner, Banner):
            banner = self.banner.to_dict()
        else:
            banner = self.banner

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "os": os,
                "tier": tier,
                "default_placement": default_placement,
                "branches": branches,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if color is not UNSET:
            field_dict["color"] = color
        if banner is not UNSET:
            field_dict["banner"] = banner
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.banner import Banner
        from ..models.branch_map import BranchMap
        from ..models.default_placement import DefaultPlacement
        from ..models.icon import Icon

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        os = Os(d.pop("os"))

        tier = Tier(d.pop("tier"))

        default_placement = DefaultPlacement.from_dict(d.pop("default_placement"))

        branches = BranchMap.from_dict(d.pop("branches"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_banner(data: object) -> Banner | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                banner_type_0 = Banner.from_dict(data)

                return banner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Banner | None | Unset, data)

        banner = _parse_banner(d.pop("banner", UNSET))

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        app = cls(
            id=id,
            name=name,
            slug=slug,
            os=os,
            tier=tier,
            default_placement=default_placement,
            branches=branches,
            created_at=created_at,
            updated_at=updated_at,
            icon=icon,
            color=color,
            banner=banner,
            deleted_at=deleted_at,
        )

        app.additional_properties = d
        return app

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

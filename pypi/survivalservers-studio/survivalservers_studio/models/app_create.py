from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..models.tier import Tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.default_placement import DefaultPlacement


T = TypeVar("T", bound="AppCreate")


@_attrs_define
class AppCreate:
    """
    Attributes:
        name (str):
        os (Os):
        slug (str | Unset): Short name of lowercase letters, digits and dashes.
        tier (Tier | Unset): Public hardware tier. Default: Tier.STANDARD.
        default_placement (DefaultPlacement | Unset): Used by starts that send no `placement`.
        color (str | Unset): A color as `#rrggbb` (answers are lower case). The panel lightens one that would be hard to
            read on its dark pages.
    """

    name: str
    os: Os
    slug: str | Unset = UNSET
    tier: Tier | Unset = Tier.STANDARD
    default_placement: DefaultPlacement | Unset = UNSET
    color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        os = self.os.value

        slug = self.slug

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        default_placement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_placement, Unset):
            default_placement = self.default_placement.to_dict()

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "os": os,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tier is not UNSET:
            field_dict["tier"] = tier
        if default_placement is not UNSET:
            field_dict["default_placement"] = default_placement
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.default_placement import DefaultPlacement

        d = dict(src_dict)
        name = d.pop("name")

        os = Os(d.pop("os"))

        slug = d.pop("slug", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: Tier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = Tier(_tier)

        _default_placement = d.pop("default_placement", UNSET)
        default_placement: DefaultPlacement | Unset
        if isinstance(_default_placement, Unset):
            default_placement = UNSET
        else:
            default_placement = DefaultPlacement.from_dict(_default_placement)

        color = d.pop("color", UNSET)

        app_create = cls(
            name=name,
            os=os,
            slug=slug,
            tier=tier,
            default_placement=default_placement,
            color=color,
        )

        app_create.additional_properties = d
        return app_create

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StudioCreate")


@_attrs_define
class StudioCreate:
    """
    Attributes:
        name (str):
        slug (str | Unset): Short name of lowercase letters, digits and dashes.
        time_zone (str | Unset): A time zone by its IANA name (`America/Los_Angeles`, `Europe/Paris`, `UTC`). Only for
            showing times to people: the panel and emails show times in it, while the API always answers and takes times in
            UTC.
        terms_version (str | Unset): A version of the terms, like `1.0`.
    """

    name: str
    slug: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    terms_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        time_zone = self.time_zone

        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        studio_create = cls(
            name=name,
            slug=slug,
            time_zone=time_zone,
            terms_version=terms_version,
        )

        studio_create.additional_properties = d
        return studio_create

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

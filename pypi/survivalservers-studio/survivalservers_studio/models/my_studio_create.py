from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyStudioCreate")


@_attrs_define
class MyStudioCreate:
    """
    Attributes:
        time_zone (str | Unset): A time zone by its IANA name (`America/Los_Angeles`, `Europe/Paris`, `UTC`). Only for
            showing times to people: the panel and emails show times in it, while the API always answers and takes times in
            UTC.
        ignore_invitations (bool | Unset): Make it even though invitations are waiting (the person chose their own
            studio). `false` when left out.
        terms_version (str | Unset): A version of the terms, like `1.0`.
    """

    time_zone: str | Unset = UNSET
    ignore_invitations: bool | Unset = UNSET
    terms_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone = self.time_zone

        ignore_invitations = self.ignore_invitations

        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if ignore_invitations is not UNSET:
            field_dict["ignore_invitations"] = ignore_invitations
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time_zone = d.pop("time_zone", UNSET)

        ignore_invitations = d.pop("ignore_invitations", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        my_studio_create = cls(
            time_zone=time_zone,
            ignore_invitations=ignore_invitations,
            terms_version=terms_version,
        )

        my_studio_create.additional_properties = d
        return my_studio_create

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

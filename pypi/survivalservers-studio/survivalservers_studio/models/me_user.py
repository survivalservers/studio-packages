from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeUser")


@_attrs_define
class MeUser:
    """
    Attributes:
        id (str): Person ID.
        email (str):
        name (None | str | Unset):
        mfa_enabled (bool | Unset):
        company_sign_in (bool | Unset): This sign-in came through a studio's own sign-in provider (single sign-on); the
            company then keeps the person's name, password and 2FA.
        time_zone (None | str | Unset): The time zone this person picked for the panel; `null` means each studio's own.
    """

    id: str
    email: str
    name: None | str | Unset = UNSET
    mfa_enabled: bool | Unset = UNSET
    company_sign_in: bool | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        mfa_enabled = self.mfa_enabled

        company_sign_in = self.company_sign_in

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if mfa_enabled is not UNSET:
            field_dict["mfa_enabled"] = mfa_enabled
        if company_sign_in is not UNSET:
            field_dict["company_sign_in"] = company_sign_in
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        mfa_enabled = d.pop("mfa_enabled", UNSET)

        company_sign_in = d.pop("company_sign_in", UNSET)

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        me_user = cls(
            id=id,
            email=email,
            name=name,
            mfa_enabled=mfa_enabled,
            company_sign_in=company_sign_in,
            time_zone=time_zone,
        )

        me_user.additional_properties = d
        return me_user

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

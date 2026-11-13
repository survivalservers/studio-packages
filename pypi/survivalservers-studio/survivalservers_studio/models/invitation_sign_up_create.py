from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationSignUpCreate")


@_attrs_define
class InvitationSignUpCreate:
    """
    Attributes:
        token (str): The token from the invitation link.
        website (str | Unset): Leave empty. The page hides it from people.
        terms_version (str | Unset): A version of the terms, like `1.0`.
    """

    token: str
    website: str | Unset = UNSET
    terms_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        website = self.website

        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
            }
        )
        if website is not UNSET:
            field_dict["website"] = website
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        website = d.pop("website", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        invitation_sign_up_create = cls(
            token=token,
            website=website,
            terms_version=terms_version,
        )

        return invitation_sign_up_create

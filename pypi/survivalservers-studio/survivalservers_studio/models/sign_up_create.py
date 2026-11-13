from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignUpCreate")


@_attrs_define
class SignUpCreate:
    """
    Attributes:
        email (str): The address to sign up with.
        return_to (str | Unset): A path on the panel the link leads back to (default `/`).
        website (str | Unset): Leave empty. The form hides it from people.
        terms_version (str | Unset): A version of the terms, like `1.0`.
    """

    email: str
    return_to: str | Unset = UNSET
    website: str | Unset = UNSET
    terms_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        return_to = self.return_to

        website = self.website

        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if return_to is not UNSET:
            field_dict["return_to"] = return_to
        if website is not UNSET:
            field_dict["website"] = website
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        return_to = d.pop("return_to", UNSET)

        website = d.pop("website", UNSET)

        terms_version = d.pop("terms_version", UNSET)

        sign_up_create = cls(
            email=email,
            return_to=return_to,
            website=website,
            terms_version=terms_version,
        )

        return sign_up_create

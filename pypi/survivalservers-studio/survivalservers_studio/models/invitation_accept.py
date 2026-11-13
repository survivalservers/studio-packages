from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationAccept")


@_attrs_define
class InvitationAccept:
    """
    Attributes:
        terms_version (str | Unset): A version of the terms, like `1.0`.
    """

    terms_version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        terms_version = self.terms_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if terms_version is not UNSET:
            field_dict["terms_version"] = terms_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        terms_version = d.pop("terms_version", UNSET)

        invitation_accept = cls(
            terms_version=terms_version,
        )

        return invitation_accept

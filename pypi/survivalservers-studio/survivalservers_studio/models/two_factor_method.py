from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method_kind import TwoFactorMethodKind

T = TypeVar("T", bound="TwoFactorMethod")


@_attrs_define
class TwoFactorMethod:
    """
    Attributes:
        id (str): The method's own ID: Profile's Remove names it to the sign-in's removal step.
        kind (TwoFactorMethodKind): `passkey` (a passkey on a phone or computer, which also signs the person in by
            itself), `security_key` (a security key asked for after the password), `app` (an authenticator app's code) or
            `text` (a code texted to a phone number; while texts are off such a number signs nobody in).
        name (None | str): The name it was given when it was set up; `null` when it has none.
        added_at (datetime.datetime | None): When it was set up; `null` when the sign-in does not know.
    """

    id: str
    kind: TwoFactorMethodKind
    name: None | str
    added_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        name: None | str
        name = self.name

        added_at: None | str
        if isinstance(self.added_at, datetime.datetime):
            added_at = self.added_at.isoformat()
        else:
            added_at = self.added_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "name": name,
                "added_at": added_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = TwoFactorMethodKind(d.pop("kind"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_added_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_at_type_0 = datetime.datetime.fromisoformat(data)

                return added_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        added_at = _parse_added_at(d.pop("added_at"))

        two_factor_method = cls(
            id=id,
            kind=kind,
            name=name,
            added_at=added_at,
        )

        two_factor_method.additional_properties = d
        return two_factor_method

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

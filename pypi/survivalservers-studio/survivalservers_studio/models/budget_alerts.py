from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetAlerts")


@_attrs_define
class BudgetAlerts:
    """
    Attributes:
        thresholds_usd (list[str]):
        email (list[str] | Unset):
        unconfirmed (list[str] | Unset): Read only, in answers: the addresses on the list that are not a member's sign-
            in email and have not confirmed yet, which get no alert until they do. A `PUT` ignores it.
        held_back_at (datetime.datetime | None | Unset): Read only, in answers: when the studio's daily limit of 20
            budget alert emails last held an alert back, in the past 30 days; left out when none was. A `PUT` ignores it.
    """

    thresholds_usd: list[str]
    email: list[str] | Unset = UNSET
    unconfirmed: list[str] | Unset = UNSET
    held_back_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thresholds_usd = self.thresholds_usd

        email: list[str] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email

        unconfirmed: list[str] | Unset = UNSET
        if not isinstance(self.unconfirmed, Unset):
            unconfirmed = self.unconfirmed

        held_back_at: None | str | Unset
        if isinstance(self.held_back_at, Unset):
            held_back_at = UNSET
        elif isinstance(self.held_back_at, datetime.datetime):
            held_back_at = self.held_back_at.isoformat()
        else:
            held_back_at = self.held_back_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thresholds_usd": thresholds_usd,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if unconfirmed is not UNSET:
            field_dict["unconfirmed"] = unconfirmed
        if held_back_at is not UNSET:
            field_dict["held_back_at"] = held_back_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        thresholds_usd = cast(list[str], d.pop("thresholds_usd"))

        email = cast(list[str], d.pop("email", UNSET))

        unconfirmed = cast(list[str], d.pop("unconfirmed", UNSET))

        def _parse_held_back_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                held_back_at_type_0 = datetime.datetime.fromisoformat(data)

                return held_back_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        held_back_at = _parse_held_back_at(d.pop("held_back_at", UNSET))

        budget_alerts = cls(
            thresholds_usd=thresholds_usd,
            email=email,
            unconfirmed=unconfirmed,
            held_back_at=held_back_at,
        )

        budget_alerts.additional_properties = d
        return budget_alerts

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

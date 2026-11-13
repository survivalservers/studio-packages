from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_kind import CreditKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credit")


@_attrs_define
class Credit:
    """
    Attributes:
        id (str): Credit ID.
        period (str):
        kind (CreditKind):
        amount_usd (str): USD as a decimal string.
        created_at (datetime.datetime): When it was made.
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        continent (str | Unset): `north-america`, `europe`, `asia`, `oceania`, `south-america`, `middle-east`, `africa`.
        reason (str | Unset):
        invoice (str | Unset): Invoice ID.
    """

    id: str
    period: str
    kind: CreditKind
    amount_usd: str
    created_at: datetime.datetime
    region: str | Unset = UNSET
    continent: str | Unset = UNSET
    reason: str | Unset = UNSET
    invoice: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        period = self.period

        kind = self.kind.value

        amount_usd = self.amount_usd

        created_at = self.created_at.isoformat()

        region = self.region

        continent = self.continent

        reason = self.reason

        invoice = self.invoice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "period": period,
                "kind": kind,
                "amount_usd": amount_usd,
                "created_at": created_at,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if continent is not UNSET:
            field_dict["continent"] = continent
        if reason is not UNSET:
            field_dict["reason"] = reason
        if invoice is not UNSET:
            field_dict["invoice"] = invoice

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        period = d.pop("period")

        kind = CreditKind(d.pop("kind"))

        amount_usd = d.pop("amount_usd")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        region = d.pop("region", UNSET)

        continent = d.pop("continent", UNSET)

        reason = d.pop("reason", UNSET)

        invoice = d.pop("invoice", UNSET)

        credit = cls(
            id=id,
            period=period,
            kind=kind,
            amount_usd=amount_usd,
            created_at=created_at,
            region=region,
            continent=continent,
            reason=reason,
            invoice=invoice,
        )

        credit.additional_properties = d
        return credit

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

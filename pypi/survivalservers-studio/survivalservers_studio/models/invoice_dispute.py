from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_dispute_status import InvoiceDisputeStatus

T = TypeVar("T", bound="InvoiceDispute")


@_attrs_define
class InvoiceDispute:
    """
    Attributes:
        status (InvoiceDisputeStatus):
        amount_usd (str): USD as a decimal string.
        opened_at (datetime.datetime):
        closed_at (datetime.datetime | None):
    """

    status: InvoiceDisputeStatus
    amount_usd: str
    opened_at: datetime.datetime
    closed_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        amount_usd = self.amount_usd

        opened_at = self.opened_at.isoformat()

        closed_at: None | str
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "amount_usd": amount_usd,
                "opened_at": opened_at,
                "closed_at": closed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = InvoiceDisputeStatus(d.pop("status"))

        amount_usd = d.pop("amount_usd")

        opened_at = datetime.datetime.fromisoformat(d.pop("opened_at"))

        def _parse_closed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        invoice_dispute = cls(
            status=status,
            amount_usd=amount_usd,
            opened_at=opened_at,
            closed_at=closed_at,
        )

        invoice_dispute.additional_properties = d
        return invoice_dispute

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

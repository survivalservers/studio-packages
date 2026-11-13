from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.invoice_line import InvoiceLine


T = TypeVar("T", bound="UpcomingInvoice")


@_attrs_define
class UpcomingInvoice:
    """
    Attributes:
        period (str): The month it is for.
        as_of (datetime.datetime): When it was worked out (at most a minute ago).
        subtotal_usd (str): USD as a decimal string.
        credits_usd (str): USD as a decimal string.
        total_usd (str): USD as a decimal string.
        lines (list[InvoiceLine]):
    """

    period: str
    as_of: datetime.datetime
    subtotal_usd: str
    credits_usd: str
    total_usd: str
    lines: list[InvoiceLine]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        as_of = self.as_of.isoformat()

        subtotal_usd = self.subtotal_usd

        credits_usd = self.credits_usd

        total_usd = self.total_usd

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "as_of": as_of,
                "subtotal_usd": subtotal_usd,
                "credits_usd": credits_usd,
                "total_usd": total_usd,
                "lines": lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invoice_line import InvoiceLine

        d = dict(src_dict)
        period = d.pop("period")

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        subtotal_usd = d.pop("subtotal_usd")

        credits_usd = d.pop("credits_usd")

        total_usd = d.pop("total_usd")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceLine.from_dict(lines_item_data)

            lines.append(lines_item)

        upcoming_invoice = cls(
            period=period,
            as_of=as_of,
            subtotal_usd=subtotal_usd,
            credits_usd=credits_usd,
            total_usd=total_usd,
            lines=lines,
        )

        upcoming_invoice.additional_properties = d
        return upcoming_invoice

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

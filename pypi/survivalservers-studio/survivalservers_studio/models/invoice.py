from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_dispute import InvoiceDispute
    from ..models.invoice_line import InvoiceLine


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        id (str): Invoice ID.
        period (str):
        status (InvoiceStatus):
        subtotal_usd (str): USD as a decimal string.
        credits_usd (str): USD as a decimal string.
        total_usd (str): USD as a decimal string.
        lines (list[InvoiceLine]):
        created_at (datetime.datetime): When it was made.
        refunded_usd (str): USD as a decimal string.
        dispute (InvoiceDispute | None): The newest card dispute of this invoice's payment with your bank, or `null`.
            While one is `open`, or `lost` and not settled yet with
            [support](https://studio.survivalservers.com/docs/help/get-help/), new starts are refused; game servers already
            running keep running (`402 payment_disputed`).
        hosted_invoice_url (None | str | Unset):
        due_at (datetime.datetime | None | Unset):
        paid_at (datetime.datetime | None | Unset):
    """

    id: str
    period: str
    status: InvoiceStatus
    subtotal_usd: str
    credits_usd: str
    total_usd: str
    lines: list[InvoiceLine]
    created_at: datetime.datetime
    refunded_usd: str
    dispute: InvoiceDispute | None
    hosted_invoice_url: None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    paid_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_dispute import InvoiceDispute

        id = self.id

        period = self.period

        status = self.status.value

        subtotal_usd = self.subtotal_usd

        credits_usd = self.credits_usd

        total_usd = self.total_usd

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        created_at = self.created_at.isoformat()

        refunded_usd = self.refunded_usd

        dispute: dict[str, Any] | None
        if isinstance(self.dispute, InvoiceDispute):
            dispute = self.dispute.to_dict()
        else:
            dispute = self.dispute

        hosted_invoice_url: None | str | Unset
        if isinstance(self.hosted_invoice_url, Unset):
            hosted_invoice_url = UNSET
        else:
            hosted_invoice_url = self.hosted_invoice_url

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "period": period,
                "status": status,
                "subtotal_usd": subtotal_usd,
                "credits_usd": credits_usd,
                "total_usd": total_usd,
                "lines": lines,
                "created_at": created_at,
                "refunded_usd": refunded_usd,
                "dispute": dispute,
            }
        )
        if hosted_invoice_url is not UNSET:
            field_dict["hosted_invoice_url"] = hosted_invoice_url
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invoice_dispute import InvoiceDispute
        from ..models.invoice_line import InvoiceLine

        d = dict(src_dict)
        id = d.pop("id")

        period = d.pop("period")

        status = InvoiceStatus(d.pop("status"))

        subtotal_usd = d.pop("subtotal_usd")

        credits_usd = d.pop("credits_usd")

        total_usd = d.pop("total_usd")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = InvoiceLine.from_dict(lines_item_data)

            lines.append(lines_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        refunded_usd = d.pop("refunded_usd")

        def _parse_dispute(data: object) -> InvoiceDispute | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dispute_type_0 = InvoiceDispute.from_dict(data)

                return dispute_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoiceDispute | None, data)

        dispute = _parse_dispute(d.pop("dispute"))

        def _parse_hosted_invoice_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hosted_invoice_url = _parse_hosted_invoice_url(
            d.pop("hosted_invoice_url", UNSET)
        )

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        def _parse_paid_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = datetime.datetime.fromisoformat(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))

        invoice = cls(
            id=id,
            period=period,
            status=status,
            subtotal_usd=subtotal_usd,
            credits_usd=credits_usd,
            total_usd=total_usd,
            lines=lines,
            created_at=created_at,
            refunded_usd=refunded_usd,
            dispute=dispute,
            hosted_invoice_url=hosted_invoice_url,
            due_at=due_at,
            paid_at=paid_at,
        )

        invoice.additional_properties = d
        return invoice

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

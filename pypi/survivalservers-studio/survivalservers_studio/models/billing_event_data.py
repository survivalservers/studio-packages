from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_event_data_percent import BillingEventDataPercent
from ..models.event_object_meta_object import EventObjectMetaObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingEventData")


@_attrs_define
class BillingEventData:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
        period (str | Unset):
        threshold_usd (str | Unset): USD as a decimal string.
        projected_month_usd (str | Unset): USD as a decimal string.
        invoice (str | Unset): Invoice ID.
        total_usd (str | Unset): USD as a decimal string.
        starts_stop_at (datetime.datetime | Unset): `billing.payment_failed` only. When new starts are refused if it
            stays unpaid.
        free_vcpu_hours (int | Unset): `billing.free_hours` only. The month's free vCPU-hours.
        used_vcpu_hours (float | Unset): `billing.free_hours` only. The free vCPU-hours used so far this month, as the
            invoice counts them.
        percent (BillingEventDataPercent | Unset): `billing.free_hours` only. The step passed: 80, or 100 when they are
            used up. Each is sent once a month.
        past_due (bool | Unset): `billing.payment_failed` only. True when no payment failed: an emailed invoice (no card
            on file) passed its due date unpaid, which starts the same clock, from the due date.
    """

    object_: EventObjectMetaObject
    sequence: int
    period: str | Unset = UNSET
    threshold_usd: str | Unset = UNSET
    projected_month_usd: str | Unset = UNSET
    invoice: str | Unset = UNSET
    total_usd: str | Unset = UNSET
    starts_stop_at: datetime.datetime | Unset = UNSET
    free_vcpu_hours: int | Unset = UNSET
    used_vcpu_hours: float | Unset = UNSET
    percent: BillingEventDataPercent | Unset = UNSET
    past_due: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        sequence = self.sequence

        period = self.period

        threshold_usd = self.threshold_usd

        projected_month_usd = self.projected_month_usd

        invoice = self.invoice

        total_usd = self.total_usd

        starts_stop_at: str | Unset = UNSET
        if not isinstance(self.starts_stop_at, Unset):
            starts_stop_at = self.starts_stop_at.isoformat()

        free_vcpu_hours = self.free_vcpu_hours

        used_vcpu_hours = self.used_vcpu_hours

        percent: int | Unset = UNSET
        if not isinstance(self.percent, Unset):
            percent = self.percent.value

        past_due = self.past_due

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period
        if threshold_usd is not UNSET:
            field_dict["threshold_usd"] = threshold_usd
        if projected_month_usd is not UNSET:
            field_dict["projected_month_usd"] = projected_month_usd
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if total_usd is not UNSET:
            field_dict["total_usd"] = total_usd
        if starts_stop_at is not UNSET:
            field_dict["starts_stop_at"] = starts_stop_at
        if free_vcpu_hours is not UNSET:
            field_dict["free_vcpu_hours"] = free_vcpu_hours
        if used_vcpu_hours is not UNSET:
            field_dict["used_vcpu_hours"] = used_vcpu_hours
        if percent is not UNSET:
            field_dict["percent"] = percent
        if past_due is not UNSET:
            field_dict["past_due"] = past_due

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        period = d.pop("period", UNSET)

        threshold_usd = d.pop("threshold_usd", UNSET)

        projected_month_usd = d.pop("projected_month_usd", UNSET)

        invoice = d.pop("invoice", UNSET)

        total_usd = d.pop("total_usd", UNSET)

        _starts_stop_at = d.pop("starts_stop_at", UNSET)
        starts_stop_at: datetime.datetime | Unset
        if isinstance(_starts_stop_at, Unset):
            starts_stop_at = UNSET
        else:
            starts_stop_at = datetime.datetime.fromisoformat(_starts_stop_at)

        free_vcpu_hours = d.pop("free_vcpu_hours", UNSET)

        used_vcpu_hours = d.pop("used_vcpu_hours", UNSET)

        _percent = d.pop("percent", UNSET)
        percent: BillingEventDataPercent | Unset
        if isinstance(_percent, Unset):
            percent = UNSET
        else:
            percent = BillingEventDataPercent(_percent)

        past_due = d.pop("past_due", UNSET)

        billing_event_data = cls(
            object_=object_,
            sequence=sequence,
            period=period,
            threshold_usd=threshold_usd,
            projected_month_usd=projected_month_usd,
            invoice=invoice,
            total_usd=total_usd,
            starts_stop_at=starts_stop_at,
            free_vcpu_hours=free_vcpu_hours,
            used_vcpu_hours=used_vcpu_hours,
            percent=percent,
            past_due=past_due,
        )

        billing_event_data.additional_properties = d
        return billing_event_data

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

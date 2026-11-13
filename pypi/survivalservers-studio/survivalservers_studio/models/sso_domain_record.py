from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SsoDomainRecord")


@_attrs_define
class SsoDomainRecord:
    """
    Attributes:
        domain (str):
        record_name (str): The TXT record's name.
        record_value (str): Its value.
        verified (bool): The record was found; the domain is yours.
    """

    domain: str
    record_name: str
    record_value: str
    verified: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        record_name = self.record_name

        record_value = self.record_value

        verified = self.verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "record_name": record_name,
                "record_value": record_value,
                "verified": verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        domain = d.pop("domain")

        record_name = d.pop("record_name")

        record_value = d.pop("record_value")

        verified = d.pop("verified")

        sso_domain_record = cls(
            domain=domain,
            record_name=record_name,
            record_value=record_value,
            verified=verified,
        )

        sso_domain_record.additional_properties = d
        return sso_domain_record

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

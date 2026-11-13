from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MachineEnrollment")


@_attrs_define
class MachineEnrollment:
    """
    Attributes:
        token (str): One use. Pass it to the machine agent's `enroll` command; it is never shown again.
        expires_at (datetime.datetime):
        enroll_url (str): The address the machine agent enrolls at.
    """

    token: str
    expires_at: datetime.datetime
    enroll_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        expires_at = self.expires_at.isoformat()

        enroll_url = self.enroll_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "expires_at": expires_at,
                "enroll_url": enroll_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        enroll_url = d.pop("enroll_url")

        machine_enrollment = cls(
            token=token,
            expires_at=expires_at,
            enroll_url=enroll_url,
        )

        machine_enrollment.additional_properties = d
        return machine_enrollment

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolFailedStart")


@_attrs_define
class PoolFailedStart:
    """
    Attributes:
        at (datetime.datetime): When it ended.
        reason (str): `crashed`, `boot_timeout` (not ready within the version's boot timeout), `health_timeout`,
            `out_of_memory`, `out_of_disk` or `self` (its program quit); new reasons may be added.
        exit_code (int | None):
        detail (str): A sentence, such as "Exited with code 1 before its ready check, within a second of starting."
    """

    at: datetime.datetime
    reason: str
    exit_code: int | None
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        reason = self.reason

        exit_code: int | None
        exit_code = self.exit_code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
                "reason": reason,
                "exit_code": exit_code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        reason = d.pop("reason")

        def _parse_exit_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_code = _parse_exit_code(d.pop("exit_code"))

        detail = d.pop("detail")

        pool_failed_start = cls(
            at=at,
            reason=reason,
            exit_code=exit_code,
            detail=detail,
        )

        pool_failed_start.additional_properties = d
        return pool_failed_start

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

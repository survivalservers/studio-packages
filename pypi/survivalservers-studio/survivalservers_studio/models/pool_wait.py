from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolWait")


@_attrs_define
class PoolWait:
    """
    Attributes:
        code (str): Why it cannot start a ready server now: `no_capacity`, `not_offered`, `version_not_ready`,
            `limit_reached` (the studio's running vCPUs are at its limit; waiting game servers count), `card_required` (the
            studio's starts need a card; the waiting ones stay), `payment_disputed` (a card payment is disputed with the
            bank, or a lost dispute isn't settled yet; the waiting ones stay), or `studio_suspended` and `studio_closed` (it
            keeps none: they are stopped and `target` reads 0); new codes may be added.
        detail (str): A sentence that says what it waits for and, where there is one, what to change, such as "Waiting
            for room: no machine in Europe West has room for 1 vCPU and 1 GB for this studio now. The pool starts its
            servers as soon as room frees."
        since (datetime.datetime): The first pool round that met this reason.
    """

    code: str
    detail: str
    since: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        detail = self.detail

        since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "detail": detail,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        detail = d.pop("detail")

        since = datetime.datetime.fromisoformat(d.pop("since"))

        pool_wait = cls(
            code=code,
            detail=detail,
            since=since,
        )

        pool_wait.additional_properties = d
        return pool_wait

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

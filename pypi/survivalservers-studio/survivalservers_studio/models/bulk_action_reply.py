from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_target_status import BulkActionTargetStatus

T = TypeVar("T", bound="BulkActionReply")


@_attrs_define
class BulkActionReply:
    """
    Attributes:
        reply (str): What the game answered, or why the command failed. Empty when it was delivered and the game said
            nothing.
        status (BulkActionTargetStatus):
        count (int): How many targets gave this reply.
        targets (list[str]): Up to 10 of them, as IDs.
    """

    reply: str
    status: BulkActionTargetStatus
    count: int
    targets: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reply = self.reply

        status = self.status.value

        count = self.count

        targets = self.targets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reply": reply,
                "status": status,
                "count": count,
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reply = d.pop("reply")

        status = BulkActionTargetStatus(d.pop("status"))

        count = d.pop("count")

        targets = cast(list[str], d.pop("targets"))

        bulk_action_reply = cls(
            reply=reply,
            status=status,
            count=count,
            targets=targets,
        )

        bulk_action_reply.additional_properties = d
        return bulk_action_reply

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

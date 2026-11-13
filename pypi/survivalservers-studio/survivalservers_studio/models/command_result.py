from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommandResult")


@_attrs_define
class CommandResult:
    """
    Attributes:
        delivered (bool): The game took the command (its port answered, or the line was typed).
        output (str | Unset): The RCON reply, the HTTP body, or the console lines written within `capture`; up to 4 KiB,
            the first part kept.
        http_status (int | Unset): HTTP calls only: the game's status code.
        truncated (bool | Unset): The output was longer than 4 KiB.
        error (str | Unset): Why it was not delivered.
    """

    delivered: bool
    output: str | Unset = UNSET
    http_status: int | Unset = UNSET
    truncated: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivered = self.delivered

        output = self.output

        http_status = self.http_status

        truncated = self.truncated

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delivered": delivered,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delivered = d.pop("delivered")

        output = d.pop("output", UNSET)

        http_status = d.pop("http_status", UNSET)

        truncated = d.pop("truncated", UNSET)

        error = d.pop("error", UNSET)

        command_result = cls(
            delivered=delivered,
            output=output,
            http_status=http_status,
            truncated=truncated,
            error=error,
        )

        command_result.additional_properties = d
        return command_result

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersistentServerConfigResult")


@_attrs_define
class PersistentServerConfigResult:
    """
    Attributes:
        id (str): The setting's ID.
        delivered (bool): The game took it.
        output (str | Unset): What the game answered.
        error (str | Unset): Why it was not delivered.
    """

    id: str
    delivered: bool
    output: str | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delivered = self.delivered

        output = self.output

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "delivered": delivered,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        delivered = d.pop("delivered")

        output = d.pop("output", UNSET)

        error = d.pop("error", UNSET)

        persistent_server_config_result = cls(
            id=id,
            delivered=delivered,
            output=output,
            error=error,
        )

        persistent_server_config_result.additional_properties = d
        return persistent_server_config_result

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

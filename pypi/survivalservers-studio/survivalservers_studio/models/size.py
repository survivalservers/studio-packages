from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Size")


@_attrs_define
class Size:
    """One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs. Memory 0.5 GB to
    4 GB per vCPU.

        Attributes:
            cpu (float): vCPUs (hardware threads).
            memory_gb (float): Memory in GB.
    """

    cpu: float
    memory_gb: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        memory_gb = self.memory_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu": cpu,
                "memory_gb": memory_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu = d.pop("cpu")

        memory_gb = d.pop("memory_gb")

        size = cls(
            cpu=cpu,
            memory_gb=memory_gb,
        )

        size.additional_properties = d
        return size

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

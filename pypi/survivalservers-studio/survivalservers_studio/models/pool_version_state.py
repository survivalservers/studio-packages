from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolVersionState")


@_attrs_define
class PoolVersionState:
    """
    Attributes:
        version (str): Version name, unique in its app, for example `2.3.1`.
        ready (int): Ready and waiting for a start.
        starting (int): Started and not ready yet.
    """

    version: str
    ready: int
    starting: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        ready = self.ready

        starting = self.starting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "ready": ready,
                "starting": starting,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version = d.pop("version")

        ready = d.pop("ready")

        starting = d.pop("starting")

        pool_version_state = cls(
            version=version,
            ready=ready,
            starting=starting,
        )

        pool_version_state.additional_properties = d
        return pool_version_state

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

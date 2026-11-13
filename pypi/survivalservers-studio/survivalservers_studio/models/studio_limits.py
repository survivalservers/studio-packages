from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StudioLimits")


@_attrs_define
class StudioLimits:
    """
    Attributes:
        running_cpus (int): How many vCPUs the studio may run at once: every live game server counts, ready ones waiting
            in pools included, and a persistent server from the moment it is asked to start.
        cpus_per_game_server (int):
        memory_gb_per_game_server (int):
        zip_build_gb (int):
        image_build_gb (int):
        versions_per_app (int):
        build_storage_gb (int):
    """

    running_cpus: int
    cpus_per_game_server: int
    memory_gb_per_game_server: int
    zip_build_gb: int
    image_build_gb: int
    versions_per_app: int
    build_storage_gb: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        running_cpus = self.running_cpus

        cpus_per_game_server = self.cpus_per_game_server

        memory_gb_per_game_server = self.memory_gb_per_game_server

        zip_build_gb = self.zip_build_gb

        image_build_gb = self.image_build_gb

        versions_per_app = self.versions_per_app

        build_storage_gb = self.build_storage_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "running_cpus": running_cpus,
                "cpus_per_game_server": cpus_per_game_server,
                "memory_gb_per_game_server": memory_gb_per_game_server,
                "zip_build_gb": zip_build_gb,
                "image_build_gb": image_build_gb,
                "versions_per_app": versions_per_app,
                "build_storage_gb": build_storage_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        running_cpus = d.pop("running_cpus")

        cpus_per_game_server = d.pop("cpus_per_game_server")

        memory_gb_per_game_server = d.pop("memory_gb_per_game_server")

        zip_build_gb = d.pop("zip_build_gb")

        image_build_gb = d.pop("image_build_gb")

        versions_per_app = d.pop("versions_per_app")

        build_storage_gb = d.pop("build_storage_gb")

        studio_limits = cls(
            running_cpus=running_cpus,
            cpus_per_game_server=cpus_per_game_server,
            memory_gb_per_game_server=memory_gb_per_game_server,
            zip_build_gb=zip_build_gb,
            image_build_gb=image_build_gb,
            versions_per_app=versions_per_app,
            build_storage_gb=build_storage_gb,
        )

        studio_limits.additional_properties = d
        return studio_limits

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

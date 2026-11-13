from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..models.tier import Tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch import Launch
    from ..models.restart_policy import RestartPolicy
    from ..models.size import Size
    from ..models.version_region import VersionRegion
    from ..models.version_usage import VersionUsage
    from ..models.version_warning import VersionWarning


T = TypeVar("T", bound="VersionDetail")


@_attrs_define
class VersionDetail:
    """
    Attributes:
        id (str): Version ID.
        app (str): App ID.
        name (str): Version name, unique in its app, for example `2.3.1`.
        build (str): Build ID.
        tier (Tier): Public hardware tier.
        os (Os):
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        launch (Launch):
        restart (RestartPolicy): What happens when the game server exits on its own.
        target_regions (list[str]): The requested region list, as sent (`["*"]` or region IDs).
        regions (list[VersionRegion]): Readiness per region; fills in as each region gets it.
        deprecated (bool):
        created_at (datetime.datetime): When it was made.
        usage (None | VersionUsage): The memory of its matches and persistent server runs that ended in the last 90
            days, each counted at its highest. `null` when none has.
        max_duration (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        warnings (list[VersionWarning] | Unset): Settings that work but carry a risk, each with what to do instead. Left
            out when there are none. New codes may be added.
    """

    id: str
    app: str
    name: str
    build: str
    tier: Tier
    os: Os
    size: Size
    launch: Launch
    restart: RestartPolicy
    target_regions: list[str]
    regions: list[VersionRegion]
    deprecated: bool
    created_at: datetime.datetime
    usage: None | VersionUsage
    max_duration: int | str | Unset = UNSET
    warnings: list[VersionWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.version_usage import VersionUsage

        id = self.id

        app = self.app

        name = self.name

        build = self.build

        tier = self.tier.value

        os = self.os.value

        size = self.size.to_dict()

        launch = self.launch.to_dict()

        restart = self.restart.to_dict()

        target_regions = self.target_regions

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        deprecated = self.deprecated

        created_at = self.created_at.isoformat()

        usage: dict[str, Any] | None
        if isinstance(self.usage, VersionUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        max_duration: int | str | Unset
        if isinstance(self.max_duration, Unset):
            max_duration = UNSET
        else:
            max_duration = self.max_duration

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app": app,
                "name": name,
                "build": build,
                "tier": tier,
                "os": os,
                "size": size,
                "launch": launch,
                "restart": restart,
                "target_regions": target_regions,
                "regions": regions,
                "deprecated": deprecated,
                "created_at": created_at,
                "usage": usage,
            }
        )
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.launch import Launch
        from ..models.restart_policy import RestartPolicy
        from ..models.size import Size
        from ..models.version_region import VersionRegion
        from ..models.version_usage import VersionUsage
        from ..models.version_warning import VersionWarning

        d = dict(src_dict)
        id = d.pop("id")

        app = d.pop("app")

        name = d.pop("name")

        build = d.pop("build")

        tier = Tier(d.pop("tier"))

        os = Os(d.pop("os"))

        size = Size.from_dict(d.pop("size"))

        launch = Launch.from_dict(d.pop("launch"))

        restart = RestartPolicy.from_dict(d.pop("restart"))

        target_regions = cast(list[str], d.pop("target_regions"))

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = VersionRegion.from_dict(regions_item_data)

            regions.append(regions_item)

        deprecated = d.pop("deprecated")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_usage(data: object) -> None | VersionUsage:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = VersionUsage.from_dict(data)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VersionUsage, data)

        usage = _parse_usage(d.pop("usage"))

        def _parse_max_duration(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        max_duration = _parse_max_duration(d.pop("max_duration", UNSET))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[VersionWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = VersionWarning.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        version_detail = cls(
            id=id,
            app=app,
            name=name,
            build=build,
            tier=tier,
            os=os,
            size=size,
            launch=launch,
            restart=restart,
            target_regions=target_regions,
            regions=regions,
            deprecated=deprecated,
            created_at=created_at,
            usage=usage,
            max_duration=max_duration,
            warnings=warnings,
        )

        version_detail.additional_properties = d
        return version_detail

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

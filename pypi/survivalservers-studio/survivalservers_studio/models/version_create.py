from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tier import Tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_profile import GameProfile
    from ..models.launch import Launch
    from ..models.restart_policy import RestartPolicy
    from ..models.size import Size


T = TypeVar("T", bound="VersionCreate")


@_attrs_define
class VersionCreate:
    """
    Attributes:
        name (str): Version name, unique in its app, for example `2.3.1`.
        build (str): Build ID.
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        launch (Launch):
        tier (Tier | Unset): Public hardware tier.
        restart (RestartPolicy | Unset): What happens when the game server exits on its own.
        profile (GameProfile | Unset): One description of a server, read by the panel, the API, the CLI and AI tools:
            how to reach the game and the commands it takes. Plain JSON, and every part is optional. Secrets stay in the
            version's env values; a profile only names them.
        max_duration (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        regions (list[str] | Unset): Where to stage it ahead of time; `["*"]` for every region that offers the app's
            tier and OS.
    """

    name: str
    build: str
    size: Size
    launch: Launch
    tier: Tier | Unset = UNSET
    restart: RestartPolicy | Unset = UNSET
    profile: GameProfile | Unset = UNSET
    max_duration: int | str | Unset = UNSET
    regions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        build = self.build

        size = self.size.to_dict()

        launch = self.launch.to_dict()

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        max_duration: int | str | Unset
        if isinstance(self.max_duration, Unset):
            max_duration = UNSET
        else:
            max_duration = self.max_duration

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "build": build,
                "size": size,
                "launch": launch,
            }
        )
        if tier is not UNSET:
            field_dict["tier"] = tier
        if restart is not UNSET:
            field_dict["restart"] = restart
        if profile is not UNSET:
            field_dict["profile"] = profile
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_profile import GameProfile
        from ..models.launch import Launch
        from ..models.restart_policy import RestartPolicy
        from ..models.size import Size

        d = dict(src_dict)
        name = d.pop("name")

        build = d.pop("build")

        size = Size.from_dict(d.pop("size"))

        launch = Launch.from_dict(d.pop("launch"))

        _tier = d.pop("tier", UNSET)
        tier: Tier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = Tier(_tier)

        _restart = d.pop("restart", UNSET)
        restart: RestartPolicy | Unset
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = RestartPolicy.from_dict(_restart)

        _profile = d.pop("profile", UNSET)
        profile: GameProfile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = GameProfile.from_dict(_profile)

        def _parse_max_duration(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        max_duration = _parse_max_duration(d.pop("max_duration", UNSET))

        regions = cast(list[str], d.pop("regions", UNSET))

        version_create = cls(
            name=name,
            build=build,
            size=size,
            launch=launch,
            tier=tier,
            restart=restart,
            profile=profile,
            max_duration=max_duration,
            regions=regions,
        )

        version_create.additional_properties = d
        return version_create

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

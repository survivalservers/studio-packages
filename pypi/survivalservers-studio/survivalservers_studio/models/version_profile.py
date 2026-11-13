from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.game_profile import GameProfile


T = TypeVar("T", bound="VersionProfile")


@_attrs_define
class VersionProfile:
    """
    Attributes:
        profile (GameProfile): One description of a server, read by the panel, the API, the CLI and AI tools: how to
            reach the game and the commands it takes. Plain JSON, and every part is optional. Secrets stay in the version's
            env values; a profile only names them.
        revision (int): One more with each save; 0 for a version that never had one.
    """

    profile: GameProfile
    revision: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile.to_dict()

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile": profile,
                "revision": revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_profile import GameProfile

        d = dict(src_dict)
        profile = GameProfile.from_dict(d.pop("profile"))

        revision = d.pop("revision")

        version_profile = cls(
            profile=profile,
            revision=revision,
        )

        version_profile.additional_properties = d
        return version_profile

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

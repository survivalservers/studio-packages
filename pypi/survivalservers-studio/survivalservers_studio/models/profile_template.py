from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.game_profile import GameProfile
    from ..models.profile_template_port import ProfileTemplatePort


T = TypeVar("T", bound="ProfileTemplate")


@_attrs_define
class ProfileTemplate:
    """
    Attributes:
        id (str): The template's ID.
        name (str): The game.
        summary (str): What the profile covers.
        ports (list[ProfileTemplatePort]): Ports the version must have.
        env (list[str]): Env values the version must set.
        setup (list[str]): What else the game needs, one step each.
        sources (list[str]): Where each fact comes from.
        proven (list[str]): What has run against the real game.
        not_proven (list[str]): What has not run against the real game, or rests on a source other than the game's own.
        profile (GameProfile): One description of a server, read by the panel, the API, the CLI and AI tools: how to
            reach the game and the commands it takes. Plain JSON, and every part is optional. Secrets stay in the version's
            env values; a profile only names them.
    """

    id: str
    name: str
    summary: str
    ports: list[ProfileTemplatePort]
    env: list[str]
    setup: list[str]
    sources: list[str]
    proven: list[str]
    not_proven: list[str]
    profile: GameProfile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        summary = self.summary

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        env = self.env

        setup = self.setup

        sources = self.sources

        proven = self.proven

        not_proven = self.not_proven

        profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "summary": summary,
                "ports": ports,
                "env": env,
                "setup": setup,
                "sources": sources,
                "proven": proven,
                "not_proven": not_proven,
                "profile": profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_profile import GameProfile
        from ..models.profile_template_port import ProfileTemplatePort

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        summary = d.pop("summary")

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = ProfileTemplatePort.from_dict(ports_item_data)

            ports.append(ports_item)

        env = cast(list[str], d.pop("env"))

        setup = cast(list[str], d.pop("setup"))

        sources = cast(list[str], d.pop("sources"))

        proven = cast(list[str], d.pop("proven"))

        not_proven = cast(list[str], d.pop("not_proven"))

        profile = GameProfile.from_dict(d.pop("profile"))

        profile_template = cls(
            id=id,
            name=name,
            summary=summary,
            ports=ports,
            env=env,
            setup=setup,
            sources=sources,
            proven=proven,
            not_proven=not_proven,
            profile=profile,
        )

        profile_template.additional_properties = d
        return profile_template

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileSettingPlace")


@_attrs_define
class ProfileSettingPlace:
    """Where a setting lives: `env`, `arg`, or `file` with `key`.

    Attributes:
        env (str | Unset): An environment value.
        arg (str | Unset): A launch argument, with `{{value}}`. `-name {{value}}` is two arguments.
        file (str | Unset): The `id` of one of the config files.
        section (str | Unset): ini and toml: the section.
        key (str | Unset): The key. json: a path with dots.
        field (str | Unset): ini: a field inside the key's one-line `(A=1,B=2)` value, as Palworld keeps its settings.
    """

    env: str | Unset = UNSET
    arg: str | Unset = UNSET
    file: str | Unset = UNSET
    section: str | Unset = UNSET
    key: str | Unset = UNSET
    field: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        env = self.env

        arg = self.arg

        file = self.file

        section = self.section

        key = self.key

        field = self.field

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if env is not UNSET:
            field_dict["env"] = env
        if arg is not UNSET:
            field_dict["arg"] = arg
        if file is not UNSET:
            field_dict["file"] = file
        if section is not UNSET:
            field_dict["section"] = section
        if key is not UNSET:
            field_dict["key"] = key
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        env = d.pop("env", UNSET)

        arg = d.pop("arg", UNSET)

        file = d.pop("file", UNSET)

        section = d.pop("section", UNSET)

        key = d.pop("key", UNSET)

        field = d.pop("field", UNSET)

        profile_setting_place = cls(
            env=env,
            arg=arg,
            file=file,
            section=section,
            key=key,
            field=field,
        )

        return profile_setting_place

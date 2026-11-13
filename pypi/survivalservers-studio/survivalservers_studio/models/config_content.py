from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_file import ConfigFile
    from ..models.env import Env
    from ..models.setting_values import SettingValues


T = TypeVar("T", bound="ConfigContent")


@_attrs_define
class ConfigContent:
    """The settings of one version. The set's `env` replaces a persistent server's own value of the same name (a change
    across all your servers reaches every persistent server); the set's `args` come after the version's and the
    persistent server's own; `files` are written into the persistent server's folder before every run, replacing what is
    there. Up to 32 files and 512 KiB in all. `values` set the settings in the game profile by ID, changing only those
    keys in the game's own files, and win over a server's own values.

        Attributes:
            env (Env | Unset): Environment variables. Names starting with `GS_` are reserved (`422`).
            args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
                `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
                or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
                its arguments to the running game as allocation data, as written.
            files (list[ConfigFile] | Unset):
            values (SettingValues | Unset): Values by setting ID, each its setting's type.
            note (str | Unset): What changed and why.
    """

    env: Env | Unset = UNSET
    args: list[str] | Unset = UNSET
    files: list[ConfigFile] | Unset = UNSET
    values: SettingValues | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env is not UNSET:
            field_dict["env"] = env
        if args is not UNSET:
            field_dict["args"] = args
        if files is not UNSET:
            field_dict["files"] = files
        if values is not UNSET:
            field_dict["values"] = values
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_file import ConfigFile
        from ..models.env import Env
        from ..models.setting_values import SettingValues

        d = dict(src_dict)
        _env = d.pop("env", UNSET)
        env: Env | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = Env.from_dict(_env)

        args = cast(list[str], d.pop("args", UNSET))

        _files = d.pop("files", UNSET)
        files: list[ConfigFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ConfigFile.from_dict(files_item_data)

                files.append(files_item)

        _values = d.pop("values", UNSET)
        values: SettingValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = SettingValues.from_dict(_values)

        note = d.pop("note", UNSET)

        config_content = cls(
            env=env,
            args=args,
            files=files,
            values=values,
            note=note,
        )

        config_content.additional_properties = d
        return config_content

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_file import ConfigFile
    from ..models.env import Env
    from ..models.setting_values import SettingValues


T = TypeVar("T", bound="ConfigSetVersion")


@_attrs_define
class ConfigSetVersion:
    """
    Attributes:
        config_set (str): Config set ID.
        version (int):
        env (Env): Environment variables. Names starting with `GS_` are reserved (`422`).
        args (list[str]): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        files (list[ConfigFile]):
        created_by (str): The key or member that saved it.
        created_at (datetime.datetime): When it was saved.
        persistent_servers (int): Persistent servers on this version now.
        values (SettingValues | Unset): Values by setting ID, each its setting's type.
        note (None | str | Unset):
    """

    config_set: str
    version: int
    env: Env
    args: list[str]
    files: list[ConfigFile]
    created_by: str
    created_at: datetime.datetime
    persistent_servers: int
    values: SettingValues | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_set = self.config_set

        version = self.version

        env = self.env.to_dict()

        args = self.args

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        persistent_servers = self.persistent_servers

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_set": config_set,
                "version": version,
                "env": env,
                "args": args,
                "files": files,
                "created_by": created_by,
                "created_at": created_at,
                "persistent_servers": persistent_servers,
            }
        )
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
        config_set = d.pop("config_set")

        version = d.pop("version")

        env = Env.from_dict(d.pop("env"))

        args = cast(list[str], d.pop("args"))

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = ConfigFile.from_dict(files_item_data)

            files.append(files_item)

        created_by = d.pop("created_by")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        persistent_servers = d.pop("persistent_servers")

        _values = d.pop("values", UNSET)
        values: SettingValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = SettingValues.from_dict(_values)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        config_set_version = cls(
            config_set=config_set,
            version=version,
            env=env,
            args=args,
            files=files,
            created_by=created_by,
            created_at=created_at,
            persistent_servers=persistent_servers,
            values=values,
            note=note,
        )

        config_set_version.additional_properties = d
        return config_set_version

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_env_change import ConfigEnvChange
    from ..models.config_file_change import ConfigFileChange


T = TypeVar("T", bound="ConfigDiff")


@_attrs_define
class ConfigDiff:
    """
    Attributes:
        env (list[ConfigEnvChange]):
        args_before (list[str]): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        args_after (list[str]): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        files (list[ConfigFileChange]):
        from_ (int | None | Unset): The older version; `null` for no config set.
        to (int | None | Unset): The newer version; `null` when the set is taken off.
        values (list[ConfigEnvChange] | Unset): Settings by ID, with their values as text.
    """

    env: list[ConfigEnvChange]
    args_before: list[str]
    args_after: list[str]
    files: list[ConfigFileChange]
    from_: int | None | Unset = UNSET
    to: int | None | Unset = UNSET
    values: list[ConfigEnvChange] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env = []
        for env_item_data in self.env:
            env_item = env_item_data.to_dict()
            env.append(env_item)

        args_before = self.args_before

        args_after = self.args_after

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        from_: int | None | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: int | None | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "env": env,
                "args_before": args_before,
                "args_after": args_after,
                "files": files,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_env_change import ConfigEnvChange
        from ..models.config_file_change import ConfigFileChange

        d = dict(src_dict)
        env = []
        _env = d.pop("env")
        for env_item_data in _env:
            env_item = ConfigEnvChange.from_dict(env_item_data)

            env.append(env_item)

        args_before = cast(list[str], d.pop("args_before"))

        args_after = cast(list[str], d.pop("args_after"))

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = ConfigFileChange.from_dict(files_item_data)

            files.append(files_item)

        def _parse_from_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        _values = d.pop("values", UNSET)
        values: list[ConfigEnvChange] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ConfigEnvChange.from_dict(values_item_data)

                values.append(values_item)

        config_diff = cls(
            env=env,
            args_before=args_before,
            args_after=args_after,
            files=files,
            from_=from_,
            to=to,
            values=values,
        )

        config_diff.additional_properties = d
        return config_diff

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

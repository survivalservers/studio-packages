from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_config_file import ProfileConfigFile
    from ..models.profile_setting import ProfileSetting


T = TypeVar("T", bound="ProfileConfig")


@_attrs_define
class ProfileConfig:
    """The game's settings as data. The panel draws its config form from this, and a change writes only the keys it names.

    Attributes:
        files (list[ProfileConfigFile] | Unset):
        settings (list[ProfileSetting] | Unset):
    """

    files: list[ProfileConfigFile] | Unset = UNSET
    settings: list[ProfileSetting] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = []
            for settings_item_data in self.settings:
                settings_item = settings_item_data.to_dict()
                settings.append(settings_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.profile_config_file import ProfileConfigFile
        from ..models.profile_setting import ProfileSetting

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[ProfileConfigFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ProfileConfigFile.from_dict(files_item_data)

                files.append(files_item)

        _settings = d.pop("settings", UNSET)
        settings: list[ProfileSetting] | Unset = UNSET
        if _settings is not UNSET:
            settings = []
            for settings_item_data in _settings:
                settings_item = ProfileSetting.from_dict(settings_item_data)

                settings.append(settings_item)

        profile_config = cls(
            files=files,
            settings=settings,
        )

        return profile_config

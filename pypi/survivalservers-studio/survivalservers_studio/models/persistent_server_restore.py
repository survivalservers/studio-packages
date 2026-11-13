from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restore_version import RestoreVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_warning import BulkActionWarning
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="PersistentServerRestore")


@_attrs_define
class PersistentServerRestore:
    """Give `backup` or `at`, or the `plan` of a preview.

    Attributes:
        backup (str | Unset): Backup ID.
        at (datetime.datetime | Unset): Go back to its newest backup from before this moment.
        version (RestoreVersion | Unset): `keep` restores the saves and keeps the version it runs now. `then` also puts
            back the version it ran when the backup was made; a server whose version from then was deleted is skipped with
            `version_gone`.
        start (bool | Unset): Start it after, even if it is stopped now. `false` leaves it stopped. Default: running
            again if it was running.
        warnings (list[BulkActionWarning] | Unset): In-game warnings first, as for maintenance; the restore starts after
            the earliest one.
        warn_command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command
            for the game server itself.
        note (str | Unset):
        dry_run (bool | Unset):  Default: False.
        plan (str | Unset): A preview's ID.
    """

    backup: str | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    version: RestoreVersion | Unset = UNSET
    start: bool | Unset = UNSET
    warnings: list[BulkActionWarning] | Unset = UNSET
    warn_command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = False
    plan: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        backup = self.backup

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        start = self.start

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        warn_command: dict[str, Any] | Unset
        if isinstance(self.warn_command, Unset):
            warn_command = UNSET
        elif (
            isinstance(self.warn_command, GameCommandConsole)
            or isinstance(self.warn_command, GameCommandRcon)
            or isinstance(self.warn_command, GameCommandHttp)
        ):
            warn_command = self.warn_command.to_dict()
        else:
            warn_command = self.warn_command.to_dict()

        note = self.note

        dry_run = self.dry_run

        plan = self.plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup is not UNSET:
            field_dict["backup"] = backup
        if at is not UNSET:
            field_dict["at"] = at
        if version is not UNSET:
            field_dict["version"] = version
        if start is not UNSET:
            field_dict["start"] = start
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if warn_command is not UNSET:
            field_dict["warn_command"] = warn_command
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_warning import BulkActionWarning
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        backup = d.pop("backup", UNSET)

        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        _version = d.pop("version", UNSET)
        version: RestoreVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = RestoreVersion(_version)

        start = d.pop("start", UNSET)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[BulkActionWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = BulkActionWarning.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        def _parse_warn_command(
            data: object,
        ) -> (
            GameCommandConsole
            | GameCommandHttp
            | GameCommandIsleRcon
            | GameCommandRcon
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_0 = GameCommandConsole.from_dict(
                    data
                )

                return componentsschemas_game_command_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_1 = GameCommandRcon.from_dict(data)

                return componentsschemas_game_command_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_2 = GameCommandHttp.from_dict(data)

                return componentsschemas_game_command_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_game_command_type_3 = GameCommandIsleRcon.from_dict(data)

            return componentsschemas_game_command_type_3

        warn_command = _parse_warn_command(d.pop("warn_command", UNSET))

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        plan = d.pop("plan", UNSET)

        persistent_server_restore = cls(
            backup=backup,
            at=at,
            version=version,
            start=start,
            warnings=warnings,
            warn_command=warn_command,
            note=note,
            dry_run=dry_run,
            plan=plan,
        )

        persistent_server_restore.additional_properties = d
        return persistent_server_restore

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

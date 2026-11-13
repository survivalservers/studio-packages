from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_maintenance_action import BulkActionMaintenanceAction
    from ..models.bulk_action_warning import BulkActionWarning
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="BulkActionMaintenance")


@_attrs_define
class BulkActionMaintenance:
    """Maintenance only.

    Attributes:
        at (datetime.datetime | Unset): When the action starts.
        ends_at (datetime.datetime | None | Unset): Persistent servers not started by then are skipped.
        warnings (list[BulkActionWarning] | Unset):
        warn_command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command
            for the game server itself.
        action (BulkActionMaintenanceAction | Unset):
        warnings_sent (int | Unset): Warnings sent so far.
    """

    at: datetime.datetime | Unset = UNSET
    ends_at: datetime.datetime | None | Unset = UNSET
    warnings: list[BulkActionWarning] | Unset = UNSET
    warn_command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    action: BulkActionMaintenanceAction | Unset = UNSET
    warnings_sent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        ends_at: None | str | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        elif isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

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

        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        warnings_sent = self.warnings_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if warn_command is not UNSET:
            field_dict["warn_command"] = warn_command
        if action is not UNSET:
            field_dict["action"] = action
        if warnings_sent is not UNSET:
            field_dict["warnings_sent"] = warnings_sent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_maintenance_action import BulkActionMaintenanceAction
        from ..models.bulk_action_warning import BulkActionWarning
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        def _parse_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

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

        _action = d.pop("action", UNSET)
        action: BulkActionMaintenanceAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = BulkActionMaintenanceAction.from_dict(_action)

        warnings_sent = d.pop("warnings_sent", UNSET)

        bulk_action_maintenance = cls(
            at=at,
            ends_at=ends_at,
            warnings=warnings,
            warn_command=warn_command,
            action=action,
            warnings_sent=warnings_sent,
        )

        bulk_action_maintenance.additional_properties = d
        return bulk_action_maintenance

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

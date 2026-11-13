from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_maintenance_action import BulkActionMaintenanceAction
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_selector import BulkActionSelector
    from ..models.bulk_action_warning import BulkActionWarning
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="BulkActionMaintenanceCreate")


@_attrs_define
class BulkActionMaintenanceCreate:
    """
    Attributes:
        selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
            filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        at (datetime.datetime): When the action starts, after the last warning.
        action (BulkActionMaintenanceAction):
        ends_at (datetime.datetime | Unset): Persistent servers not started by then are skipped.
        warnings (list[BulkActionWarning] | Unset):
        warn_command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command
            for the game server itself.
        shutdown_time (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        rollout (BulkActionRollout | Unset): How targets are taken in batches. Give `batch_size` or `batch_percent`, not
            both.
        note (str | Unset):
        dry_run (bool | Unset):  Default: False.
    """

    selector: BulkActionSelector
    at: datetime.datetime
    action: BulkActionMaintenanceAction
    ends_at: datetime.datetime | Unset = UNSET
    warnings: list[BulkActionWarning] | Unset = UNSET
    warn_command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    shutdown_time: int | str | Unset = UNSET
    rollout: BulkActionRollout | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        selector = self.selector.to_dict()

        at = self.at.isoformat()

        action = self.action.to_dict()

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

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

        shutdown_time: int | str | Unset
        if isinstance(self.shutdown_time, Unset):
            shutdown_time = UNSET
        else:
            shutdown_time = self.shutdown_time

        rollout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.to_dict()

        note = self.note

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
                "at": at,
                "action": action,
            }
        )
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if warn_command is not UNSET:
            field_dict["warn_command"] = warn_command
        if shutdown_time is not UNSET:
            field_dict["shutdown_time"] = shutdown_time
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_maintenance_action import BulkActionMaintenanceAction
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_selector import BulkActionSelector
        from ..models.bulk_action_warning import BulkActionWarning
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        selector = BulkActionSelector.from_dict(d.pop("selector"))

        at = datetime.datetime.fromisoformat(d.pop("at"))

        action = BulkActionMaintenanceAction.from_dict(d.pop("action"))

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = datetime.datetime.fromisoformat(_ends_at)

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

        def _parse_shutdown_time(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        shutdown_time = _parse_shutdown_time(d.pop("shutdown_time", UNSET))

        _rollout = d.pop("rollout", UNSET)
        rollout: BulkActionRollout | Unset
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = BulkActionRollout.from_dict(_rollout)

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        bulk_action_maintenance_create = cls(
            selector=selector,
            at=at,
            action=action,
            ends_at=ends_at,
            warnings=warnings,
            warn_command=warn_command,
            shutdown_time=shutdown_time,
            rollout=rollout,
            note=note,
            dry_run=dry_run,
        )

        bulk_action_maintenance_create.additional_properties = d
        return bulk_action_maintenance_create

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

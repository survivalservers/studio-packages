from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restore_version import RestoreVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_selector import BulkActionSelector
    from ..models.bulk_action_warning import BulkActionWarning
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="BulkActionRollbackCreate")


@_attrs_define
class BulkActionRollbackCreate:
    """Send `selector` and `at` (or `before_update`) for a preview; send the preview's `id` as `plan` to run it.

    Attributes:
        selector (BulkActionSelector | Unset): Which persistent servers, game servers or pools a bulk action acts on.
            Every filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        at (datetime.datetime | Unset): Each server goes back to its newest backup from before this moment.
        before_update (str | Unset): Bulk action ID.
        version (RestoreVersion | Unset): `keep` restores the saves and keeps the version it runs now. `then` also puts
            back the version it ran when the backup was made; a server whose version from then was deleted is skipped with
            `version_gone`.
        warnings (list[BulkActionWarning] | Unset): In-game warnings first, as for maintenance; the rollback starts
            after the earliest one.
        warn_command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command
            for the game server itself.
        starts_at (datetime.datetime | Unset): Start later than now.
        rollout (BulkActionRollout | Unset): How targets are taken in batches. Give `batch_size` or `batch_percent`, not
            both.
        shutdown_time (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        note (str | Unset):
        dry_run (bool | Unset): A rollback always runs from a preview
        plan (str | Unset): A preview's ID.
    """

    selector: BulkActionSelector | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    before_update: str | Unset = UNSET
    version: RestoreVersion | Unset = UNSET
    warnings: list[BulkActionWarning] | Unset = UNSET
    warn_command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    starts_at: datetime.datetime | Unset = UNSET
    rollout: BulkActionRollout | Unset = UNSET
    shutdown_time: int | str | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = UNSET
    plan: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        before_update = self.before_update

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

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

        starts_at: str | Unset = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        rollout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.to_dict()

        shutdown_time: int | str | Unset
        if isinstance(self.shutdown_time, Unset):
            shutdown_time = UNSET
        else:
            shutdown_time = self.shutdown_time

        note = self.note

        dry_run = self.dry_run

        plan = self.plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selector is not UNSET:
            field_dict["selector"] = selector
        if at is not UNSET:
            field_dict["at"] = at
        if before_update is not UNSET:
            field_dict["before_update"] = before_update
        if version is not UNSET:
            field_dict["version"] = version
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if warn_command is not UNSET:
            field_dict["warn_command"] = warn_command
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if shutdown_time is not UNSET:
            field_dict["shutdown_time"] = shutdown_time
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_selector import BulkActionSelector
        from ..models.bulk_action_warning import BulkActionWarning
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        _selector = d.pop("selector", UNSET)
        selector: BulkActionSelector | Unset
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = BulkActionSelector.from_dict(_selector)

        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        before_update = d.pop("before_update", UNSET)

        _version = d.pop("version", UNSET)
        version: RestoreVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = RestoreVersion(_version)

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

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: datetime.datetime | Unset
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = datetime.datetime.fromisoformat(_starts_at)

        _rollout = d.pop("rollout", UNSET)
        rollout: BulkActionRollout | Unset
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = BulkActionRollout.from_dict(_rollout)

        def _parse_shutdown_time(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        shutdown_time = _parse_shutdown_time(d.pop("shutdown_time", UNSET))

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        plan = d.pop("plan", UNSET)

        bulk_action_rollback_create = cls(
            selector=selector,
            at=at,
            before_update=before_update,
            version=version,
            warnings=warnings,
            warn_command=warn_command,
            starts_at=starts_at,
            rollout=rollout,
            shutdown_time=shutdown_time,
            note=note,
            dry_run=dry_run,
            plan=plan,
        )

        bulk_action_rollback_create.additional_properties = d
        return bulk_action_rollback_create

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

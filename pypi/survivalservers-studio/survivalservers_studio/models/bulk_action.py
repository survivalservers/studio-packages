from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_apply import BulkActionApply
from ..models.bulk_action_status import BulkActionStatus
from ..models.bulk_action_type import BulkActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_batches import BulkActionBatches
    from ..models.bulk_action_counts import BulkActionCounts
    from ..models.bulk_action_maintenance import BulkActionMaintenance
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_saved_command import BulkActionSavedCommand
    from ..models.bulk_action_selector import BulkActionSelector
    from ..models.config_set_ref_type_0 import ConfigSetRefType0
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="BulkAction")


@_attrs_define
class BulkAction:
    """
    Attributes:
        id (str): Bulk action ID.
        type_ (BulkActionType):
        status (BulkActionStatus): `warning`: maintenance is sending its warnings; `stopped`: it stopped by itself
            because more targets failed than `max_failures` allows (resume or cancel it).
        selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
            filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        rollout (BulkActionRollout): How targets are taken in batches. Give `batch_size` or `batch_percent`, not both.
        counts (BulkActionCounts):
        batches (BulkActionBatches):
        created_by (str): The key or member that made it (as the audit log names them).
        created_at (datetime.datetime): When it was made.
        command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command for
            the game server itself.
        saved_command (BulkActionSavedCommand | Unset): The saved command a bulk action runs. `command` beside it is
            what the first target was sent.
        capture (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        version (None | str | Unset): Rollouts: the version targets move to.
        branch (None | str | Unset): Rollouts: the branch targets follow.
        apply (BulkActionApply | Unset):
        config_set (ConfigSetRefType0 | None | Unset):
        remove (bool | Unset): Config: the set is being taken off.
        shutdown_time (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        maintenance (BulkActionMaintenance | Unset): Maintenance only.
        stop_reason (None | str | Unset): Why it stopped, in a sentence a person reads.
        undo_of (None | str | Unset): The bulk action this one undoes.
        retry_of (None | str | Unset): The bulk action whose failed targets this one retries.
        undoable (bool | Unset): `POST .../undo` can put its targets back.
        note (None | str | Unset):
        scheduled_at (datetime.datetime | None | Unset): When it starts (scheduled ones).
        started_at (datetime.datetime | None | Unset): When its first batch started.
        finished_at (datetime.datetime | None | Unset): When it ended.
        updated_at (datetime.datetime | Unset): When it last changed.
    """

    id: str
    type_: BulkActionType
    status: BulkActionStatus
    selector: BulkActionSelector
    rollout: BulkActionRollout
    counts: BulkActionCounts
    batches: BulkActionBatches
    created_by: str
    created_at: datetime.datetime
    command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    saved_command: BulkActionSavedCommand | Unset = UNSET
    capture: int | str | Unset = UNSET
    version: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    apply: BulkActionApply | Unset = UNSET
    config_set: ConfigSetRefType0 | None | Unset = UNSET
    remove: bool | Unset = UNSET
    shutdown_time: int | str | Unset = UNSET
    maintenance: BulkActionMaintenance | Unset = UNSET
    stop_reason: None | str | Unset = UNSET
    undo_of: None | str | Unset = UNSET
    retry_of: None | str | Unset = UNSET
    undoable: bool | Unset = UNSET
    note: None | str | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_set_ref_type_0 import ConfigSetRefType0
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        id = self.id

        type_ = self.type_.value

        status = self.status.value

        selector = self.selector.to_dict()

        rollout = self.rollout.to_dict()

        counts = self.counts.to_dict()

        batches = self.batches.to_dict()

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        command: dict[str, Any] | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        elif (
            isinstance(self.command, GameCommandConsole)
            or isinstance(self.command, GameCommandRcon)
            or isinstance(self.command, GameCommandHttp)
        ):
            command = self.command.to_dict()
        else:
            command = self.command.to_dict()

        saved_command: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saved_command, Unset):
            saved_command = self.saved_command.to_dict()

        capture: int | str | Unset
        if isinstance(self.capture, Unset):
            capture = UNSET
        else:
            capture = self.capture

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        apply: str | Unset = UNSET
        if not isinstance(self.apply, Unset):
            apply = self.apply.value

        config_set: dict[str, Any] | None | Unset
        if isinstance(self.config_set, Unset):
            config_set = UNSET
        elif isinstance(self.config_set, ConfigSetRefType0):
            config_set = self.config_set.to_dict()
        else:
            config_set = self.config_set

        remove = self.remove

        shutdown_time: int | str | Unset
        if isinstance(self.shutdown_time, Unset):
            shutdown_time = UNSET
        else:
            shutdown_time = self.shutdown_time

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        stop_reason: None | str | Unset
        if isinstance(self.stop_reason, Unset):
            stop_reason = UNSET
        else:
            stop_reason = self.stop_reason

        undo_of: None | str | Unset
        if isinstance(self.undo_of, Unset):
            undo_of = UNSET
        else:
            undo_of = self.undo_of

        retry_of: None | str | Unset
        if isinstance(self.retry_of, Unset):
            retry_of = UNSET
        else:
            retry_of = self.retry_of

        undoable = self.undoable

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "selector": selector,
                "rollout": rollout,
                "counts": counts,
                "batches": batches,
                "created_by": created_by,
                "created_at": created_at,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if saved_command is not UNSET:
            field_dict["saved_command"] = saved_command
        if capture is not UNSET:
            field_dict["capture"] = capture
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if apply is not UNSET:
            field_dict["apply"] = apply
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if remove is not UNSET:
            field_dict["remove"] = remove
        if shutdown_time is not UNSET:
            field_dict["shutdown_time"] = shutdown_time
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if stop_reason is not UNSET:
            field_dict["stop_reason"] = stop_reason
        if undo_of is not UNSET:
            field_dict["undo_of"] = undo_of
        if retry_of is not UNSET:
            field_dict["retry_of"] = retry_of
        if undoable is not UNSET:
            field_dict["undoable"] = undoable
        if note is not UNSET:
            field_dict["note"] = note
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_batches import BulkActionBatches
        from ..models.bulk_action_counts import BulkActionCounts
        from ..models.bulk_action_maintenance import BulkActionMaintenance
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_saved_command import BulkActionSavedCommand
        from ..models.bulk_action_selector import BulkActionSelector
        from ..models.config_set_ref_type_0 import ConfigSetRefType0
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        id = d.pop("id")

        type_ = BulkActionType(d.pop("type"))

        status = BulkActionStatus(d.pop("status"))

        selector = BulkActionSelector.from_dict(d.pop("selector"))

        rollout = BulkActionRollout.from_dict(d.pop("rollout"))

        counts = BulkActionCounts.from_dict(d.pop("counts"))

        batches = BulkActionBatches.from_dict(d.pop("batches"))

        created_by = d.pop("created_by")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_command(
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

        command = _parse_command(d.pop("command", UNSET))

        _saved_command = d.pop("saved_command", UNSET)
        saved_command: BulkActionSavedCommand | Unset
        if isinstance(_saved_command, Unset):
            saved_command = UNSET
        else:
            saved_command = BulkActionSavedCommand.from_dict(_saved_command)

        def _parse_capture(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        capture = _parse_capture(d.pop("capture", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        _apply = d.pop("apply", UNSET)
        apply: BulkActionApply | Unset
        if isinstance(_apply, Unset):
            apply = UNSET
        else:
            apply = BulkActionApply(_apply)

        def _parse_config_set(data: object) -> ConfigSetRefType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_config_set_ref_type_0 = ConfigSetRefType0.from_dict(
                    data
                )

                return componentsschemas_config_set_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigSetRefType0 | None | Unset, data)

        config_set = _parse_config_set(d.pop("config_set", UNSET))

        remove = d.pop("remove", UNSET)

        def _parse_shutdown_time(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        shutdown_time = _parse_shutdown_time(d.pop("shutdown_time", UNSET))

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: BulkActionMaintenance | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = BulkActionMaintenance.from_dict(_maintenance)

        def _parse_stop_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stop_reason = _parse_stop_reason(d.pop("stop_reason", UNSET))

        def _parse_undo_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        undo_of = _parse_undo_of(d.pop("undo_of", UNSET))

        def _parse_retry_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retry_of = _parse_retry_of(d.pop("retry_of", UNSET))

        undoable = d.pop("undoable", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        bulk_action = cls(
            id=id,
            type_=type_,
            status=status,
            selector=selector,
            rollout=rollout,
            counts=counts,
            batches=batches,
            created_by=created_by,
            created_at=created_at,
            command=command,
            saved_command=saved_command,
            capture=capture,
            version=version,
            branch=branch,
            apply=apply,
            config_set=config_set,
            remove=remove,
            shutdown_time=shutdown_time,
            maintenance=maintenance,
            stop_reason=stop_reason,
            undo_of=undo_of,
            retry_of=retry_of,
            undoable=undoable,
            note=note,
            scheduled_at=scheduled_at,
            started_at=started_at,
            finished_at=finished_at,
            updated_at=updated_at,
        )

        bulk_action.additional_properties = d
        return bulk_action

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

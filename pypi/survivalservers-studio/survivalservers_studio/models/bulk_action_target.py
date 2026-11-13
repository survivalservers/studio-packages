from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_target_kind import BulkActionTargetKind
from ..models.bulk_action_target_phase import BulkActionTargetPhase
from ..models.bulk_action_target_status import BulkActionTargetStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_change_from import BulkActionChangeFrom
    from ..models.bulk_action_export import BulkActionExport
    from ..models.bulk_action_restore import BulkActionRestore


T = TypeVar("T", bound="BulkActionTarget")


@_attrs_define
class BulkActionTarget:
    """
    Attributes:
        id (str): The persistent server or game server ID; for a pool, its region.
        kind (BulkActionTargetKind):
        batch (int): Its batch, from 1.
        status (BulkActionTargetStatus):
        name (None | str | Unset): A persistent server's name.
        app (str | Unset): App ID.
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        version (None | str | Unset): Its version when it was planned.
        players (int | Unset): Players on it when it was planned.
        reason (None | str | Unset): Why it was skipped or failed: `not_running`, `paused`, `already_current`, `busy`
            (another bulk action is changing it), `no_command` (its version has no such saved command), `no_setting` (its
            version has no such setting, or takes the value differently), `not_applied` (its machine did not make the change
            in the game's file, because it runs an older agent), `window_closed`, `not_delivered`, `boot_failed`, `crashed`,
            `not_back` (not running again in time), `cancelled`, `no_backup` (no backup from before that time), `save_newer`
            (its backup is from a newer version than it runs), `version_gone` (a restore with `version: then` whose backup's
            version was deleted since), `not_saved` (its current state could not be backed up, so it was not restored, or
            not updated: it is back on its old version), `not_updated` (a rollback to before a rollout's update: that
            rollout's version never reached it), `export_failed` (its zip could not be built); new reasons may be added.
        detail (None | str | Unset): A sentence with more about it.
        output (None | str | Unset): Commands: what the game answered, up to 4 KiB.
        http_status (int | None | Unset):
        before (BulkActionChangeFrom | Unset): What a target had before the bulk action changed it.
        restore (BulkActionRestore | Unset): The backup a rollback takes this target to.
        export (BulkActionExport | Unset): A bulk export's zip of one server. `url` is there once it is ready, for a
            caller who can read backups.
        phase (BulkActionTargetPhase | Unset): A running target: a rollback's `saving` (saving, stopping and backing
            up), `restoring` (restoring and starting) and `checking` (running, and watched for `healthy_for`); a pool's
            `checking` (its ready servers on the new version starting, and watched for `healthy_for`).
        game_server (None | str | Unset): Persistent servers: the run it started, once restarted.
        started_at (datetime.datetime | None | Unset): When its step started.
        finished_at (datetime.datetime | None | Unset): When its step ended.
    """

    id: str
    kind: BulkActionTargetKind
    batch: int
    status: BulkActionTargetStatus
    name: None | str | Unset = UNSET
    app: str | Unset = UNSET
    region: str | Unset = UNSET
    version: None | str | Unset = UNSET
    players: int | Unset = UNSET
    reason: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    http_status: int | None | Unset = UNSET
    before: BulkActionChangeFrom | Unset = UNSET
    restore: BulkActionRestore | Unset = UNSET
    export: BulkActionExport | Unset = UNSET
    phase: BulkActionTargetPhase | Unset = UNSET
    game_server: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        batch = self.batch

        status = self.status.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        app = self.app

        region = self.region

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        players = self.players

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        restore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restore, Unset):
            restore = self.restore.to_dict()

        export: dict[str, Any] | Unset = UNSET
        if not isinstance(self.export, Unset):
            export = self.export.to_dict()

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        game_server: None | str | Unset
        if isinstance(self.game_server, Unset):
            game_server = UNSET
        else:
            game_server = self.game_server

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "batch": batch,
                "status": status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if app is not UNSET:
            field_dict["app"] = app
        if region is not UNSET:
            field_dict["region"] = region
        if version is not UNSET:
            field_dict["version"] = version
        if players is not UNSET:
            field_dict["players"] = players
        if reason is not UNSET:
            field_dict["reason"] = reason
        if detail is not UNSET:
            field_dict["detail"] = detail
        if output is not UNSET:
            field_dict["output"] = output
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if before is not UNSET:
            field_dict["before"] = before
        if restore is not UNSET:
            field_dict["restore"] = restore
        if export is not UNSET:
            field_dict["export"] = export
        if phase is not UNSET:
            field_dict["phase"] = phase
        if game_server is not UNSET:
            field_dict["game_server"] = game_server
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_change_from import BulkActionChangeFrom
        from ..models.bulk_action_export import BulkActionExport
        from ..models.bulk_action_restore import BulkActionRestore

        d = dict(src_dict)
        id = d.pop("id")

        kind = BulkActionTargetKind(d.pop("kind"))

        batch = d.pop("batch")

        status = BulkActionTargetStatus(d.pop("status"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        app = d.pop("app", UNSET)

        region = d.pop("region", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        players = d.pop("players", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("http_status", UNSET))

        _before = d.pop("before", UNSET)
        before: BulkActionChangeFrom | Unset
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = BulkActionChangeFrom.from_dict(_before)

        _restore = d.pop("restore", UNSET)
        restore: BulkActionRestore | Unset
        if isinstance(_restore, Unset):
            restore = UNSET
        else:
            restore = BulkActionRestore.from_dict(_restore)

        _export = d.pop("export", UNSET)
        export: BulkActionExport | Unset
        if isinstance(_export, Unset):
            export = UNSET
        else:
            export = BulkActionExport.from_dict(_export)

        _phase = d.pop("phase", UNSET)
        phase: BulkActionTargetPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = BulkActionTargetPhase(_phase)

        def _parse_game_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        game_server = _parse_game_server(d.pop("game_server", UNSET))

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

        bulk_action_target = cls(
            id=id,
            kind=kind,
            batch=batch,
            status=status,
            name=name,
            app=app,
            region=region,
            version=version,
            players=players,
            reason=reason,
            detail=detail,
            output=output,
            http_status=http_status,
            before=before,
            restore=restore,
            export=export,
            phase=phase,
            game_server=game_server,
            started_at=started_at,
            finished_at=finished_at,
        )

        bulk_action_target.additional_properties = d
        return bulk_action_target

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persistent_server_desired_state import PersistentServerDesiredState
from ..models.persistent_server_status import PersistentServerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.backup import Backup
    from ..models.backup_policy import BackupPolicy
    from ..models.backups_failing import BackupsFailing
    from ..models.config_set_ref_type_0 import ConfigSetRefType0
    from ..models.env import Env
    from ..models.labels import Labels
    from ..models.persistent_server_when_empty import PersistentServerWhenEmpty
    from ..models.players import Players
    from ..models.restart_schedule import RestartSchedule
    from ..models.size import Size
    from ..models.stored_backups import StoredBackups


T = TypeVar("T", bound="PersistentServer")


@_attrs_define
class PersistentServer:
    """
    Attributes:
        id (str): Persistent server ID.
        app (str): App ID.
        version (str): Version name, unique in its app, for example `2.3.1`.
        name (str): Its name.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        continent (str): `north-america`, `europe`, `asia`, `oceania`, `south-america`, `middle-east`, `africa`.
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        labels (Labels): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
        status (PersistentServerStatus): `paused`: nobody plays and it is paused (see `when_empty`); `resuming`: a
            player arrived and it is resuming.
        desired_state (PersistentServerDesiredState):
        address (Address): Final at the reply; players can be sent at once.
        players (Players):
        created_at (datetime.datetime): When it was made.
        branch (None | str | Unset):
        env (Env | Unset): Environment variables. Names starting with `GS_` are reserved (`422`).
        args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        save_paths (list[str] | Unset): Folders copied into every backup (Windows relative to the build's top, Linux
            absolute in the container).
        backup (BackupPolicy | Unset):
        restart (RestartSchedule | Unset):
        game_server (None | str | Unset): The current run.
        last_backup (Backup | Unset):
        stored_backups (StoredBackups | Unset): What a persistent server's backups hold. A chunk shared by many backups
            counts once.
        backups_failing (BackupsFailing | Unset): The persistent server's backups are failing: its last tries failed and
            none has been stored since. It clears once a backup is stored. `persistent_server.backup_failed` fires when it
            begins, then at most once a day while it lasts.
        when_empty (PersistentServerWhenEmpty | Unset): Pause when nobody plays and resume on the first player's packet
            or connection, which is answered. A paused persistent server keeps its machine, address and ports. Scheduled
            restarts are skipped while it is paused; a new version or a restart asked for while it is paused is applied at
            once, since nobody is on it.
        paused_since (datetime.datetime | None | Unset): When it was paused (while `paused`).
        stops_instead (bool | Unset): Present and true when this version exited by itself right after a resume from a
            pause (within 30 seconds): the persistent server stops when empty instead, whatever `when_empty.then` says,
            until it runs a new version.
        config_set (ConfigSetRefType0 | None | Unset):
        pending_config_set (ConfigSetRefType0 | None | Unset):
        updated_at (datetime.datetime | Unset): When it last changed.
    """

    id: str
    app: str
    version: str
    name: str
    region: str
    continent: str
    size: Size
    labels: Labels
    status: PersistentServerStatus
    desired_state: PersistentServerDesiredState
    address: Address
    players: Players
    created_at: datetime.datetime
    branch: None | str | Unset = UNSET
    env: Env | Unset = UNSET
    args: list[str] | Unset = UNSET
    save_paths: list[str] | Unset = UNSET
    backup: BackupPolicy | Unset = UNSET
    restart: RestartSchedule | Unset = UNSET
    game_server: None | str | Unset = UNSET
    last_backup: Backup | Unset = UNSET
    stored_backups: StoredBackups | Unset = UNSET
    backups_failing: BackupsFailing | Unset = UNSET
    when_empty: PersistentServerWhenEmpty | Unset = UNSET
    paused_since: datetime.datetime | None | Unset = UNSET
    stops_instead: bool | Unset = UNSET
    config_set: ConfigSetRefType0 | None | Unset = UNSET
    pending_config_set: ConfigSetRefType0 | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_set_ref_type_0 import ConfigSetRefType0

        id = self.id

        app = self.app

        version = self.version

        name = self.name

        region = self.region

        continent = self.continent

        size = self.size.to_dict()

        labels = self.labels.to_dict()

        status = self.status.value

        desired_state = self.desired_state.value

        address = self.address.to_dict()

        players = self.players.to_dict()

        created_at = self.created_at.isoformat()

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        save_paths: list[str] | Unset = UNSET
        if not isinstance(self.save_paths, Unset):
            save_paths = self.save_paths

        backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        game_server: None | str | Unset
        if isinstance(self.game_server, Unset):
            game_server = UNSET
        else:
            game_server = self.game_server

        last_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.to_dict()

        stored_backups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stored_backups, Unset):
            stored_backups = self.stored_backups.to_dict()

        backups_failing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backups_failing, Unset):
            backups_failing = self.backups_failing.to_dict()

        when_empty: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when_empty, Unset):
            when_empty = self.when_empty.to_dict()

        paused_since: None | str | Unset
        if isinstance(self.paused_since, Unset):
            paused_since = UNSET
        elif isinstance(self.paused_since, datetime.datetime):
            paused_since = self.paused_since.isoformat()
        else:
            paused_since = self.paused_since

        stops_instead = self.stops_instead

        config_set: dict[str, Any] | None | Unset
        if isinstance(self.config_set, Unset):
            config_set = UNSET
        elif isinstance(self.config_set, ConfigSetRefType0):
            config_set = self.config_set.to_dict()
        else:
            config_set = self.config_set

        pending_config_set: dict[str, Any] | None | Unset
        if isinstance(self.pending_config_set, Unset):
            pending_config_set = UNSET
        elif isinstance(self.pending_config_set, ConfigSetRefType0):
            pending_config_set = self.pending_config_set.to_dict()
        else:
            pending_config_set = self.pending_config_set

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app": app,
                "version": version,
                "name": name,
                "region": region,
                "continent": continent,
                "size": size,
                "labels": labels,
                "status": status,
                "desired_state": desired_state,
                "address": address,
                "players": players,
                "created_at": created_at,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if env is not UNSET:
            field_dict["env"] = env
        if args is not UNSET:
            field_dict["args"] = args
        if save_paths is not UNSET:
            field_dict["save_paths"] = save_paths
        if backup is not UNSET:
            field_dict["backup"] = backup
        if restart is not UNSET:
            field_dict["restart"] = restart
        if game_server is not UNSET:
            field_dict["game_server"] = game_server
        if last_backup is not UNSET:
            field_dict["last_backup"] = last_backup
        if stored_backups is not UNSET:
            field_dict["stored_backups"] = stored_backups
        if backups_failing is not UNSET:
            field_dict["backups_failing"] = backups_failing
        if when_empty is not UNSET:
            field_dict["when_empty"] = when_empty
        if paused_since is not UNSET:
            field_dict["paused_since"] = paused_since
        if stops_instead is not UNSET:
            field_dict["stops_instead"] = stops_instead
        if config_set is not UNSET:
            field_dict["config_set"] = config_set
        if pending_config_set is not UNSET:
            field_dict["pending_config_set"] = pending_config_set
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.address import Address
        from ..models.backup import Backup
        from ..models.backup_policy import BackupPolicy
        from ..models.backups_failing import BackupsFailing
        from ..models.config_set_ref_type_0 import ConfigSetRefType0
        from ..models.env import Env
        from ..models.labels import Labels
        from ..models.persistent_server_when_empty import PersistentServerWhenEmpty
        from ..models.players import Players
        from ..models.restart_schedule import RestartSchedule
        from ..models.size import Size
        from ..models.stored_backups import StoredBackups

        d = dict(src_dict)
        id = d.pop("id")

        app = d.pop("app")

        version = d.pop("version")

        name = d.pop("name")

        region = d.pop("region")

        continent = d.pop("continent")

        size = Size.from_dict(d.pop("size"))

        labels = Labels.from_dict(d.pop("labels"))

        status = PersistentServerStatus(d.pop("status"))

        desired_state = PersistentServerDesiredState(d.pop("desired_state"))

        address = Address.from_dict(d.pop("address"))

        players = Players.from_dict(d.pop("players"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        _env = d.pop("env", UNSET)
        env: Env | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = Env.from_dict(_env)

        args = cast(list[str], d.pop("args", UNSET))

        save_paths = cast(list[str], d.pop("save_paths", UNSET))

        _backup = d.pop("backup", UNSET)
        backup: BackupPolicy | Unset
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = BackupPolicy.from_dict(_backup)

        _restart = d.pop("restart", UNSET)
        restart: RestartSchedule | Unset
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = RestartSchedule.from_dict(_restart)

        def _parse_game_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        game_server = _parse_game_server(d.pop("game_server", UNSET))

        _last_backup = d.pop("last_backup", UNSET)
        last_backup: Backup | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = Backup.from_dict(_last_backup)

        _stored_backups = d.pop("stored_backups", UNSET)
        stored_backups: StoredBackups | Unset
        if isinstance(_stored_backups, Unset):
            stored_backups = UNSET
        else:
            stored_backups = StoredBackups.from_dict(_stored_backups)

        _backups_failing = d.pop("backups_failing", UNSET)
        backups_failing: BackupsFailing | Unset
        if isinstance(_backups_failing, Unset):
            backups_failing = UNSET
        else:
            backups_failing = BackupsFailing.from_dict(_backups_failing)

        _when_empty = d.pop("when_empty", UNSET)
        when_empty: PersistentServerWhenEmpty | Unset
        if isinstance(_when_empty, Unset):
            when_empty = UNSET
        else:
            when_empty = PersistentServerWhenEmpty.from_dict(_when_empty)

        def _parse_paused_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paused_since_type_0 = datetime.datetime.fromisoformat(data)

                return paused_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paused_since = _parse_paused_since(d.pop("paused_since", UNSET))

        stops_instead = d.pop("stops_instead", UNSET)

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

        def _parse_pending_config_set(data: object) -> ConfigSetRefType0 | None | Unset:
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

        pending_config_set = _parse_pending_config_set(
            d.pop("pending_config_set", UNSET)
        )

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        persistent_server = cls(
            id=id,
            app=app,
            version=version,
            name=name,
            region=region,
            continent=continent,
            size=size,
            labels=labels,
            status=status,
            desired_state=desired_state,
            address=address,
            players=players,
            created_at=created_at,
            branch=branch,
            env=env,
            args=args,
            save_paths=save_paths,
            backup=backup,
            restart=restart,
            game_server=game_server,
            last_backup=last_backup,
            stored_backups=stored_backups,
            backups_failing=backups_failing,
            when_empty=when_empty,
            paused_since=paused_since,
            stops_instead=stops_instead,
            config_set=config_set,
            pending_config_set=pending_config_set,
            updated_at=updated_at,
        )

        persistent_server.additional_properties = d
        return persistent_server

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

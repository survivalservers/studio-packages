from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_policy import BackupPolicy
    from ..models.env import Env
    from ..models.labels import Labels
    from ..models.persistent_server_when_empty import PersistentServerWhenEmpty
    from ..models.restart_schedule import RestartSchedule
    from ..models.size import Size


T = TypeVar("T", bound="PersistentServerCreate")


@_attrs_define
class PersistentServerCreate:
    """
    Attributes:
        app (str): App ID or slug.
        name (str):
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        from_backup (str | Unset): Backup ID.
        version (str | Unset): Version name or ID. Default the `live` branch.
        branch (str | Unset): Branch name, for example `live`.
        size (Size | Unset): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole
            vCPUs. Memory 0.5 GB to 4 GB per vCPU.
        env (Env | Unset): Environment variables. Names starting with `GS_` are reserved (`422`).
        args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        labels (Labels | Unset): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
        save_paths (list[str] | Unset): Folders copied into every backup, and the only ones kept between runs. At least
            one (422 without), unless `from_backup` gives the source server's. Windows builds: relative to the build's top
            folder (for example `BrinewatchServer/Saved/SaveGames`). Linux images: absolute paths inside the container (for
            example `/data/saves`). No `..`. Change them later with `PATCH` while the server is stopped.
        backup (BackupPolicy | Unset):
        restart (RestartSchedule | Unset):
        start (bool | Unset):  Default: True.
        webhook_url (str | Unset):
        when_empty (PersistentServerWhenEmpty | Unset): Pause when nobody plays and resume on the first player's packet
            or connection, which is answered. A paused persistent server keeps its machine, address and ports. Scheduled
            restarts are skipped while it is paused; a new version or a restart asked for while it is paused is applied at
            once, since nobody is on it.
    """

    app: str
    name: str
    region: str
    from_backup: str | Unset = UNSET
    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    size: Size | Unset = UNSET
    env: Env | Unset = UNSET
    args: list[str] | Unset = UNSET
    labels: Labels | Unset = UNSET
    save_paths: list[str] | Unset = UNSET
    backup: BackupPolicy | Unset = UNSET
    restart: RestartSchedule | Unset = UNSET
    start: bool | Unset = True
    webhook_url: str | Unset = UNSET
    when_empty: PersistentServerWhenEmpty | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        name = self.name

        region = self.region

        from_backup = self.from_backup

        version = self.version

        branch = self.branch

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        save_paths: list[str] | Unset = UNSET
        if not isinstance(self.save_paths, Unset):
            save_paths = self.save_paths

        backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        start = self.start

        webhook_url = self.webhook_url

        when_empty: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when_empty, Unset):
            when_empty = self.when_empty.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "name": name,
                "region": region,
            }
        )
        if from_backup is not UNSET:
            field_dict["from_backup"] = from_backup
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if size is not UNSET:
            field_dict["size"] = size
        if env is not UNSET:
            field_dict["env"] = env
        if args is not UNSET:
            field_dict["args"] = args
        if labels is not UNSET:
            field_dict["labels"] = labels
        if save_paths is not UNSET:
            field_dict["save_paths"] = save_paths
        if backup is not UNSET:
            field_dict["backup"] = backup
        if restart is not UNSET:
            field_dict["restart"] = restart
        if start is not UNSET:
            field_dict["start"] = start
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if when_empty is not UNSET:
            field_dict["when_empty"] = when_empty

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_policy import BackupPolicy
        from ..models.env import Env
        from ..models.labels import Labels
        from ..models.persistent_server_when_empty import PersistentServerWhenEmpty
        from ..models.restart_schedule import RestartSchedule
        from ..models.size import Size

        d = dict(src_dict)
        app = d.pop("app")

        name = d.pop("name")

        region = d.pop("region")

        from_backup = d.pop("from_backup", UNSET)

        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

        _size = d.pop("size", UNSET)
        size: Size | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = Size.from_dict(_size)

        _env = d.pop("env", UNSET)
        env: Env | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = Env.from_dict(_env)

        args = cast(list[str], d.pop("args", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = Labels.from_dict(_labels)

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

        start = d.pop("start", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        _when_empty = d.pop("when_empty", UNSET)
        when_empty: PersistentServerWhenEmpty | Unset
        if isinstance(_when_empty, Unset):
            when_empty = UNSET
        else:
            when_empty = PersistentServerWhenEmpty.from_dict(_when_empty)

        persistent_server_create = cls(
            app=app,
            name=name,
            region=region,
            from_backup=from_backup,
            version=version,
            branch=branch,
            size=size,
            env=env,
            args=args,
            labels=labels,
            save_paths=save_paths,
            backup=backup,
            restart=restart,
            start=start,
            webhook_url=webhook_url,
            when_empty=when_empty,
        )

        persistent_server_create.additional_properties = d
        return persistent_server_create

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

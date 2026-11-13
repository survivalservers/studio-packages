from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persistent_server_update_apply import PersistentServerUpdateApply
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_policy import BackupPolicy
    from ..models.env import Env
    from ..models.labels import Labels
    from ..models.persistent_server_when_empty import PersistentServerWhenEmpty
    from ..models.restart_schedule import RestartSchedule
    from ..models.size import Size


T = TypeVar("T", bound="PersistentServerUpdate")


@_attrs_define
class PersistentServerUpdate:
    """
    Attributes:
        version (str | Unset):
        branch (str | Unset): Branch name, for example `live`.
        env (Env | Unset): Environment variables. Names starting with `GS_` are reserved (`422`).
        args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        labels (Labels | Unset): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
        backup (BackupPolicy | Unset):
        save_paths (list[str] | Unset): New save folders, in the same form as at create; at least one. Only while the
            persistent server is stopped (409 otherwise, and while its last backup is still being stored). Its newest
            backup, its saves as they are now, is locked first and labelled "Before its save folders changed" (unless it has
            a label), so you can restore it. The next run keeps and backs up the new folders.
        restart (None | RestartSchedule | Unset): The restart schedule; `null` removes it.
        apply (PersistentServerUpdateApply | Unset):  Default: PersistentServerUpdateApply.NEXT_RESTART.
        when_empty (PersistentServerWhenEmpty | Unset): Pause when nobody plays and resume on the first player's packet
            or connection, which is answered. A paused persistent server keeps its machine, address and ports. Scheduled
            restarts are skipped while it is paused; a new version or a restart asked for while it is paused is applied at
            once, since nobody is on it.
        size (Size | Unset): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole
            vCPUs. Memory 0.5 GB to 4 GB per vCPU.
    """

    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    env: Env | Unset = UNSET
    args: list[str] | Unset = UNSET
    labels: Labels | Unset = UNSET
    backup: BackupPolicy | Unset = UNSET
    save_paths: list[str] | Unset = UNSET
    restart: None | RestartSchedule | Unset = UNSET
    apply: PersistentServerUpdateApply | Unset = (
        PersistentServerUpdateApply.NEXT_RESTART
    )
    when_empty: PersistentServerWhenEmpty | Unset = UNSET
    size: Size | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.restart_schedule import RestartSchedule

        version = self.version

        branch = self.branch

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup, Unset):
            backup = self.backup.to_dict()

        save_paths: list[str] | Unset = UNSET
        if not isinstance(self.save_paths, Unset):
            save_paths = self.save_paths

        restart: dict[str, Any] | None | Unset
        if isinstance(self.restart, Unset):
            restart = UNSET
        elif isinstance(self.restart, RestartSchedule):
            restart = self.restart.to_dict()
        else:
            restart = self.restart

        apply: str | Unset = UNSET
        if not isinstance(self.apply, Unset):
            apply = self.apply.value

        when_empty: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when_empty, Unset):
            when_empty = self.when_empty.to_dict()

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if env is not UNSET:
            field_dict["env"] = env
        if args is not UNSET:
            field_dict["args"] = args
        if labels is not UNSET:
            field_dict["labels"] = labels
        if backup is not UNSET:
            field_dict["backup"] = backup
        if save_paths is not UNSET:
            field_dict["save_paths"] = save_paths
        if restart is not UNSET:
            field_dict["restart"] = restart
        if apply is not UNSET:
            field_dict["apply"] = apply
        if when_empty is not UNSET:
            field_dict["when_empty"] = when_empty
        if size is not UNSET:
            field_dict["size"] = size

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
        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

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

        _backup = d.pop("backup", UNSET)
        backup: BackupPolicy | Unset
        if isinstance(_backup, Unset):
            backup = UNSET
        else:
            backup = BackupPolicy.from_dict(_backup)

        save_paths = cast(list[str], d.pop("save_paths", UNSET))

        def _parse_restart(data: object) -> None | RestartSchedule | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restart_type_0 = RestartSchedule.from_dict(data)

                return restart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RestartSchedule | Unset, data)

        restart = _parse_restart(d.pop("restart", UNSET))

        _apply = d.pop("apply", UNSET)
        apply: PersistentServerUpdateApply | Unset
        if isinstance(_apply, Unset):
            apply = UNSET
        else:
            apply = PersistentServerUpdateApply(_apply)

        _when_empty = d.pop("when_empty", UNSET)
        when_empty: PersistentServerWhenEmpty | Unset
        if isinstance(_when_empty, Unset):
            when_empty = UNSET
        else:
            when_empty = PersistentServerWhenEmpty.from_dict(_when_empty)

        _size = d.pop("size", UNSET)
        size: Size | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = Size.from_dict(_size)

        persistent_server_update = cls(
            version=version,
            branch=branch,
            env=env,
            args=args,
            labels=labels,
            backup=backup,
            save_paths=save_paths,
            restart=restart,
            apply=apply,
            when_empty=when_empty,
            size=size,
        )

        persistent_server_update.additional_properties = d
        return persistent_server_update

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

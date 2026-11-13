from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.launch_compat_item import LaunchCompatItem
from ..models.launch_crash_dump import LaunchCrashDump
from ..models.launch_env_aliases_item import LaunchEnvAliasesItem
from ..models.launch_stdin import LaunchStdin
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launch_env import LaunchEnv
    from ..models.launch_file import LaunchFile
    from ..models.port_spec import PortSpec
    from ..models.ready_check_delay import ReadyCheckDelay
    from ..models.ready_check_local_api import ReadyCheckLocalApi
    from ..models.ready_check_log import ReadyCheckLog
    from ..models.ready_check_none import ReadyCheckNone
    from ..models.ready_check_port import ReadyCheckPort
    from ..models.save_spec import SaveSpec
    from ..models.stop_spec import StopSpec


T = TypeVar("T", bound="Launch")


@_attrs_define
class Launch:
    """
    Attributes:
        executable (str | Unset): Path inside the zip (Windows). Linux - optional, overrides the image entrypoint.
        args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        env (LaunchEnv | Unset): Environment variables for every game server of the version. Names starting with `GS_`
            are reserved (`422`). A value can also be made new for each game server (GeneratedEnvValue).
        files (list[LaunchFile] | Unset): Small files the machine writes before every start, for a game that reads its
            admin or RCON password from a file of its own. `content` takes the same templates as `args`, `{{env.<NAME>}}`
            included, filled in on the machine. A file replaces whatever the build has at that path. Windows: written into
            the game server's own folder, which only your studio's account can read; Linux: kept in memory, never on the
            machine's disk. Up to 16 files and 512 KiB in all; never inside a persistent server's save paths (its snapshots
            would keep it).
        ports (list[PortSpec] | Unset): Named ports. We assign the public port on every start (a fresh one per match).
            An admin port (`port_policy` `none`) gets no public port. On Linux a public port has a `container_port`, or
            `port_policy` `passthrough` for a game that must listen on its public number itself.
        ready_check (ReadyCheckDelay | ReadyCheckLocalApi | ReadyCheckLog | ReadyCheckNone | ReadyCheckPort | Unset):
            When a game server counts as joinable.
        stop (StopSpec | Unset):
        save (SaveSpec | Unset): How to make the game save, for servers that do not save on their own before a backup:
            sent before every persistent server backup (manual, scheduled and at a stop) and before the stop method. A save
            that fails or runs out of time does not hold up the backup; the timeline says `save_failed`.
        init (bool | Unset): Default true. Linux: every game server starts under a small init (open source) as the
            container's process 1. It forwards stop signals to the game's process group, reaps orphaned processes and passes
            the game's exit code through. Turn it off only for an image that must be process 1 itself (for example
            s6-overlay); console stop and save commands need it. Windows builds ignore it.
        stdin (LaunchStdin | Unset): What the server reads as its standard input. `console` (the default): a console
            that console stop, save and typed commands write into, as when you start the server by hand. On Windows its own
            console, hidden; in a Linux image a terminal the init (`init`) holds open, so the input never ends (with `init`
            off a Linux game server has no console input). `none`: no input at all, for a server that must see its input end
            at once; a version with a console stop or save command cannot use it.
        boot_timeout (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        health_timeout (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as
            seconds.
        log_paths (list[str] | Unset): File logs kept in addition to the console (globs inside the game server's
            folder).
        artifact_paths (list[str] | Unset): Files collected at exit. A crash dump is never one of them, and is caught by
            the machine itself. A pattern that names dumps (`*.dmp`, `*.mdmp`, `core`, `core.*`, `*.core`) is refused, and a
            dump that a broader pattern matches is left out.
        crash_dump (LaunchCrashDump | Unset):  Default: LaunchCrashDump.MINI.
        env_aliases (list[LaunchEnvAliasesItem] | Unset): Also set that host's variable names: `hathora` (`HATHORA_*`),
            `gameye` (`GAMEYE_*`) or `edgegap` (`ARBITRIUM_*`: the request ID, address, ports, resources and location; a
            deployment started through the Edgegap translator also gets its tags and self-stop URL and token).
        compat (list[LaunchCompatItem] | Unset): SDKs the game already speaks that the machine answers as, for each game
            server of this version: `agones` (the Agones SDK server), `playfab` (the PlayFab agent the GSDK talks to) or
            `gamelift` (Amazon GameLift Servers' server SDK 5.x; Linux builds for now); more than one may be set for a build
            that links several. Use the ready check `local_api`: the SDK's ready call is what reports the game server ready.
            The start's env, external_id and labels reach them as each SDK expects (see the guides).
    """

    executable: str | Unset = UNSET
    args: list[str] | Unset = UNSET
    env: LaunchEnv | Unset = UNSET
    files: list[LaunchFile] | Unset = UNSET
    ports: list[PortSpec] | Unset = UNSET
    ready_check: (
        ReadyCheckDelay
        | ReadyCheckLocalApi
        | ReadyCheckLog
        | ReadyCheckNone
        | ReadyCheckPort
        | Unset
    ) = UNSET
    stop: StopSpec | Unset = UNSET
    save: SaveSpec | Unset = UNSET
    init: bool | Unset = UNSET
    stdin: LaunchStdin | Unset = UNSET
    boot_timeout: int | str | Unset = UNSET
    health_timeout: int | str | Unset = UNSET
    log_paths: list[str] | Unset = UNSET
    artifact_paths: list[str] | Unset = UNSET
    crash_dump: LaunchCrashDump | Unset = LaunchCrashDump.MINI
    env_aliases: list[LaunchEnvAliasesItem] | Unset = UNSET
    compat: list[LaunchCompatItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ready_check_delay import ReadyCheckDelay
        from ..models.ready_check_local_api import ReadyCheckLocalApi
        from ..models.ready_check_log import ReadyCheckLog
        from ..models.ready_check_port import ReadyCheckPort

        executable = self.executable

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        ready_check: dict[str, Any] | Unset
        if isinstance(self.ready_check, Unset):
            ready_check = UNSET
        elif (
            isinstance(self.ready_check, ReadyCheckLocalApi)
            or isinstance(self.ready_check, ReadyCheckLog)
            or isinstance(self.ready_check, ReadyCheckPort)
            or isinstance(self.ready_check, ReadyCheckDelay)
        ):
            ready_check = self.ready_check.to_dict()
        else:
            ready_check = self.ready_check.to_dict()

        stop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.to_dict()

        save: dict[str, Any] | Unset = UNSET
        if not isinstance(self.save, Unset):
            save = self.save.to_dict()

        init = self.init

        stdin: str | Unset = UNSET
        if not isinstance(self.stdin, Unset):
            stdin = self.stdin.value

        boot_timeout: int | str | Unset
        if isinstance(self.boot_timeout, Unset):
            boot_timeout = UNSET
        else:
            boot_timeout = self.boot_timeout

        health_timeout: int | str | Unset
        if isinstance(self.health_timeout, Unset):
            health_timeout = UNSET
        else:
            health_timeout = self.health_timeout

        log_paths: list[str] | Unset = UNSET
        if not isinstance(self.log_paths, Unset):
            log_paths = self.log_paths

        artifact_paths: list[str] | Unset = UNSET
        if not isinstance(self.artifact_paths, Unset):
            artifact_paths = self.artifact_paths

        crash_dump: str | Unset = UNSET
        if not isinstance(self.crash_dump, Unset):
            crash_dump = self.crash_dump.value

        env_aliases: list[str] | Unset = UNSET
        if not isinstance(self.env_aliases, Unset):
            env_aliases = []
            for env_aliases_item_data in self.env_aliases:
                env_aliases_item = env_aliases_item_data.value
                env_aliases.append(env_aliases_item)

        compat: list[str] | Unset = UNSET
        if not isinstance(self.compat, Unset):
            compat = []
            for compat_item_data in self.compat:
                compat_item = compat_item_data.value
                compat.append(compat_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if executable is not UNSET:
            field_dict["executable"] = executable
        if args is not UNSET:
            field_dict["args"] = args
        if env is not UNSET:
            field_dict["env"] = env
        if files is not UNSET:
            field_dict["files"] = files
        if ports is not UNSET:
            field_dict["ports"] = ports
        if ready_check is not UNSET:
            field_dict["ready_check"] = ready_check
        if stop is not UNSET:
            field_dict["stop"] = stop
        if save is not UNSET:
            field_dict["save"] = save
        if init is not UNSET:
            field_dict["init"] = init
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if boot_timeout is not UNSET:
            field_dict["boot_timeout"] = boot_timeout
        if health_timeout is not UNSET:
            field_dict["health_timeout"] = health_timeout
        if log_paths is not UNSET:
            field_dict["log_paths"] = log_paths
        if artifact_paths is not UNSET:
            field_dict["artifact_paths"] = artifact_paths
        if crash_dump is not UNSET:
            field_dict["crash_dump"] = crash_dump
        if env_aliases is not UNSET:
            field_dict["env_aliases"] = env_aliases
        if compat is not UNSET:
            field_dict["compat"] = compat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.launch_env import LaunchEnv
        from ..models.launch_file import LaunchFile
        from ..models.port_spec import PortSpec
        from ..models.ready_check_delay import ReadyCheckDelay
        from ..models.ready_check_local_api import ReadyCheckLocalApi
        from ..models.ready_check_log import ReadyCheckLog
        from ..models.ready_check_none import ReadyCheckNone
        from ..models.ready_check_port import ReadyCheckPort
        from ..models.save_spec import SaveSpec
        from ..models.stop_spec import StopSpec

        d = dict(src_dict)
        executable = d.pop("executable", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        _env = d.pop("env", UNSET)
        env: LaunchEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = LaunchEnv.from_dict(_env)

        _files = d.pop("files", UNSET)
        files: list[LaunchFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = LaunchFile.from_dict(files_item_data)

                files.append(files_item)

        _ports = d.pop("ports", UNSET)
        ports: list[PortSpec] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = PortSpec.from_dict(ports_item_data)

                ports.append(ports_item)

        def _parse_ready_check(
            data: object,
        ) -> (
            ReadyCheckDelay
            | ReadyCheckLocalApi
            | ReadyCheckLog
            | ReadyCheckNone
            | ReadyCheckPort
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ready_check_type_0 = ReadyCheckLocalApi.from_dict(
                    data
                )

                return componentsschemas_ready_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ready_check_type_1 = ReadyCheckLog.from_dict(data)

                return componentsschemas_ready_check_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ready_check_type_2 = ReadyCheckPort.from_dict(data)

                return componentsschemas_ready_check_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ready_check_type_3 = ReadyCheckDelay.from_dict(data)

                return componentsschemas_ready_check_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ready_check_type_4 = ReadyCheckNone.from_dict(data)

            return componentsschemas_ready_check_type_4

        ready_check = _parse_ready_check(d.pop("ready_check", UNSET))

        _stop = d.pop("stop", UNSET)
        stop: StopSpec | Unset
        if isinstance(_stop, Unset):
            stop = UNSET
        else:
            stop = StopSpec.from_dict(_stop)

        _save = d.pop("save", UNSET)
        save: SaveSpec | Unset
        if isinstance(_save, Unset):
            save = UNSET
        else:
            save = SaveSpec.from_dict(_save)

        init = d.pop("init", UNSET)

        _stdin = d.pop("stdin", UNSET)
        stdin: LaunchStdin | Unset
        if isinstance(_stdin, Unset):
            stdin = UNSET
        else:
            stdin = LaunchStdin(_stdin)

        def _parse_boot_timeout(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        boot_timeout = _parse_boot_timeout(d.pop("boot_timeout", UNSET))

        def _parse_health_timeout(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        health_timeout = _parse_health_timeout(d.pop("health_timeout", UNSET))

        log_paths = cast(list[str], d.pop("log_paths", UNSET))

        artifact_paths = cast(list[str], d.pop("artifact_paths", UNSET))

        _crash_dump = d.pop("crash_dump", UNSET)
        crash_dump: LaunchCrashDump | Unset
        if isinstance(_crash_dump, Unset):
            crash_dump = UNSET
        else:
            crash_dump = LaunchCrashDump(_crash_dump)

        _env_aliases = d.pop("env_aliases", UNSET)
        env_aliases: list[LaunchEnvAliasesItem] | Unset = UNSET
        if _env_aliases is not UNSET:
            env_aliases = []
            for env_aliases_item_data in _env_aliases:
                env_aliases_item = LaunchEnvAliasesItem(env_aliases_item_data)

                env_aliases.append(env_aliases_item)

        _compat = d.pop("compat", UNSET)
        compat: list[LaunchCompatItem] | Unset = UNSET
        if _compat is not UNSET:
            compat = []
            for compat_item_data in _compat:
                compat_item = LaunchCompatItem(compat_item_data)

                compat.append(compat_item)

        launch = cls(
            executable=executable,
            args=args,
            env=env,
            files=files,
            ports=ports,
            ready_check=ready_check,
            stop=stop,
            save=save,
            init=init,
            stdin=stdin,
            boot_timeout=boot_timeout,
            health_timeout=health_timeout,
            log_paths=log_paths,
            artifact_paths=artifact_paths,
            crash_dump=crash_dump,
            env_aliases=env_aliases,
            compat=compat,
        )

        launch.additional_properties = d
        return launch

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

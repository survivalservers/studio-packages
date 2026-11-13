from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_mode import StartMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env import Env
    from ..models.labels import Labels
    from ..models.placement import Placement
    from ..models.size import Size


T = TypeVar("T", bound="GameServerCreate")


@_attrs_define
class GameServerCreate:
    """
    Attributes:
        app (str): App ID or slug.
        version (str | Unset): Version name or ID. Default the `live` branch.
        branch (str | Unset): Branch name, for example `live`.
        placement (Placement | Unset):
        start_mode (StartMode | Unset):  Default: StartMode.AUTO.
        size (Size | Unset): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole
            vCPUs. Memory 0.5 GB to 4 GB per vCPU.
        env (Env | Unset): Environment variables. Names starting with `GS_` are reserved (`422`).
        args (list[str] | Unset): Added after the version's own arguments, with the same templates: `{{port.<name>}}`,
            `{{public_ip}}`, `{{id}}`, `{{region}}`, `{{cpu}}`, `{{memory_mb}}`, and `{{env.<NAME>}}` from the version's env
            or this one's, secret ones too (filled in on the machine as the game starts, never shown). A warm start hands
            its arguments to the running game as allocation data, as written.
        labels (Labels | Unset): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
        external_id (str | Unset):
        ttl (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
        webhook_url (str | Unset): Receives this game server's events, signed with the default endpoint's secret.
    """

    app: str
    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    placement: Placement | Unset = UNSET
    start_mode: StartMode | Unset = StartMode.AUTO
    size: Size | Unset = UNSET
    env: Env | Unset = UNSET
    args: list[str] | Unset = UNSET
    labels: Labels | Unset = UNSET
    external_id: str | Unset = UNSET
    ttl: int | str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        version = self.version

        branch = self.branch

        placement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.placement, Unset):
            placement = self.placement.to_dict()

        start_mode: str | Unset = UNSET
        if not isinstance(self.start_mode, Unset):
            start_mode = self.start_mode.value

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

        external_id = self.external_id

        ttl: int | str | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if placement is not UNSET:
            field_dict["placement"] = placement
        if start_mode is not UNSET:
            field_dict["start_mode"] = start_mode
        if size is not UNSET:
            field_dict["size"] = size
        if env is not UNSET:
            field_dict["env"] = env
        if args is not UNSET:
            field_dict["args"] = args
        if labels is not UNSET:
            field_dict["labels"] = labels
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.env import Env
        from ..models.labels import Labels
        from ..models.placement import Placement
        from ..models.size import Size

        d = dict(src_dict)
        app = d.pop("app")

        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

        _placement = d.pop("placement", UNSET)
        placement: Placement | Unset
        if isinstance(_placement, Unset):
            placement = UNSET
        else:
            placement = Placement.from_dict(_placement)

        _start_mode = d.pop("start_mode", UNSET)
        start_mode: StartMode | Unset
        if isinstance(_start_mode, Unset):
            start_mode = UNSET
        else:
            start_mode = StartMode(_start_mode)

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

        external_id = d.pop("external_id", UNSET)

        def _parse_ttl(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        webhook_url = d.pop("webhook_url", UNSET)

        game_server_create = cls(
            app=app,
            version=version,
            branch=branch,
            placement=placement,
            start_mode=start_mode,
            size=size,
            env=env,
            args=args,
            labels=labels,
            external_id=external_id,
            ttl=ttl,
            webhook_url=webhook_url,
        )

        game_server_create.additional_properties = d
        return game_server_create

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

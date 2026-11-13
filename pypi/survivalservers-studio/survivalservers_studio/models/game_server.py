from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.game_server_start_mode import GameServerStartMode
from ..models.game_server_status import GameServerStatus
from ..models.os import Os
from ..models.tier import Tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.game_server_exit import GameServerExit
    from ..models.labels import Labels
    from ..models.placement_result import PlacementResult
    from ..models.players import Players
    from ..models.size import Size
    from ..models.timings import Timings


T = TypeVar("T", bound="GameServer")


@_attrs_define
class GameServer:
    """
    Attributes:
        id (str): Game server ID.
        status (GameServerStatus):
        start_mode (GameServerStartMode):
        app (str): App ID.
        version (str): Version name, unique in its app, for example `2.3.1`.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        continent (str): `north-america`, `europe`, `asia`, `oceania`, `south-america`, `middle-east`, `africa`.
        tier (Tier): Public hardware tier.
        os (Os):
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        address (Address): Final at the reply; players can be sent at once.
        labels (Labels): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
        players (Players):
        created_at (datetime.datetime): When it was made.
        persistent_server (None | str | Unset): The persistent server this run belongs to, if any.
        external_id (None | str | Unset):
        placement (PlacementResult | Unset):
        running_at (datetime.datetime | None | Unset): When it became joinable.
        expires_at (datetime.datetime | None | Unset): When it expires.
        stopped_at (datetime.datetime | None | Unset): When it ended.
        exit_ (GameServerExit | Unset): Present once the game server has ended.
        restarts (int | Unset):
        timings_ms (Timings | Unset): Milliseconds spent on the start, measured at our API edge.
    """

    id: str
    status: GameServerStatus
    start_mode: GameServerStartMode
    app: str
    version: str
    region: str
    continent: str
    tier: Tier
    os: Os
    size: Size
    address: Address
    labels: Labels
    players: Players
    created_at: datetime.datetime
    persistent_server: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    placement: PlacementResult | Unset = UNSET
    running_at: datetime.datetime | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    stopped_at: datetime.datetime | None | Unset = UNSET
    exit_: GameServerExit | Unset = UNSET
    restarts: int | Unset = UNSET
    timings_ms: Timings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        start_mode = self.start_mode.value

        app = self.app

        version = self.version

        region = self.region

        continent = self.continent

        tier = self.tier.value

        os = self.os.value

        size = self.size.to_dict()

        address = self.address.to_dict()

        labels = self.labels.to_dict()

        players = self.players.to_dict()

        created_at = self.created_at.isoformat()

        persistent_server: None | str | Unset
        if isinstance(self.persistent_server, Unset):
            persistent_server = UNSET
        else:
            persistent_server = self.persistent_server

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        placement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.placement, Unset):
            placement = self.placement.to_dict()

        running_at: None | str | Unset
        if isinstance(self.running_at, Unset):
            running_at = UNSET
        elif isinstance(self.running_at, datetime.datetime):
            running_at = self.running_at.isoformat()
        else:
            running_at = self.running_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        stopped_at: None | str | Unset
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        elif isinstance(self.stopped_at, datetime.datetime):
            stopped_at = self.stopped_at.isoformat()
        else:
            stopped_at = self.stopped_at

        exit_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exit_, Unset):
            exit_ = self.exit_.to_dict()

        restarts = self.restarts

        timings_ms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timings_ms, Unset):
            timings_ms = self.timings_ms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "start_mode": start_mode,
                "app": app,
                "version": version,
                "region": region,
                "continent": continent,
                "tier": tier,
                "os": os,
                "size": size,
                "address": address,
                "labels": labels,
                "players": players,
                "created_at": created_at,
            }
        )
        if persistent_server is not UNSET:
            field_dict["persistent_server"] = persistent_server
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if placement is not UNSET:
            field_dict["placement"] = placement
        if running_at is not UNSET:
            field_dict["running_at"] = running_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if stopped_at is not UNSET:
            field_dict["stopped_at"] = stopped_at
        if exit_ is not UNSET:
            field_dict["exit"] = exit_
        if restarts is not UNSET:
            field_dict["restarts"] = restarts
        if timings_ms is not UNSET:
            field_dict["timings_ms"] = timings_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.address import Address
        from ..models.game_server_exit import GameServerExit
        from ..models.labels import Labels
        from ..models.placement_result import PlacementResult
        from ..models.players import Players
        from ..models.size import Size
        from ..models.timings import Timings

        d = dict(src_dict)
        id = d.pop("id")

        status = GameServerStatus(d.pop("status"))

        start_mode = GameServerStartMode(d.pop("start_mode"))

        app = d.pop("app")

        version = d.pop("version")

        region = d.pop("region")

        continent = d.pop("continent")

        tier = Tier(d.pop("tier"))

        os = Os(d.pop("os"))

        size = Size.from_dict(d.pop("size"))

        address = Address.from_dict(d.pop("address"))

        labels = Labels.from_dict(d.pop("labels"))

        players = Players.from_dict(d.pop("players"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_persistent_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        persistent_server = _parse_persistent_server(d.pop("persistent_server", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        _placement = d.pop("placement", UNSET)
        placement: PlacementResult | Unset
        if isinstance(_placement, Unset):
            placement = UNSET
        else:
            placement = PlacementResult.from_dict(_placement)

        def _parse_running_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                running_at_type_0 = datetime.datetime.fromisoformat(data)

                return running_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        running_at = _parse_running_at(d.pop("running_at", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_stopped_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stopped_at_type_0 = datetime.datetime.fromisoformat(data)

                return stopped_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        stopped_at = _parse_stopped_at(d.pop("stopped_at", UNSET))

        _exit_ = d.pop("exit", UNSET)
        exit_: GameServerExit | Unset
        if isinstance(_exit_, Unset):
            exit_ = UNSET
        else:
            exit_ = GameServerExit.from_dict(_exit_)

        restarts = d.pop("restarts", UNSET)

        _timings_ms = d.pop("timings_ms", UNSET)
        timings_ms: Timings | Unset
        if isinstance(_timings_ms, Unset):
            timings_ms = UNSET
        else:
            timings_ms = Timings.from_dict(_timings_ms)

        game_server = cls(
            id=id,
            status=status,
            start_mode=start_mode,
            app=app,
            version=version,
            region=region,
            continent=continent,
            tier=tier,
            os=os,
            size=size,
            address=address,
            labels=labels,
            players=players,
            created_at=created_at,
            persistent_server=persistent_server,
            external_id=external_id,
            placement=placement,
            running_at=running_at,
            expires_at=expires_at,
            stopped_at=stopped_at,
            exit_=exit_,
            restarts=restarts,
            timings_ms=timings_ms,
        )

        game_server.additional_properties = d
        return game_server

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

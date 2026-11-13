from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_server_stats_group import GameServerStatsGroup


T = TypeVar("T", bound="GameServerStatsBucket")


@_attrs_define
class GameServerStatsBucket:
    """
    Attributes:
        t (datetime.datetime): The bucket's start.
        game_servers_running (float): Average running, time-weighted: matches from their creation (a warm slot from its
            hand-over) and persistent server runs, until they stop; warm slots only with `kind` `warm`.
        game_servers_peak (int): Most running at once. Over several regions, the sum of each part's own peak.
        players_online (float): Average players, time-weighted.
        players_peak (int): Most players at once. Over several regions, the sum of each part's own peak.
        cpu_in_use (float): Average vCPUs held, time-weighted: every game server, warm slots included, from its creation
            to its stop.
        starts (int):
        failed_starts (int): Starts that failed on our side.
        crashes (int): Game servers that ended with `crashed` true.
        stops (int): Game servers that ended any other way (warm slots only with `kind` `warm`).
        group (GameServerStatsGroup | Unset): The group's values, for each `group_by` asked for.
        simulated_players_online (float | Unset): Our own test setup only: average simulated players, time-weighted.
            Never part of `players_online`. Left out when there were none.
        simulated_players_peak (int | Unset): Our own test setup only: most simulated players at once. Left out when
            there were none.
    """

    t: datetime.datetime
    game_servers_running: float
    game_servers_peak: int
    players_online: float
    players_peak: int
    cpu_in_use: float
    starts: int
    failed_starts: int
    crashes: int
    stops: int
    group: GameServerStatsGroup | Unset = UNSET
    simulated_players_online: float | Unset = UNSET
    simulated_players_peak: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        t = self.t.isoformat()

        game_servers_running = self.game_servers_running

        game_servers_peak = self.game_servers_peak

        players_online = self.players_online

        players_peak = self.players_peak

        cpu_in_use = self.cpu_in_use

        starts = self.starts

        failed_starts = self.failed_starts

        crashes = self.crashes

        stops = self.stops

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        simulated_players_online = self.simulated_players_online

        simulated_players_peak = self.simulated_players_peak

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t": t,
                "game_servers_running": game_servers_running,
                "game_servers_peak": game_servers_peak,
                "players_online": players_online,
                "players_peak": players_peak,
                "cpu_in_use": cpu_in_use,
                "starts": starts,
                "failed_starts": failed_starts,
                "crashes": crashes,
                "stops": stops,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if simulated_players_online is not UNSET:
            field_dict["simulated_players_online"] = simulated_players_online
        if simulated_players_peak is not UNSET:
            field_dict["simulated_players_peak"] = simulated_players_peak

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_server_stats_group import GameServerStatsGroup

        d = dict(src_dict)
        t = datetime.datetime.fromisoformat(d.pop("t"))

        game_servers_running = d.pop("game_servers_running")

        game_servers_peak = d.pop("game_servers_peak")

        players_online = d.pop("players_online")

        players_peak = d.pop("players_peak")

        cpu_in_use = d.pop("cpu_in_use")

        starts = d.pop("starts")

        failed_starts = d.pop("failed_starts")

        crashes = d.pop("crashes")

        stops = d.pop("stops")

        _group = d.pop("group", UNSET)
        group: GameServerStatsGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GameServerStatsGroup.from_dict(_group)

        simulated_players_online = d.pop("simulated_players_online", UNSET)

        simulated_players_peak = d.pop("simulated_players_peak", UNSET)

        game_server_stats_bucket = cls(
            t=t,
            game_servers_running=game_servers_running,
            game_servers_peak=game_servers_peak,
            players_online=players_online,
            players_peak=players_peak,
            cpu_in_use=cpu_in_use,
            starts=starts,
            failed_starts=failed_starts,
            crashes=crashes,
            stops=stops,
            group=group,
            simulated_players_online=simulated_players_online,
            simulated_players_peak=simulated_players_peak,
        )

        game_server_stats_bucket.additional_properties = d
        return game_server_stats_bucket

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

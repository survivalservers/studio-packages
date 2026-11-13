from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_players_source import ServerPlayersSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_player import ServerPlayer


T = TypeVar("T", bound="ServerPlayers")


@_attrs_define
class ServerPlayers:
    """
    Attributes:
        players (list[ServerPlayer]):
        source (ServerPlayersSource): `reported`: what the game said on the local API. `query`: a Steam query port.
            `connection`: asked through the game profile.
        truncated (bool | Unset): The answer was too long to read all of it.
        error (str | Unset): Why the game could not be asked.
    """

    players: list[ServerPlayer]
    source: ServerPlayersSource
    truncated: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        source = self.source.value

        truncated = self.truncated

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
                "source": source,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_player import ServerPlayer

        d = dict(src_dict)
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = ServerPlayer.from_dict(players_item_data)

            players.append(players_item)

        source = ServerPlayersSource(d.pop("source"))

        truncated = d.pop("truncated", UNSET)

        error = d.pop("error", UNSET)

        server_players = cls(
            players=players,
            source=source,
            truncated=truncated,
            error=error,
        )

        server_players.additional_properties = d
        return server_players

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

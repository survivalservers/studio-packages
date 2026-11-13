from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_profile_connections import GameProfileConnections
    from ..models.profile_command import ProfileCommand
    from ..models.profile_config import ProfileConfig
    from ..models.profile_map import ProfileMap
    from ..models.profile_players import ProfilePlayers


T = TypeVar("T", bound="GameProfile")


@_attrs_define
class GameProfile:
    """One description of a server, read by the panel, the API, the CLI and AI tools: how to reach the game and the
    commands it takes. Plain JSON, and every part is optional. Secrets stay in the version's env values; a profile only
    names them.

        Attributes:
            connections (GameProfileConnections | Unset): Ways to reach the game, by a name of your choice. `console` is
                always there: the game's standard input.
            commands (list[ProfileCommand] | Unset): Saved commands, which the panel shows as buttons and any API call can
                run by `id`.
            config (ProfileConfig | Unset): The game's settings as data. The panel draws its config form from this, and a
                change writes only the keys it names.
            players (ProfilePlayers | Unset): How to read who is on a server. The Players card reads it while someone looks.
                The machine also reads the count with it every 30 seconds (60 for a console line) while the game server runs,
                for a game that does not report its players on the local API, so the Overview and the players charts count real
                players. Only the count is kept, never names or positions. With none, the players the game reported on the local
                API are used.
            maps (list[ProfileMap] | Unset): The game's maps, so the panel can draw players on them.
    """

    connections: GameProfileConnections | Unset = UNSET
    commands: list[ProfileCommand] | Unset = UNSET
    config: ProfileConfig | Unset = UNSET
    players: ProfilePlayers | Unset = UNSET
    maps: list[ProfileMap] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        connections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = self.connections.to_dict()

        commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = []
            for commands_item_data in self.commands:
                commands_item = commands_item_data.to_dict()
                commands.append(commands_item)

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        players: dict[str, Any] | Unset = UNSET
        if not isinstance(self.players, Unset):
            players = self.players.to_dict()

        maps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maps, Unset):
            maps = []
            for maps_item_data in self.maps:
                maps_item = maps_item_data.to_dict()
                maps.append(maps_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections
        if commands is not UNSET:
            field_dict["commands"] = commands
        if config is not UNSET:
            field_dict["config"] = config
        if players is not UNSET:
            field_dict["players"] = players
        if maps is not UNSET:
            field_dict["maps"] = maps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_profile_connections import GameProfileConnections
        from ..models.profile_command import ProfileCommand
        from ..models.profile_config import ProfileConfig
        from ..models.profile_map import ProfileMap
        from ..models.profile_players import ProfilePlayers

        d = dict(src_dict)
        _connections = d.pop("connections", UNSET)
        connections: GameProfileConnections | Unset
        if isinstance(_connections, Unset):
            connections = UNSET
        else:
            connections = GameProfileConnections.from_dict(_connections)

        _commands = d.pop("commands", UNSET)
        commands: list[ProfileCommand] | Unset = UNSET
        if _commands is not UNSET:
            commands = []
            for commands_item_data in _commands:
                commands_item = ProfileCommand.from_dict(commands_item_data)

                commands.append(commands_item)

        _config = d.pop("config", UNSET)
        config: ProfileConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ProfileConfig.from_dict(_config)

        _players = d.pop("players", UNSET)
        players: ProfilePlayers | Unset
        if isinstance(_players, Unset):
            players = UNSET
        else:
            players = ProfilePlayers.from_dict(_players)

        _maps = d.pop("maps", UNSET)
        maps: list[ProfileMap] | Unset = UNSET
        if _maps is not UNSET:
            maps = []
            for maps_item_data in _maps:
                maps_item = ProfileMap.from_dict(maps_item_data)

                maps.append(maps_item)

        game_profile = cls(
            connections=connections,
            commands=commands,
            config=config,
            players=players,
            maps=maps,
        )

        return game_profile

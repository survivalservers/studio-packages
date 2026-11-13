from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.profile_players_method import ProfilePlayersMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_players_parse import ProfilePlayersParse


T = TypeVar("T", bound="ProfilePlayers")


@_attrs_define
class ProfilePlayers:
    """How to read who is on a server. The Players card reads it while someone looks. The machine also reads the count with
    it every 30 seconds (60 for a console line) while the game server runs, for a game that does not report its players
    on the local API, so the Overview and the players charts count real players. Only the count is kept, never names or
    positions. With none, the players the game reported on the local API are used.

        Attributes:
            via (str | Unset): A connection's name. An `a2s` or `isle_rcon` connection needs nothing else; an `a2s` one may
                take `rules_count`.
            send (str | Unset): Console and RCON: the line to send.
            method (ProfilePlayersMethod | Unset): HTTP: default GET.
            path (str | Unset): HTTP: the path.
            parse (ProfilePlayersParse | Unset): How to read the answer: `regex` per line, or `list` in a JSON answer.
            rules_count (str | Unset): An `a2s` connection: read the count from this rule of the game's Steam rules answer
                (A2S_RULES) instead of its player list, for a game whose list stays empty with players on. The rule's value must
                be a whole number. Only the count is read: the players read lists that many players with no names.
    """

    via: str | Unset = UNSET
    send: str | Unset = UNSET
    method: ProfilePlayersMethod | Unset = UNSET
    path: str | Unset = UNSET
    parse: ProfilePlayersParse | Unset = UNSET
    rules_count: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        via = self.via

        send = self.send

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        path = self.path

        parse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parse, Unset):
            parse = self.parse.to_dict()

        rules_count = self.rules_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if via is not UNSET:
            field_dict["via"] = via
        if send is not UNSET:
            field_dict["send"] = send
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if parse is not UNSET:
            field_dict["parse"] = parse
        if rules_count is not UNSET:
            field_dict["rules_count"] = rules_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.profile_players_parse import ProfilePlayersParse

        d = dict(src_dict)
        via = d.pop("via", UNSET)

        send = d.pop("send", UNSET)

        _method = d.pop("method", UNSET)
        method: ProfilePlayersMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ProfilePlayersMethod(_method)

        path = d.pop("path", UNSET)

        _parse = d.pop("parse", UNSET)
        parse: ProfilePlayersParse | Unset
        if isinstance(_parse, Unset):
            parse = UNSET
        else:
            parse = ProfilePlayersParse.from_dict(_parse)

        rules_count = d.pop("rules_count", UNSET)

        profile_players = cls(
            via=via,
            send=send,
            method=method,
            path=path,
            parse=parse,
            rules_count=rules_count,
        )

        return profile_players

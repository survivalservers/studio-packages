from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.contact_request_create_continents_item import (
    ContactRequestCreateContinentsItem,
)
from ..models.contact_request_engine import ContactRequestEngine
from ..models.contact_request_players import ContactRequestPlayers
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactRequestCreate")


@_attrs_define
class ContactRequestCreate:
    """
    Attributes:
        name (str): The person's name.
        email (str): Where to reply.
        studio (str):
        game (str): The game's name or working title.
        engine (ContactRequestEngine): `custom`: the studio's own engine.
        expected_players (ContactRequestPlayers): Peak players at once the studio expects.
        continents (list[ContactRequestCreateContinentsItem]):
        message (str | Unset):
        source (str | Unset): The page the form was on (for example `pricing`).
        website (str | Unset): Leave empty. The form hides it from people.
    """

    name: str
    email: str
    studio: str
    game: str
    engine: ContactRequestEngine
    expected_players: ContactRequestPlayers
    continents: list[ContactRequestCreateContinentsItem]
    message: str | Unset = UNSET
    source: str | Unset = UNSET
    website: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        studio = self.studio

        game = self.game

        engine = self.engine.value

        expected_players = self.expected_players.value

        continents = []
        for continents_item_data in self.continents:
            continents_item = continents_item_data.value
            continents.append(continents_item)

        message = self.message

        source = self.source

        website = self.website

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "email": email,
                "studio": studio,
                "game": game,
                "engine": engine,
                "expected_players": expected_players,
                "continents": continents,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if source is not UNSET:
            field_dict["source"] = source
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        studio = d.pop("studio")

        game = d.pop("game")

        engine = ContactRequestEngine(d.pop("engine"))

        expected_players = ContactRequestPlayers(d.pop("expected_players"))

        continents = []
        _continents = d.pop("continents")
        for continents_item_data in _continents:
            continents_item = ContactRequestCreateContinentsItem(continents_item_data)

            continents.append(continents_item)

        message = d.pop("message", UNSET)

        source = d.pop("source", UNSET)

        website = d.pop("website", UNSET)

        contact_request_create = cls(
            name=name,
            email=email,
            studio=studio,
            game=game,
            engine=engine,
            expected_players=expected_players,
            continents=continents,
            message=message,
            source=source,
            website=website,
        )

        return contact_request_create

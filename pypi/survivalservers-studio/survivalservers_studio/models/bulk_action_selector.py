from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_action_selector_target import BulkActionSelectorTarget
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_selector_players import BulkActionSelectorPlayers
    from ..models.labels import Labels


T = TypeVar("T", bound="BulkActionSelector")


@_attrs_define
class BulkActionSelector:
    """Which persistent servers, game servers or pools a bulk action acts on. Every filter given must match. At least one
    of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or `ids`. A bulk action takes up to 2,000 targets.

        Attributes:
            target (BulkActionSelectorTarget): Persistent servers, game servers that are not persistent server runs, or
                pools (rollouts only).
            app (str | Unset): App ID or slug.
            versions (list[str] | Unset): Version names or IDs, with `app`.
            branch (str | Unset): Branch name, for example `live`.
            regions (list[str] | Unset):
            continents (list[str] | Unset):
            labels (Labels | Unset): Up to 32; keys up to 63 characters of `a-z 0-9 _ . -`; values up to 256 characters.
            players (BulkActionSelectorPlayers | Unset): Only targets with this many players on them, read when the action
                is planned. `{"max": 0}` is only empty servers.
            status (list[str] | Unset): Persistent server or game server states. Default every state; targets in a state the
                action cannot use are skipped with a reason.
            ids (list[str] | Unset): Persistent server or game server IDs.
    """

    target: BulkActionSelectorTarget
    app: str | Unset = UNSET
    versions: list[str] | Unset = UNSET
    branch: str | Unset = UNSET
    regions: list[str] | Unset = UNSET
    continents: list[str] | Unset = UNSET
    labels: Labels | Unset = UNSET
    players: BulkActionSelectorPlayers | Unset = UNSET
    status: list[str] | Unset = UNSET
    ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target.value

        app = self.app

        versions: list[str] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

        branch = self.branch

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        continents: list[str] | Unset = UNSET
        if not isinstance(self.continents, Unset):
            continents = self.continents

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        players: dict[str, Any] | Unset = UNSET
        if not isinstance(self.players, Unset):
            players = self.players.to_dict()

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
            }
        )
        if app is not UNSET:
            field_dict["app"] = app
        if versions is not UNSET:
            field_dict["versions"] = versions
        if branch is not UNSET:
            field_dict["branch"] = branch
        if regions is not UNSET:
            field_dict["regions"] = regions
        if continents is not UNSET:
            field_dict["continents"] = continents
        if labels is not UNSET:
            field_dict["labels"] = labels
        if players is not UNSET:
            field_dict["players"] = players
        if status is not UNSET:
            field_dict["status"] = status
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_selector_players import BulkActionSelectorPlayers
        from ..models.labels import Labels

        d = dict(src_dict)
        target = BulkActionSelectorTarget(d.pop("target"))

        app = d.pop("app", UNSET)

        versions = cast(list[str], d.pop("versions", UNSET))

        branch = d.pop("branch", UNSET)

        regions = cast(list[str], d.pop("regions", UNSET))

        continents = cast(list[str], d.pop("continents", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = Labels.from_dict(_labels)

        _players = d.pop("players", UNSET)
        players: BulkActionSelectorPlayers | Unset
        if isinstance(_players, Unset):
            players = UNSET
        else:
            players = BulkActionSelectorPlayers.from_dict(_players)

        status = cast(list[str], d.pop("status", UNSET))

        ids = cast(list[str], d.pop("ids", UNSET))

        bulk_action_selector = cls(
            target=target,
            app=app,
            versions=versions,
            branch=branch,
            regions=regions,
            continents=continents,
            labels=labels,
            players=players,
            status=status,
            ids=ids,
        )

        bulk_action_selector.additional_properties = d
        return bulk_action_selector

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

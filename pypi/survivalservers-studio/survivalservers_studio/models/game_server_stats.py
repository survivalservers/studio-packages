from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stats_step import StatsStep

if TYPE_CHECKING:
    from ..models.game_server_stats_bucket import GameServerStatsBucket


T = TypeVar("T", bound="GameServerStats")


@_attrs_define
class GameServerStats:
    """
    Attributes:
        from_ (datetime.datetime): The first bucket's start.
        to (datetime.datetime):
        step (StatsStep): A bucket's length.
        buckets (list[GameServerStatsBucket]):
    """

    from_: datetime.datetime
    to: datetime.datetime
    step: StatsStep
    buckets: list[GameServerStatsBucket]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        step = self.step.value

        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "step": step,
                "buckets": buckets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.game_server_stats_bucket import GameServerStatsBucket

        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        step = StatsStep(d.pop("step"))

        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = GameServerStatsBucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        game_server_stats = cls(
            from_=from_,
            to=to,
            step=step,
            buckets=buckets,
        )

        game_server_stats.additional_properties = d
        return game_server_stats

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

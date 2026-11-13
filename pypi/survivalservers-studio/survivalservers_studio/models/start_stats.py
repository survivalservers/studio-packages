from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.start_stats_row import StartStatsRow


T = TypeVar("T", bound="StartStats")


@_attrs_define
class StartStats:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        data (list[StartStatsRow]): This page of results.
    """

    from_: datetime.datetime
    to: datetime.datetime
    data: list[StartStatsRow]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.start_stats_row import StartStatsRow

        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = StartStatsRow.from_dict(data_item_data)

            data.append(data_item)

        start_stats = cls(
            from_=from_,
            to=to,
            data=data,
        )

        start_stats.additional_properties = d
        return start_stats

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

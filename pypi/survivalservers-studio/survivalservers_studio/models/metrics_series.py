from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetricsSeries")


@_attrs_define
class MetricsSeries:
    """`cpu_percent`, `memory_committed_mb`, `net_in_kbps`, `net_out_kbps`, and `tick_p99_ms` when the server reports frame
    times. Each point is `[time, value]`.

    """

    additional_properties: dict[str, list[list[datetime.datetime | float]]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = []
                for (
                    componentsschemas_metric_point_item_data
                ) in additional_property_item_data:
                    componentsschemas_metric_point_item: float | str
                    if isinstance(
                        componentsschemas_metric_point_item_data, datetime.datetime
                    ):
                        componentsschemas_metric_point_item = (
                            componentsschemas_metric_point_item_data.isoformat()
                        )
                    else:
                        componentsschemas_metric_point_item = (
                            componentsschemas_metric_point_item_data
                        )
                    additional_property_item.append(componentsschemas_metric_point_item)

                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        metrics_series = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = []
                _additional_property_item = additional_property_item_data
                for (
                    componentsschemas_metric_point_item_data
                ) in _additional_property_item:

                    def _parse_componentsschemas_metric_point_item(
                        data: object,
                    ) -> datetime.datetime | float:
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            componentsschemas_metric_point_item_type_0 = (
                                datetime.datetime.fromisoformat(data)
                            )

                            return componentsschemas_metric_point_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(datetime.datetime | float, data)

                    componentsschemas_metric_point_item = (
                        _parse_componentsschemas_metric_point_item(
                            componentsschemas_metric_point_item_data
                        )
                    )

                    additional_property_item.append(componentsschemas_metric_point_item)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        metrics_series.additional_properties = additional_properties
        return metrics_series

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[list[datetime.datetime | float]]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: list[list[datetime.datetime | float]]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

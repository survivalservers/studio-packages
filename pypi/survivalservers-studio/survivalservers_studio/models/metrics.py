from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_step import MetricStep
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_series import MetricsSeries


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    """
    Attributes:
        step (MetricStep): A point's length; every point is the average over its step, starting on a UTC step boundary.
        series (MetricsSeries): `cpu_percent`, `memory_committed_mb`, `net_in_kbps`, `net_out_kbps`, and `tick_p99_ms`
            when the server reports frame times. Each point is `[time, value]`.
        tick_budget_ms (float | Unset): One update's time at the rate the game sends with its frame times (1000 divided
            by `hz`), the latest in the period: 50 at 20 updates a second, 15.6 at 64. Compare `tick_p99_ms` with it. Absent
            when the game sends no rate.
    """

    step: MetricStep
    series: MetricsSeries
    tick_budget_ms: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step.value

        series = self.series.to_dict()

        tick_budget_ms = self.tick_budget_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "series": series,
            }
        )
        if tick_budget_ms is not UNSET:
            field_dict["tick_budget_ms"] = tick_budget_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.metrics_series import MetricsSeries

        d = dict(src_dict)
        step = MetricStep(d.pop("step"))

        series = MetricsSeries.from_dict(d.pop("series"))

        tick_budget_ms = d.pop("tick_budget_ms", UNSET)

        metrics = cls(
            step=step,
            series=series,
            tick_budget_ms=tick_budget_ms,
        )

        metrics.additional_properties = d
        return metrics

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

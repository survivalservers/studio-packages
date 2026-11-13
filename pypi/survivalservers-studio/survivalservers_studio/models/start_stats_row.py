from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_stats_row_start_mode import StartStatsRowStartMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartStatsRow")


@_attrs_define
class StartStatsRow:
    """Start times measured at our API edge (request in to address out). `failed` counts only failures on our side.

    Attributes:
        starts (int):
        failed (int):
        p50_ms (int | None): `null` when there were no starts.
        p95_ms (int | None):
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        app (str | Unset): App ID.
        start_mode (StartStatsRowStartMode | Unset):
        warm (int | Unset):
        cold (int | Unset):
    """

    starts: int
    failed: int
    p50_ms: int | None
    p95_ms: int | None
    region: str | Unset = UNSET
    app: str | Unset = UNSET
    start_mode: StartStatsRowStartMode | Unset = UNSET
    warm: int | Unset = UNSET
    cold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starts = self.starts

        failed = self.failed

        p50_ms: int | None
        p50_ms = self.p50_ms

        p95_ms: int | None
        p95_ms = self.p95_ms

        region = self.region

        app = self.app

        start_mode: str | Unset = UNSET
        if not isinstance(self.start_mode, Unset):
            start_mode = self.start_mode.value

        warm = self.warm

        cold = self.cold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starts": starts,
                "failed": failed,
                "p50_ms": p50_ms,
                "p95_ms": p95_ms,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if app is not UNSET:
            field_dict["app"] = app
        if start_mode is not UNSET:
            field_dict["start_mode"] = start_mode
        if warm is not UNSET:
            field_dict["warm"] = warm
        if cold is not UNSET:
            field_dict["cold"] = cold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        starts = d.pop("starts")

        failed = d.pop("failed")

        def _parse_p50_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        p50_ms = _parse_p50_ms(d.pop("p50_ms"))

        def _parse_p95_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        p95_ms = _parse_p95_ms(d.pop("p95_ms"))

        region = d.pop("region", UNSET)

        app = d.pop("app", UNSET)

        _start_mode = d.pop("start_mode", UNSET)
        start_mode: StartStatsRowStartMode | Unset
        if isinstance(_start_mode, Unset):
            start_mode = UNSET
        else:
            start_mode = StartStatsRowStartMode(_start_mode)

        warm = d.pop("warm", UNSET)

        cold = d.pop("cold", UNSET)

        start_stats_row = cls(
            starts=starts,
            failed=failed,
            p50_ms=p50_ms,
            p95_ms=p95_ms,
            region=region,
            app=app,
            start_mode=start_mode,
            warm=warm,
            cold=cold,
        )

        start_stats_row.additional_properties = d
        return start_stats_row

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

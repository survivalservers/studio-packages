from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os
from ..models.rate_class import RateClass
from ..models.tier import Tier
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageRecord")


@_attrs_define
class UsageRecord:
    """
    Attributes:
        id (str): Usage record ID.
        app (str): App ID.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        tier (Tier): Public hardware tier.
        os (Os):
        rate_class (RateClass): `warm` appears only if warm standby is billed. `persistent_server_paused`: a paused
            persistent server kept paused past its free minutes. `reserved_included`: usage a reservation covered, priced at
            0; the reservation's own `reserved` row is what it costs. New classes may be added (section 1.1).
        cpu (float):
        memory_gb (float):
        start (datetime.datetime):
        end (datetime.datetime | None): `null` while still open.
        seconds (float): Billed seconds, to the millisecond.
        game_server (str | Unset): Game server ID.
        persistent_server (str | Unset): Persistent server ID.
    """

    id: str
    app: str
    region: str
    tier: Tier
    os: Os
    rate_class: RateClass
    cpu: float
    memory_gb: float
    start: datetime.datetime
    end: datetime.datetime | None
    seconds: float
    game_server: str | Unset = UNSET
    persistent_server: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        app = self.app

        region = self.region

        tier = self.tier.value

        os = self.os.value

        rate_class = self.rate_class.value

        cpu = self.cpu

        memory_gb = self.memory_gb

        start = self.start.isoformat()

        end: None | str
        if isinstance(self.end, datetime.datetime):
            end = self.end.isoformat()
        else:
            end = self.end

        seconds = self.seconds

        game_server = self.game_server

        persistent_server = self.persistent_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app": app,
                "region": region,
                "tier": tier,
                "os": os,
                "rate_class": rate_class,
                "cpu": cpu,
                "memory_gb": memory_gb,
                "start": start,
                "end": end,
                "seconds": seconds,
            }
        )
        if game_server is not UNSET:
            field_dict["game_server"] = game_server
        if persistent_server is not UNSET:
            field_dict["persistent_server"] = persistent_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        app = d.pop("app")

        region = d.pop("region")

        tier = Tier(d.pop("tier"))

        os = Os(d.pop("os"))

        rate_class = RateClass(d.pop("rate_class"))

        cpu = d.pop("cpu")

        memory_gb = d.pop("memory_gb")

        start = datetime.datetime.fromisoformat(d.pop("start"))

        def _parse_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = datetime.datetime.fromisoformat(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end = _parse_end(d.pop("end"))

        seconds = d.pop("seconds")

        game_server = d.pop("game_server", UNSET)

        persistent_server = d.pop("persistent_server", UNSET)

        usage_record = cls(
            id=id,
            app=app,
            region=region,
            tier=tier,
            os=os,
            rate_class=rate_class,
            cpu=cpu,
            memory_gb=memory_gb,
            start=start,
            end=end,
            seconds=seconds,
            game_server=game_server,
            persistent_server=persistent_server,
        )

        usage_record.additional_properties = d
        return usage_record

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

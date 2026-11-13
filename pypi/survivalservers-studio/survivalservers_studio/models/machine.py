from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.machine_state import MachineState
from ..models.os import Os
from ..types import UNSET, Unset

T = TypeVar("T", bound="Machine")


@_attrs_define
class Machine:
    """
    Attributes:
        id (str): Your own machine's ID.
        name (str): Your name for it.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        os (Os):
        state (MachineState): `waiting_for_agent` until its machine agent enrolls; `active` takes your game servers;
            `maintenance` takes no new ones; `unreachable` when its agent has not been heard from (game servers there may
            still run); `removed`.
        game_servers_running (int): Game servers on it now.
        created_at (datetime.datetime):
        threads (int | None | Unset): Hardware threads its agent reported.
        usable_vcpus (int | None | Unset): vCPUs your game servers can use: its hardware threads less the machine
            agent's reserve. This is what it bills for.
        memory_mb (int | None | Unset): Memory its agent can commit to game servers.
        public_ipv4 (None | str | Unset): Its public IPv4 address, as you gave it or its agent reported it.
        public_ipv6 (None | str | Unset):
        agent_version (None | str | Unset):
        monthly_price (None | str | Unset): A full month at today's usable vCPUs and your own-machine rate; null until
            its agent reports.
        enrolled_at (datetime.datetime | None | Unset):
        last_seen_at (datetime.datetime | None | Unset): When its agent last checked in.
        removed_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    region: str
    os: Os
    state: MachineState
    game_servers_running: int
    created_at: datetime.datetime
    threads: int | None | Unset = UNSET
    usable_vcpus: int | None | Unset = UNSET
    memory_mb: int | None | Unset = UNSET
    public_ipv4: None | str | Unset = UNSET
    public_ipv6: None | str | Unset = UNSET
    agent_version: None | str | Unset = UNSET
    monthly_price: None | str | Unset = UNSET
    enrolled_at: datetime.datetime | None | Unset = UNSET
    last_seen_at: datetime.datetime | None | Unset = UNSET
    removed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        region = self.region

        os = self.os.value

        state = self.state.value

        game_servers_running = self.game_servers_running

        created_at = self.created_at.isoformat()

        threads: int | None | Unset
        if isinstance(self.threads, Unset):
            threads = UNSET
        else:
            threads = self.threads

        usable_vcpus: int | None | Unset
        if isinstance(self.usable_vcpus, Unset):
            usable_vcpus = UNSET
        else:
            usable_vcpus = self.usable_vcpus

        memory_mb: int | None | Unset
        if isinstance(self.memory_mb, Unset):
            memory_mb = UNSET
        else:
            memory_mb = self.memory_mb

        public_ipv4: None | str | Unset
        if isinstance(self.public_ipv4, Unset):
            public_ipv4 = UNSET
        else:
            public_ipv4 = self.public_ipv4

        public_ipv6: None | str | Unset
        if isinstance(self.public_ipv6, Unset):
            public_ipv6 = UNSET
        else:
            public_ipv6 = self.public_ipv6

        agent_version: None | str | Unset
        if isinstance(self.agent_version, Unset):
            agent_version = UNSET
        else:
            agent_version = self.agent_version

        monthly_price: None | str | Unset
        if isinstance(self.monthly_price, Unset):
            monthly_price = UNSET
        else:
            monthly_price = self.monthly_price

        enrolled_at: None | str | Unset
        if isinstance(self.enrolled_at, Unset):
            enrolled_at = UNSET
        elif isinstance(self.enrolled_at, datetime.datetime):
            enrolled_at = self.enrolled_at.isoformat()
        else:
            enrolled_at = self.enrolled_at

        last_seen_at: None | str | Unset
        if isinstance(self.last_seen_at, Unset):
            last_seen_at = UNSET
        elif isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        removed_at: None | str | Unset
        if isinstance(self.removed_at, Unset):
            removed_at = UNSET
        elif isinstance(self.removed_at, datetime.datetime):
            removed_at = self.removed_at.isoformat()
        else:
            removed_at = self.removed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "region": region,
                "os": os,
                "state": state,
                "game_servers_running": game_servers_running,
                "created_at": created_at,
            }
        )
        if threads is not UNSET:
            field_dict["threads"] = threads
        if usable_vcpus is not UNSET:
            field_dict["usable_vcpus"] = usable_vcpus
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if public_ipv4 is not UNSET:
            field_dict["public_ipv4"] = public_ipv4
        if public_ipv6 is not UNSET:
            field_dict["public_ipv6"] = public_ipv6
        if agent_version is not UNSET:
            field_dict["agent_version"] = agent_version
        if monthly_price is not UNSET:
            field_dict["monthly_price"] = monthly_price
        if enrolled_at is not UNSET:
            field_dict["enrolled_at"] = enrolled_at
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at
        if removed_at is not UNSET:
            field_dict["removed_at"] = removed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        region = d.pop("region")

        os = Os(d.pop("os"))

        state = MachineState(d.pop("state"))

        game_servers_running = d.pop("game_servers_running")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_threads(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        threads = _parse_threads(d.pop("threads", UNSET))

        def _parse_usable_vcpus(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        usable_vcpus = _parse_usable_vcpus(d.pop("usable_vcpus", UNSET))

        def _parse_memory_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_mb = _parse_memory_mb(d.pop("memory_mb", UNSET))

        def _parse_public_ipv4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ipv4 = _parse_public_ipv4(d.pop("public_ipv4", UNSET))

        def _parse_public_ipv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_ipv6 = _parse_public_ipv6(d.pop("public_ipv6", UNSET))

        def _parse_agent_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_version = _parse_agent_version(d.pop("agent_version", UNSET))

        def _parse_monthly_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_price = _parse_monthly_price(d.pop("monthly_price", UNSET))

        def _parse_enrolled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrolled_at_type_0 = datetime.datetime.fromisoformat(data)

                return enrolled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        enrolled_at = _parse_enrolled_at(d.pop("enrolled_at", UNSET))

        def _parse_last_seen_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at", UNSET))

        def _parse_removed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_at_type_0 = datetime.datetime.fromisoformat(data)

                return removed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        removed_at = _parse_removed_at(d.pop("removed_at", UNSET))

        machine = cls(
            id=id,
            name=name,
            region=region,
            os=os,
            state=state,
            game_servers_running=game_servers_running,
            created_at=created_at,
            threads=threads,
            usable_vcpus=usable_vcpus,
            memory_mb=memory_mb,
            public_ipv4=public_ipv4,
            public_ipv6=public_ipv6,
            agent_version=agent_version,
            monthly_price=monthly_price,
            enrolled_at=enrolled_at,
            last_seen_at=last_seen_at,
            removed_at=removed_at,
        )

        machine.additional_properties = d
        return machine

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

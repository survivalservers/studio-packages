from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_failed_start import PoolFailedStart
    from ..models.pool_hold import PoolHold
    from ..models.pool_version_state import PoolVersionState
    from ..models.pool_wait import PoolWait


T = TypeVar("T", bound="PoolState")


@_attrs_define
class PoolState:
    """
    Attributes:
        ready (int): Ready servers on the pool's own version: a start on that version takes one at once.
        starting (int): Game servers of the pool's own version started and not ready yet.
        target (int): How many ready servers the pool keeps now (its size).
        allocations_last_hour (int): Starts that took one of its ready servers in the last hour.
        versions (list[PoolVersionState]): Its waiting game servers by version, the pool's own version first, even with
            none. After the pool moves to another version, the old version's ready servers wait on, for starts that still
            name that version, until as many of the new version are ready (or while the pool is held).
        failed_starts (int): Starts on the pool's own version that failed in a row: game servers that ended on their own
            before a start took them, before their ready check (crashed, quit, not ready in time) or by failing after it
            (crashed, ran out of memory). Back to 0 once one is ready. While it is above 0 the pool starts one at a time,
            waits 5 seconds after the first failure and twice as long after each one after (up to 2 minutes), and starts at
            most 4 a minute. `pool.starts_failing` fires at 3; at 10 the pool holds (`held`).
        last_failure (None | PoolFailedStart | Unset): The newest failed start counted in `failed_starts`.
        next_start_at (datetime.datetime | None | Unset): While its starts fail and it is not held: the earliest it
            starts the next one.
        held (None | PoolHold | Unset): Set when 10 starts on its version failed in a row: it starts no more on that
            version, and keeps its other versions' ready servers. Saving the pool again (as it is or changed) or moving it
            to another version (a rollout, its branch moving) ends it.
        waiting (None | PoolWait | Unset): Set while the pool needs more ready servers and cannot start one, with why:
            no machine in the region has room for its size for your studio now (`no_capacity`), no machine there sells its
            tier on its system (`not_offered`), or its version is still copying there (`version_not_ready`). It clears once
            one starts, once it needs none, or when the pool is saved again.
    """

    ready: int
    starting: int
    target: int
    allocations_last_hour: int
    versions: list[PoolVersionState]
    failed_starts: int
    last_failure: None | PoolFailedStart | Unset = UNSET
    next_start_at: datetime.datetime | None | Unset = UNSET
    held: None | PoolHold | Unset = UNSET
    waiting: None | PoolWait | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pool_failed_start import PoolFailedStart
        from ..models.pool_hold import PoolHold
        from ..models.pool_wait import PoolWait

        ready = self.ready

        starting = self.starting

        target = self.target

        allocations_last_hour = self.allocations_last_hour

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        failed_starts = self.failed_starts

        last_failure: dict[str, Any] | None | Unset
        if isinstance(self.last_failure, Unset):
            last_failure = UNSET
        elif isinstance(self.last_failure, PoolFailedStart):
            last_failure = self.last_failure.to_dict()
        else:
            last_failure = self.last_failure

        next_start_at: None | str | Unset
        if isinstance(self.next_start_at, Unset):
            next_start_at = UNSET
        elif isinstance(self.next_start_at, datetime.datetime):
            next_start_at = self.next_start_at.isoformat()
        else:
            next_start_at = self.next_start_at

        held: dict[str, Any] | None | Unset
        if isinstance(self.held, Unset):
            held = UNSET
        elif isinstance(self.held, PoolHold):
            held = self.held.to_dict()
        else:
            held = self.held

        waiting: dict[str, Any] | None | Unset
        if isinstance(self.waiting, Unset):
            waiting = UNSET
        elif isinstance(self.waiting, PoolWait):
            waiting = self.waiting.to_dict()
        else:
            waiting = self.waiting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ready": ready,
                "starting": starting,
                "target": target,
                "allocations_last_hour": allocations_last_hour,
                "versions": versions,
                "failed_starts": failed_starts,
            }
        )
        if last_failure is not UNSET:
            field_dict["last_failure"] = last_failure
        if next_start_at is not UNSET:
            field_dict["next_start_at"] = next_start_at
        if held is not UNSET:
            field_dict["held"] = held
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pool_failed_start import PoolFailedStart
        from ..models.pool_hold import PoolHold
        from ..models.pool_version_state import PoolVersionState
        from ..models.pool_wait import PoolWait

        d = dict(src_dict)
        ready = d.pop("ready")

        starting = d.pop("starting")

        target = d.pop("target")

        allocations_last_hour = d.pop("allocations_last_hour")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = PoolVersionState.from_dict(versions_item_data)

            versions.append(versions_item)

        failed_starts = d.pop("failed_starts")

        def _parse_last_failure(data: object) -> None | PoolFailedStart | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_failure_type_0 = PoolFailedStart.from_dict(data)

                return last_failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PoolFailedStart | Unset, data)

        last_failure = _parse_last_failure(d.pop("last_failure", UNSET))

        def _parse_next_start_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_start_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_start_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_start_at = _parse_next_start_at(d.pop("next_start_at", UNSET))

        def _parse_held(data: object) -> None | PoolHold | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                held_type_0 = PoolHold.from_dict(data)

                return held_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PoolHold | Unset, data)

        held = _parse_held(d.pop("held", UNSET))

        def _parse_waiting(data: object) -> None | PoolWait | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                waiting_type_0 = PoolWait.from_dict(data)

                return waiting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PoolWait | Unset, data)

        waiting = _parse_waiting(d.pop("waiting", UNSET))

        pool_state = cls(
            ready=ready,
            starting=starting,
            target=target,
            allocations_last_hour=allocations_last_hour,
            versions=versions,
            failed_starts=failed_starts,
            last_failure=last_failure,
            next_start_at=next_start_at,
            held=held,
            waiting=waiting,
        )

        pool_state.additional_properties = d
        return pool_state

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

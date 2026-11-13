from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pool_mode import PoolMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_state import PoolState
    from ..models.size import Size


T = TypeVar("T", bound="Pool")


@_attrs_define
class Pool:
    """
    Attributes:
        app (str): App ID.
        region (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older
            region ID is still accepted, and answers carry the new one.
        version (str): Version name, unique in its app, for example `2.3.1`.
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        mode (PoolMode):
        min_ (int):
        status (PoolState):
        branch (None | str | Unset):
        max_ (int | None | Unset):
        created_at (datetime.datetime | Unset): When it was made.
        updated_at (datetime.datetime | Unset): When it last changed.
    """

    app: str
    region: str
    version: str
    size: Size
    mode: PoolMode
    min_: int
    status: PoolState
    branch: None | str | Unset = UNSET
    max_: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        region = self.region

        version = self.version

        size = self.size.to_dict()

        mode = self.mode.value

        min_ = self.min_

        status = self.status.to_dict()

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "region": region,
                "version": version,
                "size": size,
                "mode": mode,
                "min": min_,
                "status": status,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if max_ is not UNSET:
            field_dict["max"] = max_
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pool_state import PoolState
        from ..models.size import Size

        d = dict(src_dict)
        app = d.pop("app")

        region = d.pop("region")

        version = d.pop("version")

        size = Size.from_dict(d.pop("size"))

        mode = PoolMode(d.pop("mode"))

        min_ = d.pop("min")

        status = PoolState.from_dict(d.pop("status"))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        pool = cls(
            app=app,
            region=region,
            version=version,
            size=size,
            mode=mode,
            min_=min_,
            status=status,
            branch=branch,
            max_=max_,
            created_at=created_at,
            updated_at=updated_at,
        )

        pool.additional_properties = d
        return pool

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

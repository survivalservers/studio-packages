from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pool_put_mode import PoolPutMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.size import Size


T = TypeVar("T", bound="PoolPut")


@_attrs_define
class PoolPut:
    """
    Attributes:
        size (Size): One vCPU is one hardware thread. `standard` from 0.25 in 0.25 steps; `high-frequency` whole vCPUs.
            Memory 0.5 GB to 4 GB per vCPU.
        mode (PoolPutMode):
        min_ (int):
        version (str | Unset): Version name or ID. Give this or `branch`.
        branch (str | Unset): Branch name, for example `live`.
        max_ (int | Unset):
    """

    size: Size
    mode: PoolPutMode
    min_: int
    version: str | Unset = UNSET
    branch: str | Unset = UNSET
    max_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size.to_dict()

        mode = self.mode.value

        min_ = self.min_

        version = self.version

        branch = self.branch

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
                "mode": mode,
                "min": min_,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.size import Size

        d = dict(src_dict)
        size = Size.from_dict(d.pop("size"))

        mode = PoolPutMode(d.pop("mode"))

        min_ = d.pop("min")

        version = d.pop("version", UNSET)

        branch = d.pop("branch", UNSET)

        max_ = d.pop("max", UNSET)

        pool_put = cls(
            size=size,
            mode=mode,
            min_=min_,
            version=version,
            branch=branch,
            max_=max_,
        )

        pool_put.additional_properties = d
        return pool_put

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

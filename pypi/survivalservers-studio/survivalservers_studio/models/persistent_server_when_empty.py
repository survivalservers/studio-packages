from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.persistent_server_when_empty_then import PersistentServerWhenEmptyThen
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersistentServerWhenEmpty")


@_attrs_define
class PersistentServerWhenEmpty:
    """Pause when nobody plays and resume on the first player's packet or connection, which is answered. A paused
    persistent server keeps its machine, address and ports. Scheduled restarts are skipped while it is paused; a new
    version or a restart asked for while it is paused is applied at once, since nobody is on it.

        Attributes:
            enabled (bool | Unset): `false` turns it off. Default: True.
            after (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
            then (PersistentServerWhenEmptyThen | Unset): `pause` resumes in well under a second and keeps its memory;
                `stop` takes a backup and stops, so resuming is a fresh start. Default: PersistentServerWhenEmptyThen.PAUSE.
            stop_after (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
    """

    enabled: bool | Unset = True
    after: int | str | Unset = UNSET
    then: PersistentServerWhenEmptyThen | Unset = PersistentServerWhenEmptyThen.PAUSE
    stop_after: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        after: int | str | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        then: str | Unset = UNSET
        if not isinstance(self.then, Unset):
            then = self.then.value

        stop_after: int | str | Unset
        if isinstance(self.stop_after, Unset):
            stop_after = UNSET
        else:
            stop_after = self.stop_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if after is not UNSET:
            field_dict["after"] = after
        if then is not UNSET:
            field_dict["then"] = then
        if stop_after is not UNSET:
            field_dict["stop_after"] = stop_after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_after(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        after = _parse_after(d.pop("after", UNSET))

        _then = d.pop("then", UNSET)
        then: PersistentServerWhenEmptyThen | Unset
        if isinstance(_then, Unset):
            then = UNSET
        else:
            then = PersistentServerWhenEmptyThen(_then)

        def _parse_stop_after(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        stop_after = _parse_stop_after(d.pop("stop_after", UNSET))

        persistent_server_when_empty = cls(
            enabled=enabled,
            after=after,
            then=then,
            stop_after=stop_after,
        )

        persistent_server_when_empty.additional_properties = d
        return persistent_server_when_empty

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

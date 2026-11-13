from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CrashDump")


@_attrs_define
class CrashDump:
    """
    Attributes:
        id (str): Collected file ID.
        name (str): The dump's file name, as the machine named it.
        run (int | None): The run of the game server that crashed and left it (1 for its first); `null` when not known.
        bytes_ (int): Its size as the game left it.
        created_at (datetime.datetime): When it was stored.
        expires_at (datetime.datetime): When it is deleted.
    """

    id: str
    name: str
    run: int | None
    bytes_: int
    created_at: datetime.datetime
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        run: int | None
        run = self.run

        bytes_ = self.bytes_

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "run": run,
                "bytes": bytes_,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_run(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        run = _parse_run(d.pop("run"))

        bytes_ = d.pop("bytes")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        crash_dump = cls(
            id=id,
            name=name,
            run=run,
            bytes_=bytes_,
            created_at=created_at,
            expires_at=expires_at,
        )

        crash_dump.additional_properties = d
        return crash_dump

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditDetails")


@_attrs_define
class AuditDetails:
    """What the entry was about, where it was recorded.

    Attributes:
        app (str | Unset): The app's slug or ID, as the entry recorded it.
        version (str | Unset): The version's name.
        region (str | Unset): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An
            older region ID is still accepted, and answers carry the new one.
        file (str | Unset): The build's file name.
        count (int | Unset): How many game servers a stop of many (`game_servers.stop`) asked to stop.
    """

    app: str | Unset = UNSET
    version: str | Unset = UNSET
    region: str | Unset = UNSET
    file: str | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        version = self.version

        region = self.region

        file = self.file

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if version is not UNSET:
            field_dict["version"] = version
        if region is not UNSET:
            field_dict["region"] = region
        if file is not UNSET:
            field_dict["file"] = file
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        app = d.pop("app", UNSET)

        version = d.pop("version", UNSET)

        region = d.pop("region", UNSET)

        file = d.pop("file", UNSET)

        count = d.pop("count", UNSET)

        audit_details = cls(
            app=app,
            version=version,
            region=region,
            file=file,
            count=count,
        )

        audit_details.additional_properties = d
        return audit_details

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

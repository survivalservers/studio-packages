from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_selector import BulkActionSelector


T = TypeVar("T", bound="BulkActionExportCreate")


@_attrs_define
class BulkActionExportCreate:
    """
    Attributes:
        selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
            filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
            `ids`. A bulk action takes up to 2,000 targets.
        at (datetime.datetime | Unset): Each server's newest backup from before this moment. Default its newest.
        note (str | Unset):
        dry_run (bool | Unset):
    """

    selector: BulkActionSelector
    at: datetime.datetime | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector.to_dict()

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        note = self.note

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
            }
        )
        if at is not UNSET:
            field_dict["at"] = at
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_selector import BulkActionSelector

        d = dict(src_dict)
        selector = BulkActionSelector.from_dict(d.pop("selector"))

        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        bulk_action_export_create = cls(
            selector=selector,
            at=at,
            note=note,
            dry_run=dry_run,
        )

        bulk_action_export_create.additional_properties = d
        return bulk_action_export_create

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

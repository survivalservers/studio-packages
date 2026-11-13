from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_card_status import StatusCardStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_card_preview import StatusCardPreview


T = TypeVar("T", bound="StatusCard")


@_attrs_define
class StatusCard:
    """
    Attributes:
        id (str): Status card ID.
        url (str): Masked. The URL is the secret.
        app (str): App ID.
        branch (str):
        regions (list[str]):
        persistent_servers (list[str]):
        status (StatusCardStatus): A card Discord says is gone or closed to us is disabled at once.
        created_at (datetime.datetime): When it was made.
        disabled_reason (None | str | Unset):
        preview (StatusCardPreview | Unset): The exact Discord message body the card sends.
    """

    id: str
    url: str
    app: str
    branch: str
    regions: list[str]
    persistent_servers: list[str]
    status: StatusCardStatus
    created_at: datetime.datetime
    disabled_reason: None | str | Unset = UNSET
    preview: StatusCardPreview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        app = self.app

        branch = self.branch

        regions = self.regions

        persistent_servers = self.persistent_servers

        status = self.status.value

        created_at = self.created_at.isoformat()

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        else:
            disabled_reason = self.disabled_reason

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "app": app,
                "branch": branch,
                "regions": regions,
                "persistent_servers": persistent_servers,
                "status": status,
                "created_at": created_at,
            }
        )
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_card_preview import StatusCardPreview

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        app = d.pop("app")

        branch = d.pop("branch")

        regions = cast(list[str], d.pop("regions"))

        persistent_servers = cast(list[str], d.pop("persistent_servers"))

        status = StatusCardStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_disabled_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason", UNSET))

        _preview = d.pop("preview", UNSET)
        preview: StatusCardPreview | Unset
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = StatusCardPreview.from_dict(_preview)

        status_card = cls(
            id=id,
            url=url,
            app=app,
            branch=branch,
            regions=regions,
            persistent_servers=persistent_servers,
            status=status,
            created_at=created_at,
            disabled_reason=disabled_reason,
            preview=preview,
        )

        status_card.additional_properties = d
        return status_card

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

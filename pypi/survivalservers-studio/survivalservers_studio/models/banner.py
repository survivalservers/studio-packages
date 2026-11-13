from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Banner")


@_attrs_define
class Banner:
    """The wide picture across the top of the app's page, made by us from the uploaded one: JPEG at two sizes, 4:1, with no
    metadata. Each address is a signed URL that works until `expires_at` (12 to 24 hours away), as an icon's; a new
    upload gives new addresses.

        Attributes:
            url_800 (str): 800 by 200 pixels.
            url_1600 (str): 1600 by 400 pixels.
            expires_at (datetime.datetime): When these addresses stop working.
            updated_at (datetime.datetime): When it was uploaded.
    """

    url_800: str
    url_1600: str
    expires_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_800 = self.url_800

        url_1600 = self.url_1600

        expires_at = self.expires_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url_800": url_800,
                "url_1600": url_1600,
                "expires_at": expires_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url_800 = d.pop("url_800")

        url_1600 = d.pop("url_1600")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        banner = cls(
            url_800=url_800,
            url_1600=url_1600,
            expires_at=expires_at,
            updated_at=updated_at,
        )

        banner.additional_properties = d
        return banner

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

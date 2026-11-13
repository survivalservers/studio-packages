from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Icon")


@_attrs_define
class Icon:
    """The square picture shown beside the name, made by us from the uploaded one: WebP at three sizes with no metadata.
    Each address is a signed URL that works until `expires_at` (12 to 24 hours away), so show it straight from the
    answer and read the studio or app again for a fresh one; never store it. A new upload gives new addresses.

        Attributes:
            url_64 (str): 64 by 64 pixels.
            url_128 (str): 128 by 128 pixels.
            url_256 (str): 256 by 256 pixels.
            expires_at (datetime.datetime): When these addresses stop working.
            updated_at (datetime.datetime): When it was uploaded.
    """

    url_64: str
    url_128: str
    url_256: str
    expires_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_64 = self.url_64

        url_128 = self.url_128

        url_256 = self.url_256

        expires_at = self.expires_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url_64": url_64,
                "url_128": url_128,
                "url_256": url_256,
                "expires_at": expires_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url_64 = d.pop("url_64")

        url_128 = d.pop("url_128")

        url_256 = d.pop("url_256")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        icon = cls(
            url_64=url_64,
            url_128=url_128,
            url_256=url_256,
            expires_at=expires_at,
            updated_at=updated_at,
        )

        icon.additional_properties = d
        return icon

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

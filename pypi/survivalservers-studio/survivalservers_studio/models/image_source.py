from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_source_type import ImageSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageSource")


@_attrs_define
class ImageSource:
    """An OCI image in any registry (Linux). We copy it into ours, pinned by digest.

    Attributes:
        type_ (ImageSourceType):
        image (str):
        registry_credential (str | Unset): Registry login ID.
    """

    type_: ImageSourceType
    image: str
    registry_credential: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        image = self.image

        registry_credential = self.registry_credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "image": image,
            }
        )
        if registry_credential is not UNSET:
            field_dict["registry_credential"] = registry_credential

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = ImageSourceType(d.pop("type"))

        image = d.pop("image")

        registry_credential = d.pop("registry_credential", UNSET)

        image_source = cls(
            type_=type_,
            image=image,
            registry_credential=registry_credential,
        )

        image_source.additional_properties = d
        return image_source

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

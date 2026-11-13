from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.os import Os

if TYPE_CHECKING:
    from ..models.image_source import ImageSource
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="BuildCreate")


@_attrs_define
class BuildCreate:
    """
    Attributes:
        os (Os):
        source (ImageSource | UploadSource):
    """

    os: Os
    source: ImageSource | UploadSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        os = self.os.value

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "os": os,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.image_source import ImageSource
        from ..models.upload_source import UploadSource

        d = dict(src_dict)
        os = Os(d.pop("os"))

        def _parse_source(data: object) -> ImageSource | UploadSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_source_type_0 = UploadSource.from_dict(data)

                return componentsschemas_build_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_build_source_type_1 = ImageSource.from_dict(data)

            return componentsschemas_build_source_type_1

        source = _parse_source(d.pop("source"))

        build_create = cls(
            os=os,
            source=source,
        )

        build_create.additional_properties = d
        return build_create

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

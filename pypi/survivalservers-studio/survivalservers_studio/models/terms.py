from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.terms_document import TermsDocument


T = TypeVar("T", bound="Terms")


@_attrs_define
class Terms:
    """The version of the terms in effect and the pages it is made of.

    Attributes:
        version (None | str): The version in effect; `null` while the terms are not in force (no box to tick).
        effective_at (datetime.datetime | None): When it took effect.
        documents (list[TermsDocument]): The Terms of Service, the documents they name and the Privacy Notice, in the
            order the box lists them; empty while none is in effect.
    """

    version: None | str
    effective_at: datetime.datetime | None
    documents: list[TermsDocument]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version: None | str
        version = self.version

        effective_at: None | str
        if isinstance(self.effective_at, datetime.datetime):
            effective_at = self.effective_at.isoformat()
        else:
            effective_at = self.effective_at

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "effective_at": effective_at,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.terms_document import TermsDocument

        d = dict(src_dict)

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        def _parse_effective_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_at_type_0 = datetime.datetime.fromisoformat(data)

                return effective_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        effective_at = _parse_effective_at(d.pop("effective_at"))

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = TermsDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        terms = cls(
            version=version,
            effective_at=effective_at,
            documents=documents,
        )

        terms.additional_properties = d
        return terms

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

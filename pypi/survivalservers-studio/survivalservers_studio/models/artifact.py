from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artifact_kind import ArtifactKind

T = TypeVar("T", bound="Artifact")


@_attrs_define
class Artifact:
    """
    Attributes:
        id (str): Collected file ID.
        kind (ArtifactKind): `log` or `file`. This call never returns `crash_dump`: a crash dump is listed only by `GET
            /v0/game-servers/{id}/crash-dumps`, for owners and admins with the crash-dump permission. The value stays in the
            list so older clients still read it.
        path (str):
        bytes_ (int):
        download_url (str): Valid 15 minutes.
        expires_at (datetime.datetime): When it expires.
    """

    id: str
    kind: ArtifactKind
    path: str
    bytes_: int
    download_url: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        path = self.path

        bytes_ = self.bytes_

        download_url = self.download_url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "path": path,
                "bytes": bytes_,
                "download_url": download_url,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = ArtifactKind(d.pop("kind"))

        path = d.pop("path")

        bytes_ = d.pop("bytes")

        download_url = d.pop("download_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        artifact = cls(
            id=id,
            kind=kind,
            path=path,
            bytes_=bytes_,
            download_url=download_url,
            expires_at=expires_at,
        )

        artifact.additional_properties = d
        return artifact

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

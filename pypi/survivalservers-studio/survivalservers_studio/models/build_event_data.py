from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.build_status import BuildStatus
from ..models.event_object_meta_object import EventObjectMetaObject
from ..models.os import Os
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_failure import BuildFailure
    from ..models.build_upload import BuildUpload
    from ..models.image_source import ImageSource
    from ..models.scan_result import ScanResult
    from ..models.upload_source import UploadSource


T = TypeVar("T", bound="BuildEventData")


@_attrs_define
class BuildEventData:
    """
    Attributes:
        object_ (EventObjectMetaObject):
        sequence (int): Per object; ignore a lower number arriving after a higher one.
        id (str): Build ID.
        app (str): App ID.
        os (Os):
        status (BuildStatus): A ready Linux build turns `failed` with `image_not_found` if its image is no longer in our
            registry (machines could not fetch it); `build.failed` fires then.
        source (ImageSource | UploadSource):
        created_at (datetime.datetime): When it was made.
        bytes_ (int | Unset):
        unpacked_bytes (int | Unset):
        files (int | Unset):
        sha256 (str | Unset):
        image_digest (str | Unset):
        scan (ScanResult | Unset):
        executables (list[str] | Unset): Programs found in the zip, for `launch.executable`.
        failure (BuildFailure | Unset):
        upload (BuildUpload | Unset): Present while `awaiting_upload`, for a caller with `builds:write` (never in
            events); every read returns fresh URLs.
        ready_at (datetime.datetime | None | Unset): When it became ready.
    """

    object_: EventObjectMetaObject
    sequence: int
    id: str
    app: str
    os: Os
    status: BuildStatus
    source: ImageSource | UploadSource
    created_at: datetime.datetime
    bytes_: int | Unset = UNSET
    unpacked_bytes: int | Unset = UNSET
    files: int | Unset = UNSET
    sha256: str | Unset = UNSET
    image_digest: str | Unset = UNSET
    scan: ScanResult | Unset = UNSET
    executables: list[str] | Unset = UNSET
    failure: BuildFailure | Unset = UNSET
    upload: BuildUpload | Unset = UNSET
    ready_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_source import UploadSource

        object_ = self.object_.value

        sequence = self.sequence

        id = self.id

        app = self.app

        os = self.os.value

        status = self.status.value

        source: dict[str, Any]
        if isinstance(self.source, UploadSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        created_at = self.created_at.isoformat()

        bytes_ = self.bytes_

        unpacked_bytes = self.unpacked_bytes

        files = self.files

        sha256 = self.sha256

        image_digest = self.image_digest

        scan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scan, Unset):
            scan = self.scan.to_dict()

        executables: list[str] | Unset = UNSET
        if not isinstance(self.executables, Unset):
            executables = self.executables

        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        upload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upload, Unset):
            upload = self.upload.to_dict()

        ready_at: None | str | Unset
        if isinstance(self.ready_at, Unset):
            ready_at = UNSET
        elif isinstance(self.ready_at, datetime.datetime):
            ready_at = self.ready_at.isoformat()
        else:
            ready_at = self.ready_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "sequence": sequence,
                "id": id,
                "app": app,
                "os": os,
                "status": status,
                "source": source,
                "created_at": created_at,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if unpacked_bytes is not UNSET:
            field_dict["unpacked_bytes"] = unpacked_bytes
        if files is not UNSET:
            field_dict["files"] = files
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if image_digest is not UNSET:
            field_dict["image_digest"] = image_digest
        if scan is not UNSET:
            field_dict["scan"] = scan
        if executables is not UNSET:
            field_dict["executables"] = executables
        if failure is not UNSET:
            field_dict["failure"] = failure
        if upload is not UNSET:
            field_dict["upload"] = upload
        if ready_at is not UNSET:
            field_dict["ready_at"] = ready_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.build_failure import BuildFailure
        from ..models.build_upload import BuildUpload
        from ..models.image_source import ImageSource
        from ..models.scan_result import ScanResult
        from ..models.upload_source import UploadSource

        d = dict(src_dict)
        object_ = EventObjectMetaObject(d.pop("object"))

        sequence = d.pop("sequence")

        id = d.pop("id")

        app = d.pop("app")

        os = Os(d.pop("os"))

        status = BuildStatus(d.pop("status"))

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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        bytes_ = d.pop("bytes", UNSET)

        unpacked_bytes = d.pop("unpacked_bytes", UNSET)

        files = d.pop("files", UNSET)

        sha256 = d.pop("sha256", UNSET)

        image_digest = d.pop("image_digest", UNSET)

        _scan = d.pop("scan", UNSET)
        scan: ScanResult | Unset
        if isinstance(_scan, Unset):
            scan = UNSET
        else:
            scan = ScanResult.from_dict(_scan)

        executables = cast(list[str], d.pop("executables", UNSET))

        _failure = d.pop("failure", UNSET)
        failure: BuildFailure | Unset
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = BuildFailure.from_dict(_failure)

        _upload = d.pop("upload", UNSET)
        upload: BuildUpload | Unset
        if isinstance(_upload, Unset):
            upload = UNSET
        else:
            upload = BuildUpload.from_dict(_upload)

        def _parse_ready_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ready_at_type_0 = datetime.datetime.fromisoformat(data)

                return ready_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ready_at = _parse_ready_at(d.pop("ready_at", UNSET))

        build_event_data = cls(
            object_=object_,
            sequence=sequence,
            id=id,
            app=app,
            os=os,
            status=status,
            source=source,
            created_at=created_at,
            bytes_=bytes_,
            unpacked_bytes=unpacked_bytes,
            files=files,
            sha256=sha256,
            image_digest=image_digest,
            scan=scan,
            executables=executables,
            failure=failure,
            upload=upload,
            ready_at=ready_at,
        )

        build_event_data.additional_properties = d
        return build_event_data

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

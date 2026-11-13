from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code import ErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_error import FieldError
    from ..models.region_tried import RegionTried


T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """RFC 9457 problem details with a stable `code`.

    Attributes:
        type_ (str):
        title (str):
        status (int):
        code (ErrorCode):
        request_id (str): Request ID; quote it to [support](https://studio.survivalservers.com/docs/help/get-help/).
        detail (str | Unset):
        errors (list[FieldError] | Unset): Field errors, for `validation_failed`, and the fields a call does not take,
            for `bad_request`.
        regions_tried (list[RegionTried] | Unset): For `capacity_unavailable`.
        identity_provider (str | Unset): For `sso_required`, the sign-in to go through (the panel sends it to Keycloak
            as `kc_idp_hint`, so an earlier password does not get in the way).
    """

    type_: str
    title: str
    status: int
    code: ErrorCode
    request_id: str
    detail: str | Unset = UNSET
    errors: list[FieldError] | Unset = UNSET
    regions_tried: list[RegionTried] | Unset = UNSET
    identity_provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        code = self.code.value

        request_id = self.request_id

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        regions_tried: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regions_tried, Unset):
            regions_tried = []
            for regions_tried_item_data in self.regions_tried:
                regions_tried_item = regions_tried_item_data.to_dict()
                regions_tried.append(regions_tried_item)

        identity_provider = self.identity_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "code": code,
                "request_id": request_id,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if regions_tried is not UNSET:
            field_dict["regions_tried"] = regions_tried
        if identity_provider is not UNSET:
            field_dict["identity_provider"] = identity_provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.field_error import FieldError
        from ..models.region_tried import RegionTried

        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        code = ErrorCode(d.pop("code"))

        request_id = d.pop("request_id")

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[FieldError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = FieldError.from_dict(errors_item_data)

                errors.append(errors_item)

        _regions_tried = d.pop("regions_tried", UNSET)
        regions_tried: list[RegionTried] | Unset = UNSET
        if _regions_tried is not UNSET:
            regions_tried = []
            for regions_tried_item_data in _regions_tried:
                regions_tried_item = RegionTried.from_dict(regions_tried_item_data)

                regions_tried.append(regions_tried_item)

        identity_provider = d.pop("identity_provider", UNSET)

        problem = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            request_id=request_id,
            detail=detail,
            errors=errors,
            regions_tried=regions_tried,
            identity_provider=identity_provider,
        )

        problem.additional_properties = d
        return problem

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

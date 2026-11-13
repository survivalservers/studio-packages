from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invitation_status import InvitationStatus
from ..models.role import Role
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inviter import Inviter


T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (str): Invitation ID.
        email (str):
        role (Role):
        status (InvitationStatus):
        created_at (datetime.datetime): When it was made.
        expires_at (datetime.datetime): When it expires.
        invited_by (Inviter | None | Unset): The member who sent it; `null` when an API key did.
        accept_url (None | str | Unset): The one-time link that accepts this invitation. Only in the answer that made
            it, and only while invitations are not emailed (`null` when an email carries it): give it to the person
            yourself. It works once, for the invited email, until `expires_at`, and is never shown again.
    """

    id: str
    email: str
    role: Role
    status: InvitationStatus
    created_at: datetime.datetime
    expires_at: datetime.datetime
    invited_by: Inviter | None | Unset = UNSET
    accept_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inviter import Inviter

        id = self.id

        email = self.email

        role = self.role.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        invited_by: dict[str, Any] | None | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        elif isinstance(self.invited_by, Inviter):
            invited_by = self.invited_by.to_dict()
        else:
            invited_by = self.invited_by

        accept_url: None | str | Unset
        if isinstance(self.accept_url, Unset):
            accept_url = UNSET
        else:
            accept_url = self.accept_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "role": role,
                "status": status,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if accept_url is not UNSET:
            field_dict["accept_url"] = accept_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inviter import Inviter

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        role = Role(d.pop("role"))

        status = InvitationStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        def _parse_invited_by(data: object) -> Inviter | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invited_by_type_0 = Inviter.from_dict(data)

                return invited_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Inviter | None | Unset, data)

        invited_by = _parse_invited_by(d.pop("invited_by", UNSET))

        def _parse_accept_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accept_url = _parse_accept_url(d.pop("accept_url", UNSET))

        invitation = cls(
            id=id,
            email=email,
            role=role,
            status=status,
            created_at=created_at,
            expires_at=expires_at,
            invited_by=invited_by,
            accept_url=accept_url,
        )

        invitation.additional_properties = d
        return invitation

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

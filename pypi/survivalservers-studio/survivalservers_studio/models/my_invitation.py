from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role import Role
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inviter import Inviter


T = TypeVar("T", bound="MyInvitation")


@_attrs_define
class MyInvitation:
    """An invitation waiting for the signed-in person, from a studio they are not in yet.

    Attributes:
        id (str): Invitation ID.
        studio_name (str): The inviting studio's name.
        role (Role):
        created_at (datetime.datetime): When it was sent.
        expires_at (datetime.datetime): When it expires.
        invited_by (Inviter | None | Unset): The member who sent it; `null` when an API key did.
    """

    id: str
    studio_name: str
    role: Role
    created_at: datetime.datetime
    expires_at: datetime.datetime
    invited_by: Inviter | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inviter import Inviter

        id = self.id

        studio_name = self.studio_name

        role = self.role.value

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        invited_by: dict[str, Any] | None | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        elif isinstance(self.invited_by, Inviter):
            invited_by = self.invited_by.to_dict()
        else:
            invited_by = self.invited_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "studio_name": studio_name,
                "role": role,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inviter import Inviter

        d = dict(src_dict)
        id = d.pop("id")

        studio_name = d.pop("studio_name")

        role = Role(d.pop("role"))

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

        my_invitation = cls(
            id=id,
            studio_name=studio_name,
            role=role,
            created_at=created_at,
            expires_at=expires_at,
            invited_by=invited_by,
        )

        my_invitation.additional_properties = d
        return my_invitation

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.me_terms import MeTerms
    from ..models.me_user import MeUser
    from ..models.membership import Membership
    from ..models.my_invitation import MyInvitation


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        user (MeUser):
        studios (list[Membership]): Every studio this person belongs to. Send the chosen one's ID in the `Studio`
            header.
        invitations (list[MyInvitation] | Unset): Invitations waiting for this person's email address, newest first, one
            per studio, from studios they are not in yet (none that were used, canceled or are past their time). Join one
            with `POST /v0/me/invitations/{invitation}/accept`.
        terms (MeTerms | Unset):
    """

    user: MeUser
    studios: list[Membership]
    invitations: list[MyInvitation] | Unset = UNSET
    terms: MeTerms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        studios = []
        for studios_item_data in self.studios:
            studios_item = studios_item_data.to_dict()
            studios.append(studios_item)

        invitations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invitations, Unset):
            invitations = []
            for invitations_item_data in self.invitations:
                invitations_item = invitations_item_data.to_dict()
                invitations.append(invitations_item)

        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "studios": studios,
            }
        )
        if invitations is not UNSET:
            field_dict["invitations"] = invitations
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.me_terms import MeTerms
        from ..models.me_user import MeUser
        from ..models.membership import Membership
        from ..models.my_invitation import MyInvitation

        d = dict(src_dict)
        user = MeUser.from_dict(d.pop("user"))

        studios = []
        _studios = d.pop("studios")
        for studios_item_data in _studios:
            studios_item = Membership.from_dict(studios_item_data)

            studios.append(studios_item)

        _invitations = d.pop("invitations", UNSET)
        invitations: list[MyInvitation] | Unset = UNSET
        if _invitations is not UNSET:
            invitations = []
            for invitations_item_data in _invitations:
                invitations_item = MyInvitation.from_dict(invitations_item_data)

                invitations.append(invitations_item)

        _terms = d.pop("terms", UNSET)
        terms: MeTerms | Unset
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = MeTerms.from_dict(_terms)

        me = cls(
            user=user,
            studios=studios,
            invitations=invitations,
            terms=terms,
        )

        me.additional_properties = d
        return me

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restart_policy_policy import RestartPolicyPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestartPolicy")


@_attrs_define
class RestartPolicy:
    """What happens when the game server exits on its own.

    Attributes:
        policy (RestartPolicyPolicy | Unset): `on_failure` relaunches in place after a crash (same ID and address).
            Default: RestartPolicyPolicy.NEVER.
        max_ (int | Unset): At most this many restarts. Without it, a game server restarts after each crash until its
            third crash within 10 minutes, which ends it failed.
    """

    policy: RestartPolicyPolicy | Unset = RestartPolicyPolicy.NEVER
    max_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: str | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: RestartPolicyPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = RestartPolicyPolicy(_policy)

        max_ = d.pop("max", UNSET)

        restart_policy = cls(
            policy=policy,
            max_=max_,
        )

        restart_policy.additional_properties = d
        return restart_policy

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

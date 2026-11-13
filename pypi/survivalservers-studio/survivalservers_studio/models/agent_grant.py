from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_grant_ends_in_days import AgentGrantEndsInDays
from ..models.agent_permission import AgentPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentGrant")


@_attrs_define
class AgentGrant:
    """
    Attributes:
        ends_in_days (AgentGrantEndsInDays): When it is disconnected on its own.
        apps (list[str] | Unset): Limit the agent to these apps (IDs or slugs); empty or absent for every app.
        permissions (list[AgentPermission] | Unset): What it may do; empty for view only.
        time_limit (int | None | str | Unset): Game servers and persistent servers it starts stop after this long (1
            minute to 7 days). `null` for no limit.
        spend_cap (None | str | Unset): The most it may spend in a calendar month (UTC), counted from what it starts at
            your prices before free hours. At the cap it can't start more until the 1st. `null` for no cap. With `start`,
            `persistent_servers` or `bulk_actions` and no `spend_cap` sent, the cap is $50.
    """

    ends_in_days: AgentGrantEndsInDays
    apps: list[str] | Unset = UNSET
    permissions: list[AgentPermission] | Unset = UNSET
    time_limit: int | None | str | Unset = UNSET
    spend_cap: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ends_in_days = self.ends_in_days.value

        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        time_limit: int | None | str | Unset
        if isinstance(self.time_limit, Unset):
            time_limit = UNSET
        else:
            time_limit = self.time_limit

        spend_cap: None | str | Unset
        if isinstance(self.spend_cap, Unset):
            spend_cap = UNSET
        else:
            spend_cap = self.spend_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ends_in_days": ends_in_days,
            }
        )
        if apps is not UNSET:
            field_dict["apps"] = apps
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if time_limit is not UNSET:
            field_dict["time_limit"] = time_limit
        if spend_cap is not UNSET:
            field_dict["spend_cap"] = spend_cap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ends_in_days = AgentGrantEndsInDays(d.pop("ends_in_days"))

        apps = cast(list[str], d.pop("apps", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: list[AgentPermission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = AgentPermission(permissions_item_data)

                permissions.append(permissions_item)

        def _parse_time_limit(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        time_limit = _parse_time_limit(d.pop("time_limit", UNSET))

        def _parse_spend_cap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spend_cap = _parse_spend_cap(d.pop("spend_cap", UNSET))

        agent_grant = cls(
            ends_in_days=ends_in_days,
            apps=apps,
            permissions=permissions,
            time_limit=time_limit,
            spend_cap=spend_cap,
        )

        agent_grant.additional_properties = d
        return agent_grant

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

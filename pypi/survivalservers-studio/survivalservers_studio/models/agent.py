from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_kind import AgentKind
from ..models.agent_permission import AgentPermission
from ..models.scope import Scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inviter import Inviter


T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """
    Attributes:
        id (str): AI agent ID.
        kind (AgentKind): `signed_in`: a tool a member connected with the MCP sign-in, which is not available yet.
            `agent_key`: an agent key.
        name (str): The tool's name as it calls itself, or the agent key's name.
        connected_by (Inviter):
        permissions (list[AgentPermission]): Empty for view only.
        scopes (list[Scope]):
        apps (list[str]): Empty for every app.
        time_limit (None | str): How long game servers and persistent servers it starts run at most, such as `2h`;
            `null` for none.
        spend_cap (None | str): The monthly spending cap in USD as a decimal string; `null` for no cap.
        spent_this_month (str): USD as a decimal string.
        expires_at (datetime.datetime): When it is disconnected on its own.
        created_at (datetime.datetime):
        last_used_at (datetime.datetime | None):
        redirect_host (None | str | Unset): Where its sign-in went back to (`localhost` for a tool on the member's
            computer).
        key_prefix (None | str | Unset): An agent key's non-secret start.
    """

    id: str
    kind: AgentKind
    name: str
    connected_by: Inviter
    permissions: list[AgentPermission]
    scopes: list[Scope]
    apps: list[str]
    time_limit: None | str
    spend_cap: None | str
    spent_this_month: str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    last_used_at: datetime.datetime | None
    redirect_host: None | str | Unset = UNSET
    key_prefix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        name = self.name

        connected_by = self.connected_by.to_dict()

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        apps = self.apps

        time_limit: None | str
        time_limit = self.time_limit

        spend_cap: None | str
        spend_cap = self.spend_cap

        spent_this_month = self.spent_this_month

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        redirect_host: None | str | Unset
        if isinstance(self.redirect_host, Unset):
            redirect_host = UNSET
        else:
            redirect_host = self.redirect_host

        key_prefix: None | str | Unset
        if isinstance(self.key_prefix, Unset):
            key_prefix = UNSET
        else:
            key_prefix = self.key_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "name": name,
                "connected_by": connected_by,
                "permissions": permissions,
                "scopes": scopes,
                "apps": apps,
                "time_limit": time_limit,
                "spend_cap": spend_cap,
                "spent_this_month": spent_this_month,
                "expires_at": expires_at,
                "created_at": created_at,
                "last_used_at": last_used_at,
            }
        )
        if redirect_host is not UNSET:
            field_dict["redirect_host"] = redirect_host
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inviter import Inviter

        d = dict(src_dict)
        id = d.pop("id")

        kind = AgentKind(d.pop("kind"))

        name = d.pop("name")

        connected_by = Inviter.from_dict(d.pop("connected_by"))

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = AgentPermission(permissions_item_data)

            permissions.append(permissions_item)

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = Scope(scopes_item_data)

            scopes.append(scopes_item)

        apps = cast(list[str], d.pop("apps"))

        def _parse_time_limit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        time_limit = _parse_time_limit(d.pop("time_limit"))

        def _parse_spend_cap(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        spend_cap = _parse_spend_cap(d.pop("spend_cap"))

        spent_this_month = d.pop("spent_this_month")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_redirect_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_host = _parse_redirect_host(d.pop("redirect_host", UNSET))

        def _parse_key_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_prefix = _parse_key_prefix(d.pop("key_prefix", UNSET))

        agent = cls(
            id=id,
            kind=kind,
            name=name,
            connected_by=connected_by,
            permissions=permissions,
            scopes=scopes,
            apps=apps,
            time_limit=time_limit,
            spend_cap=spend_cap,
            spent_this_month=spent_this_month,
            expires_at=expires_at,
            created_at=created_at,
            last_used_at=last_used_at,
            redirect_host=redirect_host,
            key_prefix=key_prefix,
        )

        agent.additional_properties = d
        return agent

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

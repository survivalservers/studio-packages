from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_actor import AuditActor
    from ..models.audit_details import AuditDetails
    from ..models.audit_person import AuditPerson


T = TypeVar("T", bound="AuditEntry")


@_attrs_define
class AuditEntry:
    """
    Attributes:
        id (str): Audit entry ID.
        actor (AuditActor):
        action (str):
        at (datetime.datetime):
        target (None | str | Unset): The object ID acted on.
        target_name (None | str | Unset): What people call the target today: an app's, persistent server's, key's or
            settings set's name, "<app> <version>" for a version, a build's file or image, a member's name or email, a game
            server's name as the panel lists it, a bulk action by what it did ("Restart · Brinewatch Server (Linux) · 121
            game servers"). Deleted targets keep their names (see `target_deleted`); `null` when nothing names it any more.
        target_deleted (bool | Unset): `true` when the target has since been deleted (a key or AI agent: revoked).
        request_id (str | Unset): Request ID; quote it to [support](https://studio.survivalservers.com/docs/help/get-
            help/).
        ip (None | str | Unset): Absent when a key limited to some apps reads the line.
        by_ai (bool | Unset): `true` when an AI agent did it (`actor.type` is `agent`).
        on_behalf_of (AuditPerson | Unset): A key limited to some apps reads the person by `user` alone.
        details (AuditDetails | Unset): What the entry was about, where it was recorded.
    """

    id: str
    actor: AuditActor
    action: str
    at: datetime.datetime
    target: None | str | Unset = UNSET
    target_name: None | str | Unset = UNSET
    target_deleted: bool | Unset = UNSET
    request_id: str | Unset = UNSET
    ip: None | str | Unset = UNSET
    by_ai: bool | Unset = UNSET
    on_behalf_of: AuditPerson | Unset = UNSET
    details: AuditDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        actor = self.actor.to_dict()

        action = self.action

        at = self.at.isoformat()

        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        target_name: None | str | Unset
        if isinstance(self.target_name, Unset):
            target_name = UNSET
        else:
            target_name = self.target_name

        target_deleted = self.target_deleted

        request_id = self.request_id

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        by_ai = self.by_ai

        on_behalf_of: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_behalf_of, Unset):
            on_behalf_of = self.on_behalf_of.to_dict()

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "actor": actor,
                "action": action,
                "at": at,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if target_name is not UNSET:
            field_dict["target_name"] = target_name
        if target_deleted is not UNSET:
            field_dict["target_deleted"] = target_deleted
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if by_ai is not UNSET:
            field_dict["by_ai"] = by_ai
        if on_behalf_of is not UNSET:
            field_dict["on_behalf_of"] = on_behalf_of
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_actor import AuditActor
        from ..models.audit_details import AuditDetails
        from ..models.audit_person import AuditPerson

        d = dict(src_dict)
        id = d.pop("id")

        actor = AuditActor.from_dict(d.pop("actor"))

        action = d.pop("action")

        at = datetime.datetime.fromisoformat(d.pop("at"))

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))

        def _parse_target_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_name = _parse_target_name(d.pop("target_name", UNSET))

        target_deleted = d.pop("target_deleted", UNSET)

        request_id = d.pop("request_id", UNSET)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        by_ai = d.pop("by_ai", UNSET)

        _on_behalf_of = d.pop("on_behalf_of", UNSET)
        on_behalf_of: AuditPerson | Unset
        if isinstance(_on_behalf_of, Unset):
            on_behalf_of = UNSET
        else:
            on_behalf_of = AuditPerson.from_dict(_on_behalf_of)

        _details = d.pop("details", UNSET)
        details: AuditDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = AuditDetails.from_dict(_details)

        audit_entry = cls(
            id=id,
            actor=actor,
            action=action,
            at=at,
            target=target,
            target_name=target_name,
            target_deleted=target_deleted,
            request_id=request_id,
            ip=ip,
            by_ai=by_ai,
            on_behalf_of=on_behalf_of,
            details=details,
        )

        audit_entry.additional_properties = d
        return audit_entry

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

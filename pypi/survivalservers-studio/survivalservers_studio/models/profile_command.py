from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.profile_command_method import ProfileCommandMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_command_arg import ProfileCommandArg


T = TypeVar("T", bound="ProfileCommand")


@_attrs_define
class ProfileCommand:
    """
    Attributes:
        id (str): Unique in the profile.
        label (str):
        description (str | Unset): One line on what it does.
        via (str | Unset): A connection's name. Default `console`.
        send (str | Unset): Console and RCON: the line to send, with `{{name}}` for each argument.
        method (ProfileCommandMethod | Unset): HTTP: default POST.
        path (str | Unset): HTTP: the path, with `{{name}}` for each argument (URL-escaped).
        body (str | Unset): HTTP: the body, with `{{name}}` for each argument (escaped for JSON).
        args (list[ProfileCommandArg] | Unset):
        confirm (bool | Unset): The panel asks before sending it. For anything that throws a player out or loses data.
    """

    id: str
    label: str
    description: str | Unset = UNSET
    via: str | Unset = UNSET
    send: str | Unset = UNSET
    method: ProfileCommandMethod | Unset = UNSET
    path: str | Unset = UNSET
    body: str | Unset = UNSET
    args: list[ProfileCommandArg] | Unset = UNSET
    confirm: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        description = self.description

        via = self.via

        send = self.send

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        path = self.path

        body = self.body

        args: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = []
            for args_item_data in self.args:
                args_item = args_item_data.to_dict()
                args.append(args_item)

        confirm = self.confirm

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if via is not UNSET:
            field_dict["via"] = via
        if send is not UNSET:
            field_dict["send"] = send
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if body is not UNSET:
            field_dict["body"] = body
        if args is not UNSET:
            field_dict["args"] = args
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.profile_command_arg import ProfileCommandArg

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        description = d.pop("description", UNSET)

        via = d.pop("via", UNSET)

        send = d.pop("send", UNSET)

        _method = d.pop("method", UNSET)
        method: ProfileCommandMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ProfileCommandMethod(_method)

        path = d.pop("path", UNSET)

        body = d.pop("body", UNSET)

        _args = d.pop("args", UNSET)
        args: list[ProfileCommandArg] | Unset = UNSET
        if _args is not UNSET:
            args = []
            for args_item_data in _args:
                args_item = ProfileCommandArg.from_dict(args_item_data)

                args.append(args_item)

        confirm = d.pop("confirm", UNSET)

        profile_command = cls(
            id=id,
            label=label,
            description=description,
            via=via,
            send=send,
            method=method,
            path=path,
            body=body,
            args=args,
            confirm=confirm,
        )

        return profile_command

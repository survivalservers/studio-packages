from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_command_arg_type import ProfileCommandArgType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileCommandArg")


@_attrs_define
class ProfileCommandArg:
    """A value a command takes. `{{name}}` in the command is replaced with it.

    Attributes:
        name (str):
        label (str | Unset): What the panel calls it. Default its name.
        type_ (ProfileCommandArgType | Unset): Default `text`. `player` is a player's name or ID, a `number` is checked
            as one, and `choice` takes one of `choices`.
        choices (list[str] | Unset): With `choice`, the values allowed.
        optional (bool | Unset): It may be left out; `{{name}}` then becomes empty.
    """

    name: str
    label: str | Unset = UNSET
    type_: ProfileCommandArgType | Unset = UNSET
    choices: list[str] | Unset = UNSET
    optional: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        choices: list[str] | Unset = UNSET
        if not isinstance(self.choices, Unset):
            choices = self.choices

        optional = self.optional

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if choices is not UNSET:
            field_dict["choices"] = choices
        if optional is not UNSET:
            field_dict["optional"] = optional

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ProfileCommandArgType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProfileCommandArgType(_type_)

        choices = cast(list[str], d.pop("choices", UNSET))

        optional = d.pop("optional", UNSET)

        profile_command_arg = cls(
            name=name,
            label=label,
            type_=type_,
            choices=choices,
            optional=optional,
        )

        return profile_command_arg

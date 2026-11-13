from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_args import CommandArgs


T = TypeVar("T", bound="BulkActionSavedCommand")


@_attrs_define
class BulkActionSavedCommand:
    """The saved command a bulk action runs. `command` beside it is what the first target was sent.

    Attributes:
        id (str): The command's `id` in the game profile.
        label (str | Unset): The command's label on the first target's version.
        args (CommandArgs | Unset): The saved command's arguments, by name. Values are strings, numbers included.
    """

    id: str
    label: str | Unset = UNSET
    args: CommandArgs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.command_args import CommandArgs

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label", UNSET)

        _args = d.pop("args", UNSET)
        args: CommandArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = CommandArgs.from_dict(_args)

        bulk_action_saved_command = cls(
            id=id,
            label=label,
            args=args,
        )

        bulk_action_saved_command.additional_properties = d
        return bulk_action_saved_command

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_action_rollout import BulkActionRollout
    from ..models.bulk_action_selector import BulkActionSelector
    from ..models.command_args import CommandArgs
    from ..models.game_command_console import GameCommandConsole
    from ..models.game_command_http import GameCommandHttp
    from ..models.game_command_isle_rcon import GameCommandIsleRcon
    from ..models.game_command_rcon import GameCommandRcon


T = TypeVar("T", bound="BulkActionCommandCreate")


@_attrs_define
class BulkActionCommandCreate:
    """Give one of `command`, a saved command's `command_id` with its `args`, or a `line` sent through a connection
    (`via`). A saved command or a connection is read from each target's own version, so targets on different versions
    can run it differently. Targets whose version has no such command or connection are skipped (`no_command`).

        Attributes:
            selector (BulkActionSelector): Which persistent servers, game servers or pools a bulk action acts on. Every
                filter given must match. At least one of `app`, `versions`, `branch`, `regions`, `continents`, `labels` or
                `ids`. A bulk action takes up to 2,000 targets.
            command (GameCommandConsole | GameCommandHttp | GameCommandIsleRcon | GameCommandRcon | Unset): A command for
                the game server itself.
            command_id (str | Unset): A saved command in the targets' game profile.
            args (CommandArgs | Unset): The saved command's arguments, by name. Values are strings, numbers included.
            line (str | Unset): A line to send as it is, through `via`.
            via (str | Unset): With `line`, a connection in the targets' game profile. Default `console`.
            capture (int | str | Unset): A string with a unit (`ms`, `s`, `m`, `h`, `d`), or an integer read as seconds.
            rollout (BulkActionRollout | Unset): How targets are taken in batches. Give `batch_size` or `batch_percent`, not
                both.
            note (str | Unset): Shown with the bulk action and in the audit log.
            dry_run (bool | Unset): Answer with the plan and send nothing. Default: False.
    """

    selector: BulkActionSelector
    command: (
        GameCommandConsole
        | GameCommandHttp
        | GameCommandIsleRcon
        | GameCommandRcon
        | Unset
    ) = UNSET
    command_id: str | Unset = UNSET
    args: CommandArgs | Unset = UNSET
    line: str | Unset = UNSET
    via: str | Unset = UNSET
    capture: int | str | Unset = UNSET
    rollout: BulkActionRollout | Unset = UNSET
    note: str | Unset = UNSET
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_rcon import GameCommandRcon

        selector = self.selector.to_dict()

        command: dict[str, Any] | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        elif (
            isinstance(self.command, GameCommandConsole)
            or isinstance(self.command, GameCommandRcon)
            or isinstance(self.command, GameCommandHttp)
        ):
            command = self.command.to_dict()
        else:
            command = self.command.to_dict()

        command_id = self.command_id

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        line = self.line

        via = self.via

        capture: int | str | Unset
        if isinstance(self.capture, Unset):
            capture = UNSET
        else:
            capture = self.capture

        rollout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.to_dict()

        note = self.note

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if command_id is not UNSET:
            field_dict["command_id"] = command_id
        if args is not UNSET:
            field_dict["args"] = args
        if line is not UNSET:
            field_dict["line"] = line
        if via is not UNSET:
            field_dict["via"] = via
        if capture is not UNSET:
            field_dict["capture"] = capture
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if note is not UNSET:
            field_dict["note"] = note
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulk_action_rollout import BulkActionRollout
        from ..models.bulk_action_selector import BulkActionSelector
        from ..models.command_args import CommandArgs
        from ..models.game_command_console import GameCommandConsole
        from ..models.game_command_http import GameCommandHttp
        from ..models.game_command_isle_rcon import GameCommandIsleRcon
        from ..models.game_command_rcon import GameCommandRcon

        d = dict(src_dict)
        selector = BulkActionSelector.from_dict(d.pop("selector"))

        def _parse_command(
            data: object,
        ) -> (
            GameCommandConsole
            | GameCommandHttp
            | GameCommandIsleRcon
            | GameCommandRcon
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_0 = GameCommandConsole.from_dict(
                    data
                )

                return componentsschemas_game_command_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_1 = GameCommandRcon.from_dict(data)

                return componentsschemas_game_command_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_game_command_type_2 = GameCommandHttp.from_dict(data)

                return componentsschemas_game_command_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_game_command_type_3 = GameCommandIsleRcon.from_dict(data)

            return componentsschemas_game_command_type_3

        command = _parse_command(d.pop("command", UNSET))

        command_id = d.pop("command_id", UNSET)

        _args = d.pop("args", UNSET)
        args: CommandArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = CommandArgs.from_dict(_args)

        line = d.pop("line", UNSET)

        via = d.pop("via", UNSET)

        def _parse_capture(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        capture = _parse_capture(d.pop("capture", UNSET))

        _rollout = d.pop("rollout", UNSET)
        rollout: BulkActionRollout | Unset
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = BulkActionRollout.from_dict(_rollout)

        note = d.pop("note", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        bulk_action_command_create = cls(
            selector=selector,
            command=command,
            command_id=command_id,
            args=args,
            line=line,
            via=via,
            capture=capture,
            rollout=rollout,
            note=note,
            dry_run=dry_run,
        )

        bulk_action_command_create.additional_properties = d
        return bulk_action_command_create

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileSettingLive")


@_attrs_define
class ProfileSettingLive:
    """How to change it in the running game, with no restart. It is still written for the next run.

    Attributes:
        send (str): What to send, with `{{value}}`.
        via (str | Unset): A connection's name. Default `console`.
    """

    send: str
    via: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        send = self.send

        via = self.via

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "send": send,
            }
        )
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        send = d.pop("send")

        via = d.pop("via", UNSET)

        profile_setting_live = cls(
            send=send,
            via=via,
        )

        return profile_setting_live

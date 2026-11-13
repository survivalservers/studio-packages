from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_setting_type import ProfileSettingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_setting_live import ProfileSettingLive
    from ..models.profile_setting_place import ProfileSettingPlace


T = TypeVar("T", bound="ProfileSetting")


@_attrs_define
class ProfileSetting:
    """
    Attributes:
        id (str): Unique in the profile. Values use it.
        label (str):
        type_ (ProfileSettingType):
        at (ProfileSettingPlace): Where a setting lives: `env`, `arg`, or `file` with `key`.
        help_ (str | Unset): One or two lines on what it does.
        section (str | Unset): The group it shows under.
        popular (bool | Unset): Shown first.
        default (Any | Unset): The game's own default, shown in the form. It is not written: a setting nobody set stays
            as the game has it.
        min_ (float | Unset):
        max_ (float | Unset):
        step (float | Unset):
        unit (str | Unset):
        choices (list[str] | Unset): With `choice`, the values allowed.
        true_text (str | Unset): A `bool` as the game writes true. Default `true`.
        false_text (str | Unset): A `bool` as the game writes false. Default `false`.
        quote (bool | Unset): Written in double quotes, as a text value in toml or an Unreal struct needs.
        live (ProfileSettingLive | Unset): How to change it in the running game, with no restart. It is still written
            for the next run.
    """

    id: str
    label: str
    type_: ProfileSettingType
    at: ProfileSettingPlace
    help_: str | Unset = UNSET
    section: str | Unset = UNSET
    popular: bool | Unset = UNSET
    default: Any | Unset = UNSET
    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    step: float | Unset = UNSET
    unit: str | Unset = UNSET
    choices: list[str] | Unset = UNSET
    true_text: str | Unset = UNSET
    false_text: str | Unset = UNSET
    quote: bool | Unset = UNSET
    live: ProfileSettingLive | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        type_ = self.type_.value

        at = self.at.to_dict()

        help_ = self.help_

        section = self.section

        popular = self.popular

        default = self.default

        min_ = self.min_

        max_ = self.max_

        step = self.step

        unit = self.unit

        choices: list[str] | Unset = UNSET
        if not isinstance(self.choices, Unset):
            choices = self.choices

        true_text = self.true_text

        false_text = self.false_text

        quote = self.quote

        live: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live, Unset):
            live = self.live.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "label": label,
                "type": type_,
                "at": at,
            }
        )
        if help_ is not UNSET:
            field_dict["help"] = help_
        if section is not UNSET:
            field_dict["section"] = section
        if popular is not UNSET:
            field_dict["popular"] = popular
        if default is not UNSET:
            field_dict["default"] = default
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if step is not UNSET:
            field_dict["step"] = step
        if unit is not UNSET:
            field_dict["unit"] = unit
        if choices is not UNSET:
            field_dict["choices"] = choices
        if true_text is not UNSET:
            field_dict["true_text"] = true_text
        if false_text is not UNSET:
            field_dict["false_text"] = false_text
        if quote is not UNSET:
            field_dict["quote"] = quote
        if live is not UNSET:
            field_dict["live"] = live

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.profile_setting_live import ProfileSettingLive
        from ..models.profile_setting_place import ProfileSettingPlace

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        type_ = ProfileSettingType(d.pop("type"))

        at = ProfileSettingPlace.from_dict(d.pop("at"))

        help_ = d.pop("help", UNSET)

        section = d.pop("section", UNSET)

        popular = d.pop("popular", UNSET)

        default = d.pop("default", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        step = d.pop("step", UNSET)

        unit = d.pop("unit", UNSET)

        choices = cast(list[str], d.pop("choices", UNSET))

        true_text = d.pop("true_text", UNSET)

        false_text = d.pop("false_text", UNSET)

        quote = d.pop("quote", UNSET)

        _live = d.pop("live", UNSET)
        live: ProfileSettingLive | Unset
        if isinstance(_live, Unset):
            live = UNSET
        else:
            live = ProfileSettingLive.from_dict(_live)

        profile_setting = cls(
            id=id,
            label=label,
            type_=type_,
            at=at,
            help_=help_,
            section=section,
            popular=popular,
            default=default,
            min_=min_,
            max_=max_,
            step=step,
            unit=unit,
            choices=choices,
            true_text=true_text,
            false_text=false_text,
            quote=quote,
            live=live,
        )

        return profile_setting

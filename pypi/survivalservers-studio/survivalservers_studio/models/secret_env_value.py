from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretEnvValue")


@_attrs_define
class SecretEnvValue:
    """
    Attributes:
        value (str):
        secret (bool | Unset):  Default: False.
        generate_value (bool | Unset): Read back as true (with `value` `***`) for a value made for each game server: see
            GeneratedEnvValue.
    """

    value: str
    secret: bool | Unset = False
    generate_value: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        secret = self.secret

        generate_value = self.generate_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret
        if generate_value is not UNSET:
            field_dict["generate_value"] = generate_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        secret = d.pop("secret", UNSET)

        generate_value = d.pop("generate_value", UNSET)

        secret_env_value = cls(
            value=value,
            secret=secret,
            generate_value=generate_value,
        )

        return secret_env_value

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GeneratedEnvValue")


@_attrs_define
class GeneratedEnvValue:
    """A version's `launch.env` only: we make a new random value for each game server as it starts, 32 letters and digits,
    and give it to that game server alone (a persistent server gets a new one at every run). For an RCON or admin
    password every game server then has its own: put it where the game reads it with `{{env.<NAME>}}`. It is never
    stored or shown, and reads back as `{"value": "***", "secret": true, "generate_value": true}`.

        Attributes:
            secret (bool):
            generate_value (bool):
    """

    secret: bool
    generate_value: bool

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        generate_value = self.generate_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "secret": secret,
                "generate_value": generate_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        secret = d.pop("secret")

        generate_value = d.pop("generate_value")

        generated_env_value = cls(
            secret=secret,
            generate_value=generate_value,
        )

        return generated_env_value

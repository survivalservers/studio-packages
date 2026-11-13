from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.secret_env_value import SecretEnvValue


T = TypeVar("T", bound="Env")


@_attrs_define
class Env:
    """Environment variables. Names starting with `GS_` are reserved (`422`)."""

    additional_properties: dict[str, SecretEnvValue | str] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.secret_env_value import SecretEnvValue

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SecretEnvValue):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.secret_env_value import SecretEnvValue

        d = dict(src_dict)
        env = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> SecretEnvValue | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_env_value_type_1 = SecretEnvValue.from_dict(data)

                    return componentsschemas_env_value_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(SecretEnvValue | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        env.additional_properties = additional_properties
        return env

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SecretEnvValue | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SecretEnvValue | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

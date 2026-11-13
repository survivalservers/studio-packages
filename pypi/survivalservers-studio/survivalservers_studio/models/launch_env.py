from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.generated_env_value import GeneratedEnvValue
    from ..models.secret_env_value import SecretEnvValue


T = TypeVar("T", bound="LaunchEnv")


@_attrs_define
class LaunchEnv:
    """Environment variables for every game server of the version. Names starting with `GS_` are reserved (`422`). A value
    can also be made new for each game server (GeneratedEnvValue).

    """

    additional_properties: dict[str, GeneratedEnvValue | SecretEnvValue | str] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.generated_env_value import GeneratedEnvValue
        from ..models.secret_env_value import SecretEnvValue

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SecretEnvValue) or isinstance(prop, GeneratedEnvValue):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.generated_env_value import GeneratedEnvValue
        from ..models.secret_env_value import SecretEnvValue

        d = dict(src_dict)
        launch_env = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> GeneratedEnvValue | SecretEnvValue | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_launch_env_value_type_1 = (
                        SecretEnvValue.from_dict(data)
                    )

                    return componentsschemas_launch_env_value_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_launch_env_value_type_2 = (
                        GeneratedEnvValue.from_dict(data)
                    )

                    return componentsschemas_launch_env_value_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(GeneratedEnvValue | SecretEnvValue | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        launch_env.additional_properties = additional_properties
        return launch_env

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GeneratedEnvValue | SecretEnvValue | str:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GeneratedEnvValue | SecretEnvValue | str
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

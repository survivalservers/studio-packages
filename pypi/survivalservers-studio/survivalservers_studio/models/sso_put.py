from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sso_put_protocol import SsoPutProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="SsoPut")


@_attrs_define
class SsoPut:
    """
    Attributes:
        enabled (bool):
        protocol (SsoPutProtocol | Unset):
        domains (list[str] | Unset):
        oidc_issuer (str | Unset):
        oidc_client_id (str | Unset):
        oidc_client_secret (str | Unset):
        saml_metadata_url (str | Unset):
        emergency_owner (str | Unset): Person ID.
    """

    enabled: bool
    protocol: SsoPutProtocol | Unset = UNSET
    domains: list[str] | Unset = UNSET
    oidc_issuer: str | Unset = UNSET
    oidc_client_id: str | Unset = UNSET
    oidc_client_secret: str | Unset = UNSET
    saml_metadata_url: str | Unset = UNSET
    emergency_owner: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        domains: list[str] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        oidc_issuer = self.oidc_issuer

        oidc_client_id = self.oidc_client_id

        oidc_client_secret = self.oidc_client_secret

        saml_metadata_url = self.saml_metadata_url

        emergency_owner = self.emergency_owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if domains is not UNSET:
            field_dict["domains"] = domains
        if oidc_issuer is not UNSET:
            field_dict["oidc_issuer"] = oidc_issuer
        if oidc_client_id is not UNSET:
            field_dict["oidc_client_id"] = oidc_client_id
        if oidc_client_secret is not UNSET:
            field_dict["oidc_client_secret"] = oidc_client_secret
        if saml_metadata_url is not UNSET:
            field_dict["saml_metadata_url"] = saml_metadata_url
        if emergency_owner is not UNSET:
            field_dict["emergency_owner"] = emergency_owner

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        _protocol = d.pop("protocol", UNSET)
        protocol: SsoPutProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = SsoPutProtocol(_protocol)

        domains = cast(list[str], d.pop("domains", UNSET))

        oidc_issuer = d.pop("oidc_issuer", UNSET)

        oidc_client_id = d.pop("oidc_client_id", UNSET)

        oidc_client_secret = d.pop("oidc_client_secret", UNSET)

        saml_metadata_url = d.pop("saml_metadata_url", UNSET)

        emergency_owner = d.pop("emergency_owner", UNSET)

        sso_put = cls(
            enabled=enabled,
            protocol=protocol,
            domains=domains,
            oidc_issuer=oidc_issuer,
            oidc_client_id=oidc_client_id,
            oidc_client_secret=oidc_client_secret,
            saml_metadata_url=saml_metadata_url,
            emergency_owner=emergency_owner,
        )

        sso_put.additional_properties = d
        return sso_put

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

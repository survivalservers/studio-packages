from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sso_protocol_type_1 import SsoProtocolType1
from ..models.sso_protocol_type_2_type_1 import SsoProtocolType2Type1
from ..models.sso_protocol_type_3_type_1 import SsoProtocolType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sso_domain_record import SsoDomainRecord
    from ..models.sso_emergency_owner_type_0 import SsoEmergencyOwnerType0
    from ..models.sso_moving import SsoMoving


T = TypeVar("T", bound="Sso")


@_attrs_define
class Sso:
    """
    Attributes:
        enabled (bool):
        active (bool | Unset): Whether people are sent to your provider now: on, with at least one domain proven.
        protocol (None | SsoProtocolType1 | SsoProtocolType2Type1 | SsoProtocolType3Type1 | Unset):
        domains (list[str] | Unset):
        domain_records (list[SsoDomainRecord] | Unset): The DNS TXT record that proves each domain is yours. A domain
            counts once its record is found.
        oidc_issuer (None | str | Unset):
        oidc_client_id (None | str | Unset):
        saml_metadata_url (None | str | Unset):
        redirect_uri (None | str | Unset): Register this at your provider: the OIDC redirect URI, or the SAML assertion
            consumer service.
        saml_sp_metadata_url (None | str | Unset): For SAML: our side's metadata, for your provider to import.
        identity_provider (None | str | Unset): The provider's name in our sign-in, once one is saved: the panel signs
            in through it with this as the provider hint (the test before switching on).
        signed_in_through_provider (bool | Unset): Whether the sign-in reading this came through the provider: the test
            that switching on needs.
        emergency_owner (None | SsoEmergencyOwnerType0 | Unset): The owner who keeps a password and a one-time code
            while single sign-on is on, as the way in if the provider fails.
        moving (SsoMoving | Unset): Accounts with an email in a proven domain that still have a password, other than the
            emergency owner. Switching on moves them to your provider (they lose the password); while on, this stays at
            zero.
    """

    enabled: bool
    active: bool | Unset = UNSET
    protocol: (
        None | SsoProtocolType1 | SsoProtocolType2Type1 | SsoProtocolType3Type1 | Unset
    ) = UNSET
    domains: list[str] | Unset = UNSET
    domain_records: list[SsoDomainRecord] | Unset = UNSET
    oidc_issuer: None | str | Unset = UNSET
    oidc_client_id: None | str | Unset = UNSET
    saml_metadata_url: None | str | Unset = UNSET
    redirect_uri: None | str | Unset = UNSET
    saml_sp_metadata_url: None | str | Unset = UNSET
    identity_provider: None | str | Unset = UNSET
    signed_in_through_provider: bool | Unset = UNSET
    emergency_owner: None | SsoEmergencyOwnerType0 | Unset = UNSET
    moving: SsoMoving | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sso_emergency_owner_type_0 import SsoEmergencyOwnerType0

        enabled = self.enabled

        active = self.active

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        elif (
            isinstance(self.protocol, SsoProtocolType1)
            or isinstance(self.protocol, SsoProtocolType2Type1)
            or isinstance(self.protocol, SsoProtocolType3Type1)
        ):
            protocol = self.protocol.value
        else:
            protocol = self.protocol

        domains: list[str] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        domain_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domain_records, Unset):
            domain_records = []
            for domain_records_item_data in self.domain_records:
                domain_records_item = domain_records_item_data.to_dict()
                domain_records.append(domain_records_item)

        oidc_issuer: None | str | Unset
        if isinstance(self.oidc_issuer, Unset):
            oidc_issuer = UNSET
        else:
            oidc_issuer = self.oidc_issuer

        oidc_client_id: None | str | Unset
        if isinstance(self.oidc_client_id, Unset):
            oidc_client_id = UNSET
        else:
            oidc_client_id = self.oidc_client_id

        saml_metadata_url: None | str | Unset
        if isinstance(self.saml_metadata_url, Unset):
            saml_metadata_url = UNSET
        else:
            saml_metadata_url = self.saml_metadata_url

        redirect_uri: None | str | Unset
        if isinstance(self.redirect_uri, Unset):
            redirect_uri = UNSET
        else:
            redirect_uri = self.redirect_uri

        saml_sp_metadata_url: None | str | Unset
        if isinstance(self.saml_sp_metadata_url, Unset):
            saml_sp_metadata_url = UNSET
        else:
            saml_sp_metadata_url = self.saml_sp_metadata_url

        identity_provider: None | str | Unset
        if isinstance(self.identity_provider, Unset):
            identity_provider = UNSET
        else:
            identity_provider = self.identity_provider

        signed_in_through_provider = self.signed_in_through_provider

        emergency_owner: dict[str, Any] | None | Unset
        if isinstance(self.emergency_owner, Unset):
            emergency_owner = UNSET
        elif isinstance(self.emergency_owner, SsoEmergencyOwnerType0):
            emergency_owner = self.emergency_owner.to_dict()
        else:
            emergency_owner = self.emergency_owner

        moving: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moving, Unset):
            moving = self.moving.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if domains is not UNSET:
            field_dict["domains"] = domains
        if domain_records is not UNSET:
            field_dict["domain_records"] = domain_records
        if oidc_issuer is not UNSET:
            field_dict["oidc_issuer"] = oidc_issuer
        if oidc_client_id is not UNSET:
            field_dict["oidc_client_id"] = oidc_client_id
        if saml_metadata_url is not UNSET:
            field_dict["saml_metadata_url"] = saml_metadata_url
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if saml_sp_metadata_url is not UNSET:
            field_dict["saml_sp_metadata_url"] = saml_sp_metadata_url
        if identity_provider is not UNSET:
            field_dict["identity_provider"] = identity_provider
        if signed_in_through_provider is not UNSET:
            field_dict["signed_in_through_provider"] = signed_in_through_provider
        if emergency_owner is not UNSET:
            field_dict["emergency_owner"] = emergency_owner
        if moving is not UNSET:
            field_dict["moving"] = moving

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sso_domain_record import SsoDomainRecord
        from ..models.sso_emergency_owner_type_0 import SsoEmergencyOwnerType0
        from ..models.sso_moving import SsoMoving

        d = dict(src_dict)
        enabled = d.pop("enabled")

        active = d.pop("active", UNSET)

        def _parse_protocol(
            data: object,
        ) -> (
            None
            | SsoProtocolType1
            | SsoProtocolType2Type1
            | SsoProtocolType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_1 = SsoProtocolType1(data)

                return protocol_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_2_type_1 = SsoProtocolType2Type1(data)

                return protocol_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_3_type_1 = SsoProtocolType3Type1(data)

                return protocol_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SsoProtocolType1
                | SsoProtocolType2Type1
                | SsoProtocolType3Type1
                | Unset,
                data,
            )

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        domains = cast(list[str], d.pop("domains", UNSET))

        _domain_records = d.pop("domain_records", UNSET)
        domain_records: list[SsoDomainRecord] | Unset = UNSET
        if _domain_records is not UNSET:
            domain_records = []
            for domain_records_item_data in _domain_records:
                domain_records_item = SsoDomainRecord.from_dict(
                    domain_records_item_data
                )

                domain_records.append(domain_records_item)

        def _parse_oidc_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oidc_issuer = _parse_oidc_issuer(d.pop("oidc_issuer", UNSET))

        def _parse_oidc_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oidc_client_id = _parse_oidc_client_id(d.pop("oidc_client_id", UNSET))

        def _parse_saml_metadata_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_metadata_url = _parse_saml_metadata_url(d.pop("saml_metadata_url", UNSET))

        def _parse_redirect_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_uri = _parse_redirect_uri(d.pop("redirect_uri", UNSET))

        def _parse_saml_sp_metadata_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saml_sp_metadata_url = _parse_saml_sp_metadata_url(
            d.pop("saml_sp_metadata_url", UNSET)
        )

        def _parse_identity_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_provider = _parse_identity_provider(d.pop("identity_provider", UNSET))

        signed_in_through_provider = d.pop("signed_in_through_provider", UNSET)

        def _parse_emergency_owner(
            data: object,
        ) -> None | SsoEmergencyOwnerType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                emergency_owner_type_0 = SsoEmergencyOwnerType0.from_dict(data)

                return emergency_owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SsoEmergencyOwnerType0 | Unset, data)

        emergency_owner = _parse_emergency_owner(d.pop("emergency_owner", UNSET))

        _moving = d.pop("moving", UNSET)
        moving: SsoMoving | Unset
        if isinstance(_moving, Unset):
            moving = UNSET
        else:
            moving = SsoMoving.from_dict(_moving)

        sso = cls(
            enabled=enabled,
            active=active,
            protocol=protocol,
            domains=domains,
            domain_records=domain_records,
            oidc_issuer=oidc_issuer,
            oidc_client_id=oidc_client_id,
            saml_metadata_url=saml_metadata_url,
            redirect_uri=redirect_uri,
            saml_sp_metadata_url=saml_sp_metadata_url,
            identity_provider=identity_provider,
            signed_in_through_provider=signed_in_through_provider,
            emergency_owner=emergency_owner,
            moving=moving,
        )

        sso.additional_properties = d
        return sso

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.region_status import RegionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.beacon import Beacon
    from ..models.region_location import RegionLocation
    from ..models.region_offer import RegionOffer


T = TypeVar("T", bound="Region")


@_attrs_define
class Region:
    """
    Attributes:
        id (str): A region by its continent, in lower case with dashes: `us-east`, `europe-west`, `uk`. An older region
            ID is still accepted, and answers carry the new one.
        name (str): Its name.
        country (str):
        continent (str): `north-america`, `europe`, `asia`, `oceania`, `south-america`, `middle-east`, `africa`.
        location (RegionLocation):
        status (RegionStatus): `planned` regions are listed but not yet startable; `draining` ones are closing, with
            notice.
        offers (list[RegionOffer]):
        sla_eligible (bool):
        draining_until (datetime.datetime | Unset): Only on a `draining` region, once its closing date is set: when it
            closes.
        beacon (Beacon | Unset): A region's ping beacon. It echoes UDP datagrams up to 64 bytes, accepts TCP connects
            and answers ICMP ping. Measure each region that has one (median of 5). A region with no beacon leaves `beacon`
            out; send `player_ips` with a start instead.
        version_ready (bool | Unset): Only with the `app` filter.
    """

    id: str
    name: str
    country: str
    continent: str
    location: RegionLocation
    status: RegionStatus
    offers: list[RegionOffer]
    sla_eligible: bool
    draining_until: datetime.datetime | Unset = UNSET
    beacon: Beacon | Unset = UNSET
    version_ready: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        country = self.country

        continent = self.continent

        location = self.location.to_dict()

        status = self.status.value

        offers = []
        for offers_item_data in self.offers:
            offers_item = offers_item_data.to_dict()
            offers.append(offers_item)

        sla_eligible = self.sla_eligible

        draining_until: str | Unset = UNSET
        if not isinstance(self.draining_until, Unset):
            draining_until = self.draining_until.isoformat()

        beacon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.beacon, Unset):
            beacon = self.beacon.to_dict()

        version_ready = self.version_ready

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "country": country,
                "continent": continent,
                "location": location,
                "status": status,
                "offers": offers,
                "sla_eligible": sla_eligible,
            }
        )
        if draining_until is not UNSET:
            field_dict["draining_until"] = draining_until
        if beacon is not UNSET:
            field_dict["beacon"] = beacon
        if version_ready is not UNSET:
            field_dict["version_ready"] = version_ready

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.beacon import Beacon
        from ..models.region_location import RegionLocation
        from ..models.region_offer import RegionOffer

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        country = d.pop("country")

        continent = d.pop("continent")

        location = RegionLocation.from_dict(d.pop("location"))

        status = RegionStatus(d.pop("status"))

        offers = []
        _offers = d.pop("offers")
        for offers_item_data in _offers:
            offers_item = RegionOffer.from_dict(offers_item_data)

            offers.append(offers_item)

        sla_eligible = d.pop("sla_eligible")

        _draining_until = d.pop("draining_until", UNSET)
        draining_until: datetime.datetime | Unset
        if isinstance(_draining_until, Unset):
            draining_until = UNSET
        else:
            draining_until = datetime.datetime.fromisoformat(_draining_until)

        _beacon = d.pop("beacon", UNSET)
        beacon: Beacon | Unset
        if isinstance(_beacon, Unset):
            beacon = UNSET
        else:
            beacon = Beacon.from_dict(_beacon)

        version_ready = d.pop("version_ready", UNSET)

        region = cls(
            id=id,
            name=name,
            country=country,
            continent=continent,
            location=location,
            status=status,
            offers=offers,
            sla_eligible=sla_eligible,
            draining_until=draining_until,
            beacon=beacon,
            version_ready=version_ready,
        )

        region.additional_properties = d
        return region

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

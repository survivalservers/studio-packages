from enum import StrEnum


class RegionTriedReason(StrEnum):
    NOT_OFFERED = "not_offered"
    NO_CAPACITY = "no_capacity"
    OVER_MAX_PING = "over_max_ping"
    UNAVAILABLE = "unavailable"
    VERSION_NOT_READY = "version_not_ready"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "RegionTriedReason | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

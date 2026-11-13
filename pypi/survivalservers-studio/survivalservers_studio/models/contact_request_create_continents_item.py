from enum import StrEnum


class ContactRequestCreateContinentsItem(StrEnum):
    AFRICA = "africa"
    ASIA = "asia"
    EUROPE = "europe"
    MIDDLE_EAST = "middle-east"
    NORTH_AMERICA = "north-america"
    OCEANIA = "oceania"
    SOUTH_AMERICA = "south-america"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "ContactRequestCreateContinentsItem | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

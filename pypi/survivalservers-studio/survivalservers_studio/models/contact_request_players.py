from enum import StrEnum


class ContactRequestPlayers(StrEnum):
    OVER_100000 = "over_100000"
    UP_TO_100 = "up_to_100"
    UP_TO_1000 = "up_to_1000"
    UP_TO_10000 = "up_to_10000"
    UP_TO_100000 = "up_to_100000"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "ContactRequestPlayers | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

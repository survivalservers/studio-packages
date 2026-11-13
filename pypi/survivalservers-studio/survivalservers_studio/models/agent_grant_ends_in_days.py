from enum import IntEnum


class AgentGrantEndsInDays(IntEnum):
    VALUE_7 = 7
    VALUE_30 = 30
    VALUE_90 = 90
    VALUE_365 = 365

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AgentGrantEndsInDays | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, int) or isinstance(value, bool):
            return None
        unknown = int.__new__(cls, value)
        unknown._name_ = f"VALUE_{value}"
        unknown._value_ = value
        return unknown

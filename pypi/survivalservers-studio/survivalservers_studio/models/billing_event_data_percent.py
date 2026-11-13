from enum import IntEnum


class BillingEventDataPercent(IntEnum):
    VALUE_80 = 80
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "BillingEventDataPercent | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, int) or isinstance(value, bool):
            return None
        unknown = int.__new__(cls, value)
        unknown._name_ = f"VALUE_{value}"
        unknown._value_ = value
        return unknown

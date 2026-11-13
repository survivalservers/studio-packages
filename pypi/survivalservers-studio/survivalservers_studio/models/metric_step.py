from enum import StrEnum


class MetricStep(StrEnum):
    VALUE_0 = "1s"
    VALUE_1 = "10s"
    VALUE_2 = "1m"
    VALUE_3 = "5m"
    VALUE_4 = "15m"
    VALUE_5 = "1h"
    VALUE_6 = "6h"
    VALUE_7 = "1d"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "MetricStep | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

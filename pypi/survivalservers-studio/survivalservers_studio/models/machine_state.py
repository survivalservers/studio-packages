from enum import StrEnum


class MachineState(StrEnum):
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    REMOVED = "removed"
    UNREACHABLE = "unreachable"
    WAITING_FOR_AGENT = "waiting_for_agent"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "MachineState | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

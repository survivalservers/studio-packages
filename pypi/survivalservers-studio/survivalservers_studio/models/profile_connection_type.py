from enum import StrEnum


class ProfileConnectionType(StrEnum):
    A2S = "a2s"
    CONSOLE = "console"
    HTTP = "http"
    ISLE_RCON = "isle_rcon"
    RCON = "rcon"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "ProfileConnectionType | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

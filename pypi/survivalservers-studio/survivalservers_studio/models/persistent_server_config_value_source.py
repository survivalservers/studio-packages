from enum import StrEnum


class PersistentServerConfigValueSource(StrEnum):
    CONFIG_SET = "config_set"
    DEFAULT = "default"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "PersistentServerConfigValueSource | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

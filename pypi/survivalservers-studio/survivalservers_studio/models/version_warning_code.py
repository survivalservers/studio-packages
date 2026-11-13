from enum import StrEnum


class VersionWarningCode(StrEnum):
    SECRET_IN_ARGS = "secret_in_args"
    SECRET_IN_ARGS_UNREAL = "secret_in_args_unreal"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "VersionWarningCode | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

from enum import StrEnum


class BackupFailureReason(StrEnum):
    DISK_FULL = "disk_full"
    LOCKED_FILE = "locked_file"
    MACHINE_ERROR = "machine_error"
    READ_ERROR = "read_error"
    TOO_BIG = "too_big"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "BackupFailureReason | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

from enum import StrEnum


class BuildFailureCode(StrEnum):
    BAD_ARCHIVE = "bad_archive"
    CHECKSUM_MISMATCH = "checksum_mismatch"
    IMAGE_NOT_FOUND = "image_not_found"
    REGISTRY_DENIED = "registry_denied"
    SCAN_FLAGGED = "scan_flagged"
    TOO_LARGE = "too_large"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "BuildFailureCode | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

from enum import StrEnum


class GameServerExitReason(StrEnum):
    API = "api"
    BOOT_TIMEOUT = "boot_timeout"
    BULK = "bulk"
    CRASHED = "crashed"
    HEALTH_TIMEOUT = "health_timeout"
    LOST_CONTACT = "lost_contact"
    MACHINE_FAILURE = "machine_failure"
    MAX_DURATION = "max_duration"
    OUT_OF_DISK = "out_of_disk"
    OUT_OF_MEMORY = "out_of_memory"
    RESTART = "restart"
    SELF = "self"
    TTL = "ttl"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "GameServerExitReason | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

from enum import StrEnum


class RateClass(StrEnum):
    BACKUP_STORAGE = "backup_storage"
    ON_DEMAND_2GB = "on_demand_2gb"
    ON_DEMAND_4GB = "on_demand_4gb"
    OWN_MACHINE = "own_machine"
    PERSISTENT_SERVER = "persistent_server"
    PERSISTENT_SERVER_PAUSED = "persistent_server_paused"
    RESERVED = "reserved"
    RESERVED_INCLUDED = "reserved_included"
    WARM = "warm"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "RateClass | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

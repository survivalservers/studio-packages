from enum import StrEnum


class AgentPermission(StrEnum):
    BUILDS = "builds"
    BULK_ACTIONS = "bulk_actions"
    PERSISTENT_SERVERS = "persistent_servers"
    START = "start"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "AgentPermission | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

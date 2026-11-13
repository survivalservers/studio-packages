from enum import StrEnum


class Scope(StrEnum):
    APPSREAD = "apps:read"
    APPSWRITE = "apps:write"
    AUDITREAD = "audit:read"
    BACKUPSREAD = "backups:read"
    BACKUPSWRITE = "backups:write"
    BILLINGWRITE = "billing:write"
    BUILDSWRITE = "builds:write"
    GAME_SERVERSREAD = "game_servers:read"
    GAME_SERVERSWRITE = "game_servers:write"
    KEYSWRITE = "keys:write"
    LOGSREAD = "logs:read"
    MACHINESREAD = "machines:read"
    MACHINESWRITE = "machines:write"
    MEMBERSWRITE = "members:write"
    PERSISTENT_SERVERSREAD = "persistent_servers:read"
    PERSISTENT_SERVERSWRITE = "persistent_servers:write"
    STUDIOWRITE = "studio:write"
    USAGEREAD = "usage:read"
    WEBHOOKSREAD = "webhooks:read"
    WEBHOOKSWRITE = "webhooks:write"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "Scope | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

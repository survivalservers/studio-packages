from enum import StrEnum


class TimelineEntryType(StrEnum):
    ALLOCATED = "allocated"
    ARTIFACTS_COLLECTED = "artifacts_collected"
    BACKUP_FAILED = "backup_failed"
    CREATED = "created"
    DISK_HIGH = "disk_high"
    EXITED = "exited"
    LAUNCHED = "launched"
    MEMORY_HIGH = "memory_high"
    PAUSED = "paused"
    PLAYERS_CHANGED = "players_changed"
    PROCESS_ENDED = "process_ended"
    PROFILE_WRITTEN = "profile_written"
    READY = "ready"
    RESTARTED = "restarted"
    RESTORED_NOTHING = "restored_nothing"
    RESUMED = "resumed"
    RESUMING = "resuming"
    SAVE_FAILED = "save_failed"
    SIMULATED_PLAYERS_CHANGED = "simulated_players_changed"
    STOP_COMMAND_FAILED = "stop_command_failed"
    STOP_REQUESTED = "stop_requested"
    UPDATE_HELD = "update_held"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "TimelineEntryType | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

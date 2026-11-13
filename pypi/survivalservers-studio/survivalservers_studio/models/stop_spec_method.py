from enum import StrEnum


class StopSpecMethod(StrEnum):
    COMMAND = "command"
    CTRL_BREAK = "ctrl_break"
    CTRL_C = "ctrl_c"
    KILL = "kill"
    LOCAL_API = "local_api"
    SIGINT = "sigint"
    SIGTERM = "sigterm"
    WM_CLOSE = "wm_close"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "StopSpecMethod | None":
        # The API adds values at any time: a value this version does not know is read as a value of its own.
        if not isinstance(value, str):
            return None
        unknown = str.__new__(cls, value)
        unknown._name_ = value
        unknown._value_ = value
        return unknown

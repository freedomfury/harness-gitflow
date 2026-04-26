from enum import Enum


class EnumCheckStatus(str, Enum):
    ERROR = "error"
    FAILURE = "failure"
    FAILURE_IGNORED = "failure_ignored"
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)

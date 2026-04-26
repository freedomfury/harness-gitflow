from enum import Enum


class EnumWebhookExecutionResult(str, Enum):
    FATAL_ERROR = "fatal_error"
    RETRIABLE_ERROR = "retriable_error"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)

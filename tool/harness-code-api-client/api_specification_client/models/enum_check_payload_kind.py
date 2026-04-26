from enum import Enum


class EnumCheckPayloadKind(str, Enum):
    MARKDOWN = "markdown"
    PIPELINE = "pipeline"
    RAW = "raw"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ImporterPipelineOption(str, Enum):
    CONVERT = "convert"
    IGNORE = "ignore"

    def __str__(self) -> str:
        return str(self.value)

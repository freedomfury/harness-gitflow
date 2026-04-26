from enum import Enum


class EnumLabelType(str, Enum):
    DYNAMIC = "dynamic"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)

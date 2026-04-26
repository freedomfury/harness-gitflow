from enum import Enum


class EnumLabelColor(str, Enum):
    BLUE = "blue"
    BROWN = "brown"
    CYAN = "cyan"
    GREEN = "green"
    INDIGO = "indigo"
    LIME = "lime"
    MINT = "mint"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    VIOLET = "violet"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)

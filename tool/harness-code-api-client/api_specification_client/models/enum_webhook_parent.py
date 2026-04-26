from enum import Enum


class EnumWebhookParent(str, Enum):
    REGISTRY = "registry"
    REPO = "repo"
    SPACE = "space"

    def __str__(self) -> str:
        return str(self.value)

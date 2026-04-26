from enum import Enum


class ListPrincipalsTypeItem(str, Enum):
    SERVICE = "service"
    SERVICEACCOUNT = "serviceaccount"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)

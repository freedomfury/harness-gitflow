from enum import Enum


class DeleteFavoriteResourceType(str, Enum):
    CONNECTOR = "CONNECTOR"
    GITSPACE = "GITSPACE"
    INFRAPROVIDER = "INFRAPROVIDER"
    PIPELINE = "PIPELINE"
    REGISTRY = "REGISTRY"
    REPOSITORY = "REPOSITORY"
    SECRET = "SECRET"
    SERVICE = "SERVICE"
    SERVICEACCOUNT = "SERVICEACCOUNT"
    SPACE = "SPACE"
    TEMPLATE = "TEMPLATE"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)

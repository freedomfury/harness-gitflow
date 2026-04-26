from enum import Enum


class ImporterProviderType(str, Enum):
    AZURE = "azure"
    BITBUCKET = "bitbucket"
    GITEA = "gitea"
    GITHUB = "github"
    GITLAB = "gitlab"
    GOGS = "gogs"
    STASH = "stash"

    def __str__(self) -> str:
        return str(self.value)

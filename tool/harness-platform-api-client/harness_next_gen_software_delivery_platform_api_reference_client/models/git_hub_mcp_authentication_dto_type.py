from typing import Literal, cast

GitHubMcpAuthenticationDTOType = Literal["OAuth", "Token"]

GIT_HUB_MCP_AUTHENTICATION_DTO_TYPE_VALUES: set[GitHubMcpAuthenticationDTOType] = {
    "OAuth",
    "Token",
}


def check_git_hub_mcp_authentication_dto_type(value: str) -> GitHubMcpAuthenticationDTOType:
    if value in GIT_HUB_MCP_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(GitHubMcpAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_HUB_MCP_AUTHENTICATION_DTO_TYPE_VALUES!r}")

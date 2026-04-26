from typing import Literal, cast

MsTeamsConnectorApiAccessType = Literal["OAUTH", "TOKEN"]

MS_TEAMS_CONNECTOR_API_ACCESS_TYPE_VALUES: set[MsTeamsConnectorApiAccessType] = {
    "OAUTH",
    "TOKEN",
}


def check_ms_teams_connector_api_access_type(value: str) -> MsTeamsConnectorApiAccessType:
    if value in MS_TEAMS_CONNECTOR_API_ACCESS_TYPE_VALUES:
        return cast(MsTeamsConnectorApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MS_TEAMS_CONNECTOR_API_ACCESS_TYPE_VALUES!r}")

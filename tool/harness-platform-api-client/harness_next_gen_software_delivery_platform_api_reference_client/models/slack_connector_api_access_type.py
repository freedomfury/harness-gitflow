from typing import Literal, cast

SlackConnectorApiAccessType = Literal["OAUTH", "TOKEN"]

SLACK_CONNECTOR_API_ACCESS_TYPE_VALUES: set[SlackConnectorApiAccessType] = {
    "OAUTH",
    "TOKEN",
}


def check_slack_connector_api_access_type(value: str) -> SlackConnectorApiAccessType:
    if value in SLACK_CONNECTOR_API_ACCESS_TYPE_VALUES:
        return cast(SlackConnectorApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLACK_CONNECTOR_API_ACCESS_TYPE_VALUES!r}")

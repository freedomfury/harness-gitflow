from typing import Literal, cast

ConfluenceConnectorApiAccessType = Literal["OAUTH", "TOKEN"]

CONFLUENCE_CONNECTOR_API_ACCESS_TYPE_VALUES: set[ConfluenceConnectorApiAccessType] = {
    "OAUTH",
    "TOKEN",
}


def check_confluence_connector_api_access_type(value: str) -> ConfluenceConnectorApiAccessType:
    if value in CONFLUENCE_CONNECTOR_API_ACCESS_TYPE_VALUES:
        return cast(ConfluenceConnectorApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONFLUENCE_CONNECTOR_API_ACCESS_TYPE_VALUES!r}")

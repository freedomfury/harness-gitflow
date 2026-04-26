from typing import Literal, cast

SplunkConnectorType = Literal["Anonymous", "Bearer Token(HTTP Header)", "HEC Token", "UsernamePassword"]

SPLUNK_CONNECTOR_TYPE_VALUES: set[SplunkConnectorType] = {
    "Anonymous",
    "Bearer Token(HTTP Header)",
    "HEC Token",
    "UsernamePassword",
}


def check_splunk_connector_type(value: str) -> SplunkConnectorType:
    if value in SPLUNK_CONNECTOR_TYPE_VALUES:
        return cast(SplunkConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SPLUNK_CONNECTOR_TYPE_VALUES!r}")

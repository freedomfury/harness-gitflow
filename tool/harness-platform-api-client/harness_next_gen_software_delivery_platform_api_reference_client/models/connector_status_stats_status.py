from typing import Literal, cast

ConnectorStatusStatsStatus = Literal["FAILURE", "PARTIAL", "PENDING", "SUCCESS", "UNKNOWN"]

CONNECTOR_STATUS_STATS_STATUS_VALUES: set[ConnectorStatusStatsStatus] = {
    "FAILURE",
    "PARTIAL",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_connector_status_stats_status(value: str) -> ConnectorStatusStatsStatus:
    if value in CONNECTOR_STATUS_STATS_STATUS_VALUES:
        return cast(ConnectorStatusStatsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_STATUS_STATS_STATUS_VALUES!r}")

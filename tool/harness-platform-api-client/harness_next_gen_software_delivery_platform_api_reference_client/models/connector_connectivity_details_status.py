from typing import Literal, cast

ConnectorConnectivityDetailsStatus = Literal["FAILURE", "PARTIAL", "PENDING", "SUCCESS", "UNKNOWN"]

CONNECTOR_CONNECTIVITY_DETAILS_STATUS_VALUES: set[ConnectorConnectivityDetailsStatus] = {
    "FAILURE",
    "PARTIAL",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_connector_connectivity_details_status(value: str) -> ConnectorConnectivityDetailsStatus:
    if value in CONNECTOR_CONNECTIVITY_DETAILS_STATUS_VALUES:
        return cast(ConnectorConnectivityDetailsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_CONNECTIVITY_DETAILS_STATUS_VALUES!r}")

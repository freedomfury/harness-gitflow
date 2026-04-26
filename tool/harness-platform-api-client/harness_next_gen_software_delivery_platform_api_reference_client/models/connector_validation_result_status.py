from typing import Literal, cast

ConnectorValidationResultStatus = Literal["FAILURE", "PARTIAL", "PENDING", "SUCCESS", "UNKNOWN"]

CONNECTOR_VALIDATION_RESULT_STATUS_VALUES: set[ConnectorValidationResultStatus] = {
    "FAILURE",
    "PARTIAL",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_connector_validation_result_status(value: str) -> ConnectorValidationResultStatus:
    if value in CONNECTOR_VALIDATION_RESULT_STATUS_VALUES:
        return cast(ConnectorValidationResultStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_VALIDATION_RESULT_STATUS_VALUES!r}")

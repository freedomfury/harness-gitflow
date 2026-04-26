from typing import Literal, cast

ResponseDTOConnectorStatisticsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CONNECTOR_STATISTICS_STATUS_VALUES: set[ResponseDTOConnectorStatisticsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_connector_statistics_status(value: str) -> ResponseDTOConnectorStatisticsStatus:
    if value in RESPONSE_DTO_CONNECTOR_STATISTICS_STATUS_VALUES:
        return cast(ResponseDTOConnectorStatisticsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CONNECTOR_STATISTICS_STATUS_VALUES!r}")

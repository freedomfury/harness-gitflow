from typing import Literal, cast

ResponseDTOConnectorValidationResultStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CONNECTOR_VALIDATION_RESULT_STATUS_VALUES: set[ResponseDTOConnectorValidationResultStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_connector_validation_result_status(value: str) -> ResponseDTOConnectorValidationResultStatus:
    if value in RESPONSE_DTO_CONNECTOR_VALIDATION_RESULT_STATUS_VALUES:
        return cast(ResponseDTOConnectorValidationResultStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CONNECTOR_VALIDATION_RESULT_STATUS_VALUES!r}"
    )

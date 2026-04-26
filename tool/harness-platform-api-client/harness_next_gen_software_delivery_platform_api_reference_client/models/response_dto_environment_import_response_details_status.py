from typing import Literal, cast

ResponseDTOEnvironmentImportResponseDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_IMPORT_RESPONSE_DETAILS_STATUS_VALUES: set[
    ResponseDTOEnvironmentImportResponseDetailsStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_import_response_details_status(
    value: str,
) -> ResponseDTOEnvironmentImportResponseDetailsStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_IMPORT_RESPONSE_DETAILS_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentImportResponseDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_IMPORT_RESPONSE_DETAILS_STATUS_VALUES!r}"
    )

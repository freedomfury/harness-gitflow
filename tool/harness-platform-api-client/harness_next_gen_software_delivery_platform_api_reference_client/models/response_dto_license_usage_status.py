from typing import Literal, cast

ResponseDTOLicenseUsageStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LICENSE_USAGE_STATUS_VALUES: set[ResponseDTOLicenseUsageStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_license_usage_status(value: str) -> ResponseDTOLicenseUsageStatus:
    if value in RESPONSE_DTO_LICENSE_USAGE_STATUS_VALUES:
        return cast(ResponseDTOLicenseUsageStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LICENSE_USAGE_STATUS_VALUES!r}")

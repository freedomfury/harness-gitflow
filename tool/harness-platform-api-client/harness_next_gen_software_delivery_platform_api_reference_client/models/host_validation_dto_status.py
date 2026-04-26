from typing import Literal, cast

HostValidationDTOStatus = Literal["FAILED", "SUCCESS"]

HOST_VALIDATION_DTO_STATUS_VALUES: set[HostValidationDTOStatus] = {
    "FAILED",
    "SUCCESS",
}


def check_host_validation_dto_status(value: str) -> HostValidationDTOStatus:
    if value in HOST_VALIDATION_DTO_STATUS_VALUES:
        return cast(HostValidationDTOStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_VALIDATION_DTO_STATUS_VALUES!r}")

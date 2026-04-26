from typing import Literal, cast

ResponseDTOAllowedValuesUsagesInternalDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ALLOWED_VALUES_USAGES_INTERNAL_DTO_STATUS_VALUES: set[ResponseDTOAllowedValuesUsagesInternalDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_allowed_values_usages_internal_dto_status(
    value: str,
) -> ResponseDTOAllowedValuesUsagesInternalDTOStatus:
    if value in RESPONSE_DTO_ALLOWED_VALUES_USAGES_INTERNAL_DTO_STATUS_VALUES:
        return cast(ResponseDTOAllowedValuesUsagesInternalDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ALLOWED_VALUES_USAGES_INTERNAL_DTO_STATUS_VALUES!r}"
    )

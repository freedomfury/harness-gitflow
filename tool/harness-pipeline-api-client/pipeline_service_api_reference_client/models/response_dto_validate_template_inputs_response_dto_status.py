from typing import Literal, cast

ResponseDTOValidateTemplateInputsResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_VALIDATE_TEMPLATE_INPUTS_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOValidateTemplateInputsResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_validate_template_inputs_response_dto_status(
    value: str,
) -> ResponseDTOValidateTemplateInputsResponseDTOStatus:
    if value in RESPONSE_DTO_VALIDATE_TEMPLATE_INPUTS_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOValidateTemplateInputsResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_VALIDATE_TEMPLATE_INPUTS_RESPONSE_DTO_STATUS_VALUES!r}"
    )

from typing import Literal, cast

ResponseDTOInputSetTemplateResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INPUT_SET_TEMPLATE_RESPONSE_STATUS_VALUES: set[ResponseDTOInputSetTemplateResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_input_set_template_response_status(value: str) -> ResponseDTOInputSetTemplateResponseStatus:
    if value in RESPONSE_DTO_INPUT_SET_TEMPLATE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInputSetTemplateResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INPUT_SET_TEMPLATE_RESPONSE_STATUS_VALUES!r}"
    )

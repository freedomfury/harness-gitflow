from typing import Literal, cast

ResponseDTOInputSetTemplateWithReplacedExpressionsResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INPUT_SET_TEMPLATE_WITH_REPLACED_EXPRESSIONS_RESPONSE_STATUS_VALUES: set[
    ResponseDTOInputSetTemplateWithReplacedExpressionsResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_input_set_template_with_replaced_expressions_response_status(
    value: str,
) -> ResponseDTOInputSetTemplateWithReplacedExpressionsResponseStatus:
    if value in RESPONSE_DTO_INPUT_SET_TEMPLATE_WITH_REPLACED_EXPRESSIONS_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInputSetTemplateWithReplacedExpressionsResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INPUT_SET_TEMPLATE_WITH_REPLACED_EXPRESSIONS_RESPONSE_STATUS_VALUES!r}"
    )

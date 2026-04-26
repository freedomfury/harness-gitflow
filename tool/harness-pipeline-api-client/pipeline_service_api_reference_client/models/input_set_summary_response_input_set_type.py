from typing import Literal, cast

InputSetSummaryResponseInputSetType = Literal["INPUT_SET", "OVERLAY_INPUT_SET"]

INPUT_SET_SUMMARY_RESPONSE_INPUT_SET_TYPE_VALUES: set[InputSetSummaryResponseInputSetType] = {
    "INPUT_SET",
    "OVERLAY_INPUT_SET",
}


def check_input_set_summary_response_input_set_type(value: str) -> InputSetSummaryResponseInputSetType:
    if value in INPUT_SET_SUMMARY_RESPONSE_INPUT_SET_TYPE_VALUES:
        return cast(InputSetSummaryResponseInputSetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INPUT_SET_SUMMARY_RESPONSE_INPUT_SET_TYPE_VALUES!r}")

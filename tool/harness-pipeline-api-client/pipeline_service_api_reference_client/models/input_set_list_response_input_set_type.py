from typing import Literal, cast

InputSetListResponseInputSetType = Literal["INPUT_SET", "OVERLAY_INPUT_SET"]

INPUT_SET_LIST_RESPONSE_INPUT_SET_TYPE_VALUES: set[InputSetListResponseInputSetType] = {
    "INPUT_SET",
    "OVERLAY_INPUT_SET",
}


def check_input_set_list_response_input_set_type(value: str) -> InputSetListResponseInputSetType:
    if value in INPUT_SET_LIST_RESPONSE_INPUT_SET_TYPE_VALUES:
        return cast(InputSetListResponseInputSetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INPUT_SET_LIST_RESPONSE_INPUT_SET_TYPE_VALUES!r}")

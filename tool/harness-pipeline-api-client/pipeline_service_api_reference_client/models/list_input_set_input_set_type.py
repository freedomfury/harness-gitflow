from typing import Literal, cast

ListInputSetInputSetType = Literal["ALL", "INPUT_SET", "OVERLAY_INPUT_SET"]

LIST_INPUT_SET_INPUT_SET_TYPE_VALUES: set[ListInputSetInputSetType] = {
    "ALL",
    "INPUT_SET",
    "OVERLAY_INPUT_SET",
}


def check_list_input_set_input_set_type(value: str) -> ListInputSetInputSetType:
    if value in LIST_INPUT_SET_INPUT_SET_TYPE_VALUES:
        return cast(ListInputSetInputSetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INPUT_SET_INPUT_SET_TYPE_VALUES!r}")

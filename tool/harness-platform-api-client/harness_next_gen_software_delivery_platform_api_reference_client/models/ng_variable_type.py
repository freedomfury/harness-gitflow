from typing import Literal, cast

NGVariableType = Literal["Number", "Secret", "String"]

NG_VARIABLE_TYPE_VALUES: set[NGVariableType] = {
    "Number",
    "Secret",
    "String",
}


def check_ng_variable_type(value: str) -> NGVariableType:
    if value in NG_VARIABLE_TYPE_VALUES:
        return cast(NGVariableType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NG_VARIABLE_TYPE_VALUES!r}")

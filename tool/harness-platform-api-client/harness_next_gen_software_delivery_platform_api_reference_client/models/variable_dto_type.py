from typing import Literal, cast

VariableDTOType = Literal["String"]

VARIABLE_DTO_TYPE_VALUES: set[VariableDTOType] = {
    "String",
}


def check_variable_dto_type(value: str) -> VariableDTOType:
    if value in VARIABLE_DTO_TYPE_VALUES:
        return cast(VariableDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VARIABLE_DTO_TYPE_VALUES!r}")

from typing import Literal, cast

VariableConfigDTOValueType = Literal["FIXED"]

VARIABLE_CONFIG_DTO_VALUE_TYPE_VALUES: set[VariableConfigDTOValueType] = {
    "FIXED",
}


def check_variable_config_dto_value_type(value: str) -> VariableConfigDTOValueType:
    if value in VARIABLE_CONFIG_DTO_VALUE_TYPE_VALUES:
        return cast(VariableConfigDTOValueType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VARIABLE_CONFIG_DTO_VALUE_TYPE_VALUES!r}")

from typing import Literal, cast

InputSetValidatorValidatorType = Literal["ALLOWED_VALUES", "REGEX", "SELECT_MANY_FROM", "SELECT_ONE_FROM"]

INPUT_SET_VALIDATOR_VALIDATOR_TYPE_VALUES: set[InputSetValidatorValidatorType] = {
    "ALLOWED_VALUES",
    "REGEX",
    "SELECT_MANY_FROM",
    "SELECT_ONE_FROM",
}


def check_input_set_validator_validator_type(value: str) -> InputSetValidatorValidatorType:
    if value in INPUT_SET_VALIDATOR_VALIDATOR_TYPE_VALUES:
        return cast(InputSetValidatorValidatorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INPUT_SET_VALIDATOR_VALIDATOR_TYPE_VALUES!r}")

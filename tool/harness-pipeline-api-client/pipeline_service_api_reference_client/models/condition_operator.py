from typing import Literal, cast

ConditionOperator = Literal["equals", "in", "not equals", "not in"]

CONDITION_OPERATOR_VALUES: set[ConditionOperator] = {
    "equals",
    "in",
    "not equals",
    "not in",
}


def check_condition_operator(value: str) -> ConditionOperator:
    if value in CONDITION_OPERATOR_VALUES:
        return cast(ConditionOperator, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_OPERATOR_VALUES!r}")

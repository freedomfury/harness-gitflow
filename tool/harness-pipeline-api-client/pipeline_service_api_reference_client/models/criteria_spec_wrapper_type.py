from typing import Literal, cast

CriteriaSpecWrapperType = Literal["Jexl", "KeyValues"]

CRITERIA_SPEC_WRAPPER_TYPE_VALUES: set[CriteriaSpecWrapperType] = {
    "Jexl",
    "KeyValues",
}


def check_criteria_spec_wrapper_type(value: str) -> CriteriaSpecWrapperType:
    if value in CRITERIA_SPEC_WRAPPER_TYPE_VALUES:
        return cast(CriteriaSpecWrapperType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CRITERIA_SPEC_WRAPPER_TYPE_VALUES!r}")

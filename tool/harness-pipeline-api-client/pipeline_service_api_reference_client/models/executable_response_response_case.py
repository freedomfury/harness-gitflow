from typing import Literal, cast

ExecutableResponseResponseCase = Literal[
    "ASYNC",
    "ASYNCCHAIN",
    "CHILD",
    "CHILDCHAIN",
    "CHILDREN",
    "FACILITATOR",
    "RESPONSE_NOT_SET",
    "SKIPTASK",
    "SYNC",
    "TASK",
    "TASKCHAIN",
]

EXECUTABLE_RESPONSE_RESPONSE_CASE_VALUES: set[ExecutableResponseResponseCase] = {
    "ASYNC",
    "ASYNCCHAIN",
    "CHILD",
    "CHILDCHAIN",
    "CHILDREN",
    "FACILITATOR",
    "RESPONSE_NOT_SET",
    "SKIPTASK",
    "SYNC",
    "TASK",
    "TASKCHAIN",
}


def check_executable_response_response_case(value: str) -> ExecutableResponseResponseCase:
    if value in EXECUTABLE_RESPONSE_RESPONSE_CASE_VALUES:
        return cast(ExecutableResponseResponseCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTABLE_RESPONSE_RESPONSE_CASE_VALUES!r}")

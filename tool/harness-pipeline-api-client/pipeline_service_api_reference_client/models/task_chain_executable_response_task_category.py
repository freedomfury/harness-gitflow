from typing import Literal, cast

TaskChainExecutableResponseTaskCategory = Literal[
    "DELEGATE_TASK_V1", "DELEGATE_TASK_V2", "UNKNOWN_CATEGORY", "UNRECOGNIZED"
]

TASK_CHAIN_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES: set[TaskChainExecutableResponseTaskCategory] = {
    "DELEGATE_TASK_V1",
    "DELEGATE_TASK_V2",
    "UNKNOWN_CATEGORY",
    "UNRECOGNIZED",
}


def check_task_chain_executable_response_task_category(value: str) -> TaskChainExecutableResponseTaskCategory:
    if value in TASK_CHAIN_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES:
        return cast(TaskChainExecutableResponseTaskCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_CHAIN_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES!r}"
    )

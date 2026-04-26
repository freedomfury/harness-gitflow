from typing import Literal, cast

TaskExecutableResponseTaskCategory = Literal["DELEGATE_TASK_V1", "DELEGATE_TASK_V2", "UNKNOWN_CATEGORY", "UNRECOGNIZED"]

TASK_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES: set[TaskExecutableResponseTaskCategory] = {
    "DELEGATE_TASK_V1",
    "DELEGATE_TASK_V2",
    "UNKNOWN_CATEGORY",
    "UNRECOGNIZED",
}


def check_task_executable_response_task_category(value: str) -> TaskExecutableResponseTaskCategory:
    if value in TASK_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES:
        return cast(TaskExecutableResponseTaskCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_EXECUTABLE_RESPONSE_TASK_CATEGORY_VALUES!r}")

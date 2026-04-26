from typing import Literal, cast

TaskExecutableResponseOrBuilderTaskCategory = Literal[
    "DELEGATE_TASK_V1", "DELEGATE_TASK_V2", "UNKNOWN_CATEGORY", "UNRECOGNIZED"
]

TASK_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES: set[TaskExecutableResponseOrBuilderTaskCategory] = {
    "DELEGATE_TASK_V1",
    "DELEGATE_TASK_V2",
    "UNKNOWN_CATEGORY",
    "UNRECOGNIZED",
}


def check_task_executable_response_or_builder_task_category(value: str) -> TaskExecutableResponseOrBuilderTaskCategory:
    if value in TASK_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES:
        return cast(TaskExecutableResponseOrBuilderTaskCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES!r}"
    )

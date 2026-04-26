from typing import Literal, cast

TaskChainExecutableResponseOrBuilderTaskCategory = Literal[
    "DELEGATE_TASK_V1", "DELEGATE_TASK_V2", "UNKNOWN_CATEGORY", "UNRECOGNIZED"
]

TASK_CHAIN_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES: set[
    TaskChainExecutableResponseOrBuilderTaskCategory
] = {
    "DELEGATE_TASK_V1",
    "DELEGATE_TASK_V2",
    "UNKNOWN_CATEGORY",
    "UNRECOGNIZED",
}


def check_task_chain_executable_response_or_builder_task_category(
    value: str,
) -> TaskChainExecutableResponseOrBuilderTaskCategory:
    if value in TASK_CHAIN_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES:
        return cast(TaskChainExecutableResponseOrBuilderTaskCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_CHAIN_EXECUTABLE_RESPONSE_OR_BUILDER_TASK_CATEGORY_VALUES!r}"
    )

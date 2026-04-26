from typing import Literal, cast

QueuedPipelineFilterPriorityTypesItem = Literal["HIGH", "LOW", "NORMAL"]

QUEUED_PIPELINE_FILTER_PRIORITY_TYPES_ITEM_VALUES: set[QueuedPipelineFilterPriorityTypesItem] = {
    "HIGH",
    "LOW",
    "NORMAL",
}


def check_queued_pipeline_filter_priority_types_item(value: str) -> QueuedPipelineFilterPriorityTypesItem:
    if value in QUEUED_PIPELINE_FILTER_PRIORITY_TYPES_ITEM_VALUES:
        return cast(QueuedPipelineFilterPriorityTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUEUED_PIPELINE_FILTER_PRIORITY_TYPES_ITEM_VALUES!r}"
    )

from typing import Literal, cast

QueuedPipelineFilterTriggerTypesItem = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

QUEUED_PIPELINE_FILTER_TRIGGER_TYPES_ITEM_VALUES: set[QueuedPipelineFilterTriggerTypesItem] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_queued_pipeline_filter_trigger_types_item(value: str) -> QueuedPipelineFilterTriggerTypesItem:
    if value in QUEUED_PIPELINE_FILTER_TRIGGER_TYPES_ITEM_VALUES:
        return cast(QueuedPipelineFilterTriggerTypesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {QUEUED_PIPELINE_FILTER_TRIGGER_TYPES_ITEM_VALUES!r}")

from typing import Literal, cast

PipelineExecutionFilterPropertiesTriggerTypesItem = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

PIPELINE_EXECUTION_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES: set[
    PipelineExecutionFilterPropertiesTriggerTypesItem
] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_pipeline_execution_filter_properties_trigger_types_item(
    value: str,
) -> PipelineExecutionFilterPropertiesTriggerTypesItem:
    if value in PIPELINE_EXECUTION_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES:
        return cast(PipelineExecutionFilterPropertiesTriggerTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES!r}"
    )

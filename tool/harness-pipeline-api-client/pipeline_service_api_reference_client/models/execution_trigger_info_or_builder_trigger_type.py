from typing import Literal, cast

ExecutionTriggerInfoOrBuilderTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

EXECUTION_TRIGGER_INFO_OR_BUILDER_TRIGGER_TYPE_VALUES: set[ExecutionTriggerInfoOrBuilderTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_execution_trigger_info_or_builder_trigger_type(value: str) -> ExecutionTriggerInfoOrBuilderTriggerType:
    if value in EXECUTION_TRIGGER_INFO_OR_BUILDER_TRIGGER_TYPE_VALUES:
        return cast(ExecutionTriggerInfoOrBuilderTriggerType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXECUTION_TRIGGER_INFO_OR_BUILDER_TRIGGER_TYPE_VALUES!r}"
    )

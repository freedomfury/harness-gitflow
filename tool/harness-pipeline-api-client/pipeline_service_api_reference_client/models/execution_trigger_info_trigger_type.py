from typing import Literal, cast

ExecutionTriggerInfoTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

EXECUTION_TRIGGER_INFO_TRIGGER_TYPE_VALUES: set[ExecutionTriggerInfoTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_execution_trigger_info_trigger_type(value: str) -> ExecutionTriggerInfoTriggerType:
    if value in EXECUTION_TRIGGER_INFO_TRIGGER_TYPE_VALUES:
        return cast(ExecutionTriggerInfoTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTION_TRIGGER_INFO_TRIGGER_TYPE_VALUES!r}")

from typing import Literal, cast

RerunInfoOrBuilderPrevTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

RERUN_INFO_OR_BUILDER_PREV_TRIGGER_TYPE_VALUES: set[RerunInfoOrBuilderPrevTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_rerun_info_or_builder_prev_trigger_type(value: str) -> RerunInfoOrBuilderPrevTriggerType:
    if value in RERUN_INFO_OR_BUILDER_PREV_TRIGGER_TYPE_VALUES:
        return cast(RerunInfoOrBuilderPrevTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RERUN_INFO_OR_BUILDER_PREV_TRIGGER_TYPE_VALUES!r}")

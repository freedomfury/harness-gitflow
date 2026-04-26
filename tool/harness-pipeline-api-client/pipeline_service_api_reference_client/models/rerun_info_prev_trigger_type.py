from typing import Literal, cast

RerunInfoPrevTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

RERUN_INFO_PREV_TRIGGER_TYPE_VALUES: set[RerunInfoPrevTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_rerun_info_prev_trigger_type(value: str) -> RerunInfoPrevTriggerType:
    if value in RERUN_INFO_PREV_TRIGGER_TYPE_VALUES:
        return cast(RerunInfoPrevTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RERUN_INFO_PREV_TRIGGER_TYPE_VALUES!r}")

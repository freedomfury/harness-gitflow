from typing import Literal, cast

RerunInfoRootTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

RERUN_INFO_ROOT_TRIGGER_TYPE_VALUES: set[RerunInfoRootTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_rerun_info_root_trigger_type(value: str) -> RerunInfoRootTriggerType:
    if value in RERUN_INFO_ROOT_TRIGGER_TYPE_VALUES:
        return cast(RerunInfoRootTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RERUN_INFO_ROOT_TRIGGER_TYPE_VALUES!r}")

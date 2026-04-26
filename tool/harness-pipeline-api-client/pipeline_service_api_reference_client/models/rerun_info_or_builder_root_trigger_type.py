from typing import Literal, cast

RerunInfoOrBuilderRootTriggerType = Literal[
    "ARTIFACT", "MANIFEST", "MANUAL", "NOOP", "SCHEDULER_CRON", "UNRECOGNIZED", "WEBHOOK", "WEBHOOK_CUSTOM"
]

RERUN_INFO_OR_BUILDER_ROOT_TRIGGER_TYPE_VALUES: set[RerunInfoOrBuilderRootTriggerType] = {
    "ARTIFACT",
    "MANIFEST",
    "MANUAL",
    "NOOP",
    "SCHEDULER_CRON",
    "UNRECOGNIZED",
    "WEBHOOK",
    "WEBHOOK_CUSTOM",
}


def check_rerun_info_or_builder_root_trigger_type(value: str) -> RerunInfoOrBuilderRootTriggerType:
    if value in RERUN_INFO_OR_BUILDER_ROOT_TRIGGER_TYPE_VALUES:
        return cast(RerunInfoOrBuilderRootTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RERUN_INFO_OR_BUILDER_ROOT_TRIGGER_TYPE_VALUES!r}")

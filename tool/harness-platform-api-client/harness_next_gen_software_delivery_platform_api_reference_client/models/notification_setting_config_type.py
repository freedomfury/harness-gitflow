from typing import Literal, cast

NotificationSettingConfigType = Literal["DATADOG", "EMAIL", "MSTEAMS", "PAGERDUTY", "SLACK", "WEBHOOK"]

NOTIFICATION_SETTING_CONFIG_TYPE_VALUES: set[NotificationSettingConfigType] = {
    "DATADOG",
    "EMAIL",
    "MSTEAMS",
    "PAGERDUTY",
    "SLACK",
    "WEBHOOK",
}


def check_notification_setting_config_type(value: str) -> NotificationSettingConfigType:
    if value in NOTIFICATION_SETTING_CONFIG_TYPE_VALUES:
        return cast(NotificationSettingConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SETTING_CONFIG_TYPE_VALUES!r}")

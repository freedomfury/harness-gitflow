from typing import Literal, cast

NotificationSettingConfigDTOType = Literal["DATADOG", "EMAIL", "MSTEAMS", "PAGERDUTY", "SLACK", "WEBHOOK"]

NOTIFICATION_SETTING_CONFIG_DTO_TYPE_VALUES: set[NotificationSettingConfigDTOType] = {
    "DATADOG",
    "EMAIL",
    "MSTEAMS",
    "PAGERDUTY",
    "SLACK",
    "WEBHOOK",
}


def check_notification_setting_config_dto_type(value: str) -> NotificationSettingConfigDTOType:
    if value in NOTIFICATION_SETTING_CONFIG_DTO_TYPE_VALUES:
        return cast(NotificationSettingConfigDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SETTING_CONFIG_DTO_TYPE_VALUES!r}")

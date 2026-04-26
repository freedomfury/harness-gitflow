from typing import Literal, cast

SettingDTOAllowedScopesItem = Literal["ACCOUNT", "ORGANIZATION", "PROJECT"]

SETTING_DTO_ALLOWED_SCOPES_ITEM_VALUES: set[SettingDTOAllowedScopesItem] = {
    "ACCOUNT",
    "ORGANIZATION",
    "PROJECT",
}


def check_setting_dto_allowed_scopes_item(value: str) -> SettingDTOAllowedScopesItem:
    if value in SETTING_DTO_ALLOWED_SCOPES_ITEM_VALUES:
        return cast(SettingDTOAllowedScopesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_DTO_ALLOWED_SCOPES_ITEM_VALUES!r}")

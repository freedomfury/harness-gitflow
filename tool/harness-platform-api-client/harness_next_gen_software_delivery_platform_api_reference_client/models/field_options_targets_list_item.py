from typing import Literal, cast

FieldOptionsTargetsListItem = Literal[
    "TARGET_TYPE_ENUM",
    "TARGET_TYPE_ENUM_ENTRY",
    "TARGET_TYPE_EXTENSION_RANGE",
    "TARGET_TYPE_FIELD",
    "TARGET_TYPE_FILE",
    "TARGET_TYPE_MESSAGE",
    "TARGET_TYPE_METHOD",
    "TARGET_TYPE_ONEOF",
    "TARGET_TYPE_SERVICE",
    "TARGET_TYPE_UNKNOWN",
]

FIELD_OPTIONS_TARGETS_LIST_ITEM_VALUES: set[FieldOptionsTargetsListItem] = {
    "TARGET_TYPE_ENUM",
    "TARGET_TYPE_ENUM_ENTRY",
    "TARGET_TYPE_EXTENSION_RANGE",
    "TARGET_TYPE_FIELD",
    "TARGET_TYPE_FILE",
    "TARGET_TYPE_MESSAGE",
    "TARGET_TYPE_METHOD",
    "TARGET_TYPE_ONEOF",
    "TARGET_TYPE_SERVICE",
    "TARGET_TYPE_UNKNOWN",
}


def check_field_options_targets_list_item(value: str) -> FieldOptionsTargetsListItem:
    if value in FIELD_OPTIONS_TARGETS_LIST_ITEM_VALUES:
        return cast(FieldOptionsTargetsListItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_TARGETS_LIST_ITEM_VALUES!r}")

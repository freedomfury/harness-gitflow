from typing import Literal, cast

TemplateResponseStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

TEMPLATE_RESPONSE_STORE_TYPE_VALUES: set[TemplateResponseStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_template_response_store_type(value: str) -> TemplateResponseStoreType:
    if value in TEMPLATE_RESPONSE_STORE_TYPE_VALUES:
        return cast(TemplateResponseStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_RESPONSE_STORE_TYPE_VALUES!r}")

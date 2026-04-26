from typing import Literal, cast

LangSmithAuthenticationDTOType = Literal["ApiKey"]

LANG_SMITH_AUTHENTICATION_DTO_TYPE_VALUES: set[LangSmithAuthenticationDTOType] = {
    "ApiKey",
}


def check_lang_smith_authentication_dto_type(value: str) -> LangSmithAuthenticationDTOType:
    if value in LANG_SMITH_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(LangSmithAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LANG_SMITH_AUTHENTICATION_DTO_TYPE_VALUES!r}")

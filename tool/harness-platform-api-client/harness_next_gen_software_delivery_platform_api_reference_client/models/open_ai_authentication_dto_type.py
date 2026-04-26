from typing import Literal, cast

OpenAIAuthenticationDTOType = Literal["Token"]

OPEN_AI_AUTHENTICATION_DTO_TYPE_VALUES: set[OpenAIAuthenticationDTOType] = {
    "Token",
}


def check_open_ai_authentication_dto_type(value: str) -> OpenAIAuthenticationDTOType:
    if value in OPEN_AI_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(OpenAIAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OPEN_AI_AUTHENTICATION_DTO_TYPE_VALUES!r}")

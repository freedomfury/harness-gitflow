from typing import Literal, cast

BambooAuthenticationDTOType = Literal["Anonymous", "Bearer Token(HTTP Header)", "UsernamePassword"]

BAMBOO_AUTHENTICATION_DTO_TYPE_VALUES: set[BambooAuthenticationDTOType] = {
    "Anonymous",
    "Bearer Token(HTTP Header)",
    "UsernamePassword",
}


def check_bamboo_authentication_dto_type(value: str) -> BambooAuthenticationDTOType:
    if value in BAMBOO_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(BambooAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BAMBOO_AUTHENTICATION_DTO_TYPE_VALUES!r}")

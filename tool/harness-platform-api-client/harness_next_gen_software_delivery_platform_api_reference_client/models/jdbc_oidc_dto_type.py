from typing import Literal, cast

JDBCOidcDTOType = Literal["Gcp"]

JDBC_OIDC_DTO_TYPE_VALUES: set[JDBCOidcDTOType] = {
    "Gcp",
}


def check_jdbc_oidc_dto_type(value: str) -> JDBCOidcDTOType:
    if value in JDBC_OIDC_DTO_TYPE_VALUES:
        return cast(JDBCOidcDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JDBC_OIDC_DTO_TYPE_VALUES!r}")

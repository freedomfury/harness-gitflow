from typing import Literal, cast

JDBCAuthenticationDTOType = Literal[
    "Aws", "InheritFromDelegate", "Kerberos", "KeyPair", "Oidc", "ServiceAccount", "UsernamePassword"
]

JDBC_AUTHENTICATION_DTO_TYPE_VALUES: set[JDBCAuthenticationDTOType] = {
    "Aws",
    "InheritFromDelegate",
    "Kerberos",
    "KeyPair",
    "Oidc",
    "ServiceAccount",
    "UsernamePassword",
}


def check_jdbc_authentication_dto_type(value: str) -> JDBCAuthenticationDTOType:
    if value in JDBC_AUTHENTICATION_DTO_TYPE_VALUES:
        return cast(JDBCAuthenticationDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JDBC_AUTHENTICATION_DTO_TYPE_VALUES!r}")

from typing import Literal, cast

JDBCAwsDTOType = Literal["InheritFromDelegate", "Irsa", "ManualConfig", "OidcAuthentication"]

JDBC_AWS_DTO_TYPE_VALUES: set[JDBCAwsDTOType] = {
    "InheritFromDelegate",
    "Irsa",
    "ManualConfig",
    "OidcAuthentication",
}


def check_jdbc_aws_dto_type(value: str) -> JDBCAwsDTOType:
    if value in JDBC_AWS_DTO_TYPE_VALUES:
        return cast(JDBCAwsDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JDBC_AWS_DTO_TYPE_VALUES!r}")

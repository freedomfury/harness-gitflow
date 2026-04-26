from typing import Literal, cast

JDBCKerberosDTOTgtGenerationMethod = Literal["KeyTabFilePath", "Password"]

JDBC_KERBEROS_DTO_TGT_GENERATION_METHOD_VALUES: set[JDBCKerberosDTOTgtGenerationMethod] = {
    "KeyTabFilePath",
    "Password",
}


def check_jdbc_kerberos_dto_tgt_generation_method(value: str) -> JDBCKerberosDTOTgtGenerationMethod:
    if value in JDBC_KERBEROS_DTO_TGT_GENERATION_METHOD_VALUES:
        return cast(JDBCKerberosDTOTgtGenerationMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JDBC_KERBEROS_DTO_TGT_GENERATION_METHOD_VALUES!r}")

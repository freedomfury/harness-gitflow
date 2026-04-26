from typing import Literal, cast

KerberosConfigDTOTgtGenerationMethod = Literal["KeyTabFilePath", "Password"]

KERBEROS_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES: set[KerberosConfigDTOTgtGenerationMethod] = {
    "KeyTabFilePath",
    "Password",
}


def check_kerberos_config_dto_tgt_generation_method(value: str) -> KerberosConfigDTOTgtGenerationMethod:
    if value in KERBEROS_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES:
        return cast(KerberosConfigDTOTgtGenerationMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KERBEROS_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES!r}")

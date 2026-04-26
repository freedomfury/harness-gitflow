from typing import Literal, cast

KerberosWinRmConfigDTOTgtGenerationMethod = Literal["KeyTabFilePath", "Password"]

KERBEROS_WIN_RM_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES: set[KerberosWinRmConfigDTOTgtGenerationMethod] = {
    "KeyTabFilePath",
    "Password",
}


def check_kerberos_win_rm_config_dto_tgt_generation_method(value: str) -> KerberosWinRmConfigDTOTgtGenerationMethod:
    if value in KERBEROS_WIN_RM_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES:
        return cast(KerberosWinRmConfigDTOTgtGenerationMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KERBEROS_WIN_RM_CONFIG_DTO_TGT_GENERATION_METHOD_VALUES!r}"
    )

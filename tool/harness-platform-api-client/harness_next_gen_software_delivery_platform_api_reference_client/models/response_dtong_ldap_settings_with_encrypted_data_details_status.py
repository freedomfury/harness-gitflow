from typing import Literal, cast

ResponseDTONGLdapSettingsWithEncryptedDataDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTONG_LDAP_SETTINGS_WITH_ENCRYPTED_DATA_DETAILS_STATUS_VALUES: set[
    ResponseDTONGLdapSettingsWithEncryptedDataDetailsStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtong_ldap_settings_with_encrypted_data_details_status(
    value: str,
) -> ResponseDTONGLdapSettingsWithEncryptedDataDetailsStatus:
    if value in RESPONSE_DTONG_LDAP_SETTINGS_WITH_ENCRYPTED_DATA_DETAILS_STATUS_VALUES:
        return cast(ResponseDTONGLdapSettingsWithEncryptedDataDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTONG_LDAP_SETTINGS_WITH_ENCRYPTED_DATA_DETAILS_STATUS_VALUES!r}"
    )

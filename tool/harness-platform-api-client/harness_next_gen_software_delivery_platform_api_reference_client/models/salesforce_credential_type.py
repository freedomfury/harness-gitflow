from typing import Literal, cast

SalesforceCredentialType = Literal["Jwt", "SfdxAuthUrl"]

SALESFORCE_CREDENTIAL_TYPE_VALUES: set[SalesforceCredentialType] = {
    "Jwt",
    "SfdxAuthUrl",
}


def check_salesforce_credential_type(value: str) -> SalesforceCredentialType:
    if value in SALESFORCE_CREDENTIAL_TYPE_VALUES:
        return cast(SalesforceCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SALESFORCE_CREDENTIAL_TYPE_VALUES!r}")

from typing import Literal, cast

JiraAuthenticationType = Literal["PersonalAccessToken", "UsernamePassword"]

JIRA_AUTHENTICATION_TYPE_VALUES: set[JiraAuthenticationType] = {
    "PersonalAccessToken",
    "UsernamePassword",
}


def check_jira_authentication_type(value: str) -> JiraAuthenticationType:
    if value in JIRA_AUTHENTICATION_TYPE_VALUES:
        return cast(JiraAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JIRA_AUTHENTICATION_TYPE_VALUES!r}")

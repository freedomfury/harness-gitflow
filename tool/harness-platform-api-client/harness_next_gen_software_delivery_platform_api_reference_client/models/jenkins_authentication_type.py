from typing import Literal, cast

JenkinsAuthenticationType = Literal["Anonymous", "Bearer Token(HTTP Header)", "UsernamePassword"]

JENKINS_AUTHENTICATION_TYPE_VALUES: set[JenkinsAuthenticationType] = {
    "Anonymous",
    "Bearer Token(HTTP Header)",
    "UsernamePassword",
}


def check_jenkins_authentication_type(value: str) -> JenkinsAuthenticationType:
    if value in JENKINS_AUTHENTICATION_TYPE_VALUES:
        return cast(JenkinsAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JENKINS_AUTHENTICATION_TYPE_VALUES!r}")

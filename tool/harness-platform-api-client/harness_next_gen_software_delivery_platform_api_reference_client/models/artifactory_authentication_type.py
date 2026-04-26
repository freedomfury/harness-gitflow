from typing import Literal, cast

ArtifactoryAuthenticationType = Literal["Anonymous", "UsernamePassword"]

ARTIFACTORY_AUTHENTICATION_TYPE_VALUES: set[ArtifactoryAuthenticationType] = {
    "Anonymous",
    "UsernamePassword",
}


def check_artifactory_authentication_type(value: str) -> ArtifactoryAuthenticationType:
    if value in ARTIFACTORY_AUTHENTICATION_TYPE_VALUES:
        return cast(ArtifactoryAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACTORY_AUTHENTICATION_TYPE_VALUES!r}")

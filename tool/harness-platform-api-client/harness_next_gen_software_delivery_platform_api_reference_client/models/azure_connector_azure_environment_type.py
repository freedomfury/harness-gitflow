from typing import Literal, cast

AzureConnectorAzureEnvironmentType = Literal["AZURE", "AZURE_US_GOVERNMENT"]

AZURE_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES: set[AzureConnectorAzureEnvironmentType] = {
    "AZURE",
    "AZURE_US_GOVERNMENT",
}


def check_azure_connector_azure_environment_type(value: str) -> AzureConnectorAzureEnvironmentType:
    if value in AZURE_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES:
        return cast(AzureConnectorAzureEnvironmentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AZURE_CONNECTOR_AZURE_ENVIRONMENT_TYPE_VALUES!r}")

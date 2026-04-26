from typing import Literal, cast

InfrastructureResponseDTODeploymentType = Literal[
    "Asg",
    "AWS_SAM",
    "AwsLambda",
    "AzureContainerApps",
    "AzureFunction",
    "AzureWebApp",
    "CustomDeployment",
    "ECS",
    "Elastigroup",
    "GoogleCloudFunctions",
    "GoogleCloudRun",
    "GoogleManagedInstanceGroup",
    "Kubernetes",
    "NativeHelm",
    "Salesforce",
    "ServerlessAwsLambda",
    "SERVICE_YAML_V1_TYPE",
    "Ssh",
    "TAS",
    "WinRm",
]

INFRASTRUCTURE_RESPONSE_DTO_DEPLOYMENT_TYPE_VALUES: set[InfrastructureResponseDTODeploymentType] = {
    "Asg",
    "AWS_SAM",
    "AwsLambda",
    "AzureContainerApps",
    "AzureFunction",
    "AzureWebApp",
    "CustomDeployment",
    "ECS",
    "Elastigroup",
    "GoogleCloudFunctions",
    "GoogleCloudRun",
    "GoogleManagedInstanceGroup",
    "Kubernetes",
    "NativeHelm",
    "Salesforce",
    "ServerlessAwsLambda",
    "SERVICE_YAML_V1_TYPE",
    "Ssh",
    "TAS",
    "WinRm",
}


def check_infrastructure_response_dto_deployment_type(value: str) -> InfrastructureResponseDTODeploymentType:
    if value in INFRASTRUCTURE_RESPONSE_DTO_DEPLOYMENT_TYPE_VALUES:
        return cast(InfrastructureResponseDTODeploymentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INFRASTRUCTURE_RESPONSE_DTO_DEPLOYMENT_TYPE_VALUES!r}"
    )

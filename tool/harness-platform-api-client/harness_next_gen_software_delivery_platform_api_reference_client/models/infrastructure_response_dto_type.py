from typing import Literal, cast

InfrastructureResponseDTOType = Literal[
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
    "KubernetesAws",
    "KubernetesAzure",
    "KubernetesDirect",
    "KubernetesGcp",
    "KubernetesRancher",
    "Pdc",
    "Salesforce",
    "ServerlessAwsLambda",
    "SshWinRmAws",
    "SshWinRmAzure",
    "TAS",
]

INFRASTRUCTURE_RESPONSE_DTO_TYPE_VALUES: set[InfrastructureResponseDTOType] = {
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
    "KubernetesAws",
    "KubernetesAzure",
    "KubernetesDirect",
    "KubernetesGcp",
    "KubernetesRancher",
    "Pdc",
    "Salesforce",
    "ServerlessAwsLambda",
    "SshWinRmAws",
    "SshWinRmAzure",
    "TAS",
}


def check_infrastructure_response_dto_type(value: str) -> InfrastructureResponseDTOType:
    if value in INFRASTRUCTURE_RESPONSE_DTO_TYPE_VALUES:
        return cast(InfrastructureResponseDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INFRASTRUCTURE_RESPONSE_DTO_TYPE_VALUES!r}")

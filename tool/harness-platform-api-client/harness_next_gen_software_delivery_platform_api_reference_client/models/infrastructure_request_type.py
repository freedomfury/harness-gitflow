from typing import Literal, cast

InfrastructureRequestType = Literal[
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

INFRASTRUCTURE_REQUEST_TYPE_VALUES: set[InfrastructureRequestType] = {
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


def check_infrastructure_request_type(value: str) -> InfrastructureRequestType:
    if value in INFRASTRUCTURE_REQUEST_TYPE_VALUES:
        return cast(InfrastructureRequestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INFRASTRUCTURE_REQUEST_TYPE_VALUES!r}")

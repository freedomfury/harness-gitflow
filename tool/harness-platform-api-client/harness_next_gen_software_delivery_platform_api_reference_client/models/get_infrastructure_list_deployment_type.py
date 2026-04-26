from typing import Literal, cast

GetInfrastructureListDeploymentType = Literal[
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

GET_INFRASTRUCTURE_LIST_DEPLOYMENT_TYPE_VALUES: set[GetInfrastructureListDeploymentType] = {
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


def check_get_infrastructure_list_deployment_type(value: str) -> GetInfrastructureListDeploymentType:
    if value in GET_INFRASTRUCTURE_LIST_DEPLOYMENT_TYPE_VALUES:
        return cast(GetInfrastructureListDeploymentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INFRASTRUCTURE_LIST_DEPLOYMENT_TYPE_VALUES!r}")

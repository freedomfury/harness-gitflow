from typing import Literal, cast

GetServiceListType = Literal[
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

GET_SERVICE_LIST_TYPE_VALUES: set[GetServiceListType] = {
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


def check_get_service_list_type(value: str) -> GetServiceListType:
    if value in GET_SERVICE_LIST_TYPE_VALUES:
        return cast(GetServiceListType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_SERVICE_LIST_TYPE_VALUES!r}")

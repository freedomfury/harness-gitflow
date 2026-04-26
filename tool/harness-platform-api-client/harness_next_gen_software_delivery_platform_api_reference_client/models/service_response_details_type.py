from typing import Literal, cast

ServiceResponseDetailsType = Literal[
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

SERVICE_RESPONSE_DETAILS_TYPE_VALUES: set[ServiceResponseDetailsType] = {
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


def check_service_response_details_type(value: str) -> ServiceResponseDetailsType:
    if value in SERVICE_RESPONSE_DETAILS_TYPE_VALUES:
        return cast(ServiceResponseDetailsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_RESPONSE_DETAILS_TYPE_VALUES!r}")

from typing import Literal, cast

GetFilterListType = Literal[
    "Anomaly",
    "Audit",
    "Autocud",
    "CCMBudget",
    "CCMConnector",
    "CCMK8sConnector",
    "CCMRecommendation",
    "Connector",
    "Delegate",
    "DelegateProfile",
    "Deployment",
    "Environment",
    "EnvironmentGroup",
    "FileStore",
    "InputSet",
    "Override",
    "PipelineExecution",
    "PipelineSetup",
    "RIInventory",
    "RuleExecution",
    "Secret",
    "Service",
    "SPInventory",
    "Template",
    "Trigger",
    "Webhook",
]

GET_FILTER_LIST_TYPE_VALUES: set[GetFilterListType] = {
    "Anomaly",
    "Audit",
    "Autocud",
    "CCMBudget",
    "CCMConnector",
    "CCMK8sConnector",
    "CCMRecommendation",
    "Connector",
    "Delegate",
    "DelegateProfile",
    "Deployment",
    "Environment",
    "EnvironmentGroup",
    "FileStore",
    "InputSet",
    "Override",
    "PipelineExecution",
    "PipelineSetup",
    "RIInventory",
    "RuleExecution",
    "Secret",
    "Service",
    "SPInventory",
    "Template",
    "Trigger",
    "Webhook",
}


def check_get_filter_list_type(value: str) -> GetFilterListType:
    if value in GET_FILTER_LIST_TYPE_VALUES:
        return cast(GetFilterListType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_FILTER_LIST_TYPE_VALUES!r}")

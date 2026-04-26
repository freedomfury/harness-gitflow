from typing import Literal, cast

DelegateFilterPropertiesDTOFilterType = Literal[
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

DELEGATE_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES: set[DelegateFilterPropertiesDTOFilterType] = {
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


def check_delegate_filter_properties_dto_filter_type(value: str) -> DelegateFilterPropertiesDTOFilterType:
    if value in DELEGATE_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES:
        return cast(DelegateFilterPropertiesDTOFilterType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELEGATE_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES!r}"
    )

from typing import Literal, cast

FilesFilterPropertiesDTOFilterType = Literal[
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

FILES_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES: set[FilesFilterPropertiesDTOFilterType] = {
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


def check_files_filter_properties_dto_filter_type(value: str) -> FilesFilterPropertiesDTOFilterType:
    if value in FILES_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES:
        return cast(FilesFilterPropertiesDTOFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILES_FILTER_PROPERTIES_DTO_FILTER_TYPE_VALUES!r}")

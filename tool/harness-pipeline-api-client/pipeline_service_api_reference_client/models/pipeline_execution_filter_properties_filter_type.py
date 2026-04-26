from typing import Literal, cast

PipelineExecutionFilterPropertiesFilterType = Literal[
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

PIPELINE_EXECUTION_FILTER_PROPERTIES_FILTER_TYPE_VALUES: set[PipelineExecutionFilterPropertiesFilterType] = {
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


def check_pipeline_execution_filter_properties_filter_type(value: str) -> PipelineExecutionFilterPropertiesFilterType:
    if value in PIPELINE_EXECUTION_FILTER_PROPERTIES_FILTER_TYPE_VALUES:
        return cast(PipelineExecutionFilterPropertiesFilterType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_FILTER_PROPERTIES_FILTER_TYPE_VALUES!r}"
    )

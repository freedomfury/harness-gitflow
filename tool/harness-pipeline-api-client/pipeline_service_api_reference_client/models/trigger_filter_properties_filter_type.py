from typing import Literal, cast

TriggerFilterPropertiesFilterType = Literal[
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

TRIGGER_FILTER_PROPERTIES_FILTER_TYPE_VALUES: set[TriggerFilterPropertiesFilterType] = {
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


def check_trigger_filter_properties_filter_type(value: str) -> TriggerFilterPropertiesFilterType:
    if value in TRIGGER_FILTER_PROPERTIES_FILTER_TYPE_VALUES:
        return cast(TriggerFilterPropertiesFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_FILTER_PROPERTIES_FILTER_TYPE_VALUES!r}")

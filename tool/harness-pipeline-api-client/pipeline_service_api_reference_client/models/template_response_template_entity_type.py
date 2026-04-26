from typing import Literal, cast

TemplateResponseTemplateEntityType = Literal[
    "ArtifactSource",
    "CustomDeployment",
    "MonitoredService",
    "Notification",
    "Pipeline",
    "SecretManager",
    "Stage",
    "Step",
    "StepGroup",
    "Workspace",
]

TEMPLATE_RESPONSE_TEMPLATE_ENTITY_TYPE_VALUES: set[TemplateResponseTemplateEntityType] = {
    "ArtifactSource",
    "CustomDeployment",
    "MonitoredService",
    "Notification",
    "Pipeline",
    "SecretManager",
    "Stage",
    "Step",
    "StepGroup",
    "Workspace",
}


def check_template_response_template_entity_type(value: str) -> TemplateResponseTemplateEntityType:
    if value in TEMPLATE_RESPONSE_TEMPLATE_ENTITY_TYPE_VALUES:
        return cast(TemplateResponseTemplateEntityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_RESPONSE_TEMPLATE_ENTITY_TYPE_VALUES!r}")

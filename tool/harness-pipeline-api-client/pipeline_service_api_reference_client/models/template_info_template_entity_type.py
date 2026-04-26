from typing import Literal, cast

TemplateInfoTemplateEntityType = Literal[
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

TEMPLATE_INFO_TEMPLATE_ENTITY_TYPE_VALUES: set[TemplateInfoTemplateEntityType] = {
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


def check_template_info_template_entity_type(value: str) -> TemplateInfoTemplateEntityType:
    if value in TEMPLATE_INFO_TEMPLATE_ENTITY_TYPE_VALUES:
        return cast(TemplateInfoTemplateEntityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_INFO_TEMPLATE_ENTITY_TYPE_VALUES!r}")

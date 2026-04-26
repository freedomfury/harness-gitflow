from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OidcIdTokenCustomAttributesStructure")


@_attrs_define
class OidcIdTokenCustomAttributesStructure:
    """This includes all the ID token custom attributes

    Attributes:
        account_id (str):
        organization_id (str | Unset):
        project_id (str | Unset):
        pipeline_id (str | Unset):
        environment_id (str | Unset):
        environment_type (str | Unset):
        connector_id (str | Unset):
        connector_name (str | Unset):
        service_id (str | Unset):
        service_name (str | Unset):
        triggered_by_name (str | Unset):
        trigger_by_email (str | Unset):
        stage_type (str | Unset):
        step_type (str | Unset):
        context (str | Unset):
        artifact_id (str | Unset):
        artifact_type (str | Unset):
        artifact_name (str | Unset):
        artifact_digest (str | Unset):
        tag (str | Unset):
        step_execution_id (str | Unset):
    """

    account_id: str
    organization_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    pipeline_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    environment_type: str | Unset = UNSET
    connector_id: str | Unset = UNSET
    connector_name: str | Unset = UNSET
    service_id: str | Unset = UNSET
    service_name: str | Unset = UNSET
    triggered_by_name: str | Unset = UNSET
    trigger_by_email: str | Unset = UNSET
    stage_type: str | Unset = UNSET
    step_type: str | Unset = UNSET
    context: str | Unset = UNSET
    artifact_id: str | Unset = UNSET
    artifact_type: str | Unset = UNSET
    artifact_name: str | Unset = UNSET
    artifact_digest: str | Unset = UNSET
    tag: str | Unset = UNSET
    step_execution_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        organization_id = self.organization_id

        project_id = self.project_id

        pipeline_id = self.pipeline_id

        environment_id = self.environment_id

        environment_type = self.environment_type

        connector_id = self.connector_id

        connector_name = self.connector_name

        service_id = self.service_id

        service_name = self.service_name

        triggered_by_name = self.triggered_by_name

        trigger_by_email = self.trigger_by_email

        stage_type = self.stage_type

        step_type = self.step_type

        context = self.context

        artifact_id = self.artifact_id

        artifact_type = self.artifact_type

        artifact_name = self.artifact_name

        artifact_digest = self.artifact_digest

        tag = self.tag

        step_execution_id = self.step_execution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if pipeline_id is not UNSET:
            field_dict["pipeline_id"] = pipeline_id
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if environment_type is not UNSET:
            field_dict["environment_type"] = environment_type
        if connector_id is not UNSET:
            field_dict["connector_id"] = connector_id
        if connector_name is not UNSET:
            field_dict["connector_name"] = connector_name
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if triggered_by_name is not UNSET:
            field_dict["triggered_by_name"] = triggered_by_name
        if trigger_by_email is not UNSET:
            field_dict["trigger_by_email"] = trigger_by_email
        if stage_type is not UNSET:
            field_dict["stage_type"] = stage_type
        if step_type is not UNSET:
            field_dict["step_type"] = step_type
        if context is not UNSET:
            field_dict["context"] = context
        if artifact_id is not UNSET:
            field_dict["artifact_id"] = artifact_id
        if artifact_type is not UNSET:
            field_dict["artifact_type"] = artifact_type
        if artifact_name is not UNSET:
            field_dict["artifact_name"] = artifact_name
        if artifact_digest is not UNSET:
            field_dict["artifact_digest"] = artifact_digest
        if tag is not UNSET:
            field_dict["tag"] = tag
        if step_execution_id is not UNSET:
            field_dict["step_execution_id"] = step_execution_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        organization_id = d.pop("organization_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        pipeline_id = d.pop("pipeline_id", UNSET)

        environment_id = d.pop("environment_id", UNSET)

        environment_type = d.pop("environment_type", UNSET)

        connector_id = d.pop("connector_id", UNSET)

        connector_name = d.pop("connector_name", UNSET)

        service_id = d.pop("service_id", UNSET)

        service_name = d.pop("service_name", UNSET)

        triggered_by_name = d.pop("triggered_by_name", UNSET)

        trigger_by_email = d.pop("trigger_by_email", UNSET)

        stage_type = d.pop("stage_type", UNSET)

        step_type = d.pop("step_type", UNSET)

        context = d.pop("context", UNSET)

        artifact_id = d.pop("artifact_id", UNSET)

        artifact_type = d.pop("artifact_type", UNSET)

        artifact_name = d.pop("artifact_name", UNSET)

        artifact_digest = d.pop("artifact_digest", UNSET)

        tag = d.pop("tag", UNSET)

        step_execution_id = d.pop("step_execution_id", UNSET)

        oidc_id_token_custom_attributes_structure = cls(
            account_id=account_id,
            organization_id=organization_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            environment_id=environment_id,
            environment_type=environment_type,
            connector_id=connector_id,
            connector_name=connector_name,
            service_id=service_id,
            service_name=service_name,
            triggered_by_name=triggered_by_name,
            trigger_by_email=trigger_by_email,
            stage_type=stage_type,
            step_type=step_type,
            context=context,
            artifact_id=artifact_id,
            artifact_type=artifact_type,
            artifact_name=artifact_name,
            artifact_digest=artifact_digest,
            tag=tag,
            step_execution_id=step_execution_id,
        )

        oidc_id_token_custom_attributes_structure.additional_properties = d
        return oidc_id_token_custom_attributes_structure

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_trigger_details_response_dto_registration_status import (
    NGTriggerDetailsResponseDTORegistrationStatus,
    check_ng_trigger_details_response_dto_registration_status,
)
from ..models.ng_trigger_details_response_dto_type import (
    NGTriggerDetailsResponseDTOType,
    check_ng_trigger_details_response_dto_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_details import BuildDetails
    from ..models.last_trigger_execution_details import LastTriggerExecutionDetails
    from ..models.ng_trigger_details_response_dto_tags import NGTriggerDetailsResponseDTOTags
    from ..models.trigger_status import TriggerStatus
    from ..models.webhook_details import WebhookDetails


T = TypeVar("T", bound="NGTriggerDetailsResponseDTO")


@_attrs_define
class NGTriggerDetailsResponseDTO:
    """
    Attributes:
        name (str | Unset):
        identifier (str | Unset):
        description (str | Unset):
        type_ (NGTriggerDetailsResponseDTOType | Unset):
        trigger_status (TriggerStatus | Unset):
        last_trigger_execution_details (LastTriggerExecutionDetails | Unset):
        webhook_details (WebhookDetails | Unset):
        build_details (BuildDetails | Unset):
        tags (NGTriggerDetailsResponseDTOTags | Unset):
        executions (list[int] | Unset):
        yaml (str | Unset):
        webhook_url (str | Unset):
        webhook_curl_command (str | Unset):
        registration_status (NGTriggerDetailsResponseDTORegistrationStatus | Unset):
        enabled (bool | Unset):
        is_pipeline_input_outdated (bool | Unset):
        yaml_version (str | Unset):
        pipeline_input_outdated (bool | Unset):
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    type_: NGTriggerDetailsResponseDTOType | Unset = UNSET
    trigger_status: TriggerStatus | Unset = UNSET
    last_trigger_execution_details: LastTriggerExecutionDetails | Unset = UNSET
    webhook_details: WebhookDetails | Unset = UNSET
    build_details: BuildDetails | Unset = UNSET
    tags: NGTriggerDetailsResponseDTOTags | Unset = UNSET
    executions: list[int] | Unset = UNSET
    yaml: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    webhook_curl_command: str | Unset = UNSET
    registration_status: NGTriggerDetailsResponseDTORegistrationStatus | Unset = UNSET
    enabled: bool | Unset = UNSET
    is_pipeline_input_outdated: bool | Unset = UNSET
    yaml_version: str | Unset = UNSET
    pipeline_input_outdated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        description = self.description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        trigger_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_status, Unset):
            trigger_status = self.trigger_status.to_dict()

        last_trigger_execution_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_trigger_execution_details, Unset):
            last_trigger_execution_details = self.last_trigger_execution_details.to_dict()

        webhook_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_details, Unset):
            webhook_details = self.webhook_details.to_dict()

        build_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_details, Unset):
            build_details = self.build_details.to_dict()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        executions: list[int] | Unset = UNSET
        if not isinstance(self.executions, Unset):
            executions = self.executions

        yaml = self.yaml

        webhook_url = self.webhook_url

        webhook_curl_command = self.webhook_curl_command

        registration_status: str | Unset = UNSET
        if not isinstance(self.registration_status, Unset):
            registration_status = self.registration_status

        enabled = self.enabled

        is_pipeline_input_outdated = self.is_pipeline_input_outdated

        yaml_version = self.yaml_version

        pipeline_input_outdated = self.pipeline_input_outdated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if trigger_status is not UNSET:
            field_dict["triggerStatus"] = trigger_status
        if last_trigger_execution_details is not UNSET:
            field_dict["lastTriggerExecutionDetails"] = last_trigger_execution_details
        if webhook_details is not UNSET:
            field_dict["webhookDetails"] = webhook_details
        if build_details is not UNSET:
            field_dict["buildDetails"] = build_details
        if tags is not UNSET:
            field_dict["tags"] = tags
        if executions is not UNSET:
            field_dict["executions"] = executions
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if webhook_curl_command is not UNSET:
            field_dict["webhookCurlCommand"] = webhook_curl_command
        if registration_status is not UNSET:
            field_dict["registrationStatus"] = registration_status
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if is_pipeline_input_outdated is not UNSET:
            field_dict["isPipelineInputOutdated"] = is_pipeline_input_outdated
        if yaml_version is not UNSET:
            field_dict["yamlVersion"] = yaml_version
        if pipeline_input_outdated is not UNSET:
            field_dict["pipelineInputOutdated"] = pipeline_input_outdated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_details import BuildDetails
        from ..models.last_trigger_execution_details import LastTriggerExecutionDetails
        from ..models.ng_trigger_details_response_dto_tags import NGTriggerDetailsResponseDTOTags
        from ..models.trigger_status import TriggerStatus
        from ..models.webhook_details import WebhookDetails

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NGTriggerDetailsResponseDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_ng_trigger_details_response_dto_type(_type_)

        _trigger_status = d.pop("triggerStatus", UNSET)
        trigger_status: TriggerStatus | Unset
        if isinstance(_trigger_status, Unset):
            trigger_status = UNSET
        else:
            trigger_status = TriggerStatus.from_dict(_trigger_status)

        _last_trigger_execution_details = d.pop("lastTriggerExecutionDetails", UNSET)
        last_trigger_execution_details: LastTriggerExecutionDetails | Unset
        if isinstance(_last_trigger_execution_details, Unset):
            last_trigger_execution_details = UNSET
        else:
            last_trigger_execution_details = LastTriggerExecutionDetails.from_dict(_last_trigger_execution_details)

        _webhook_details = d.pop("webhookDetails", UNSET)
        webhook_details: WebhookDetails | Unset
        if isinstance(_webhook_details, Unset):
            webhook_details = UNSET
        else:
            webhook_details = WebhookDetails.from_dict(_webhook_details)

        _build_details = d.pop("buildDetails", UNSET)
        build_details: BuildDetails | Unset
        if isinstance(_build_details, Unset):
            build_details = UNSET
        else:
            build_details = BuildDetails.from_dict(_build_details)

        _tags = d.pop("tags", UNSET)
        tags: NGTriggerDetailsResponseDTOTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = NGTriggerDetailsResponseDTOTags.from_dict(_tags)

        executions = cast(list[int], d.pop("executions", UNSET))

        yaml = d.pop("yaml", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        webhook_curl_command = d.pop("webhookCurlCommand", UNSET)

        _registration_status = d.pop("registrationStatus", UNSET)
        registration_status: NGTriggerDetailsResponseDTORegistrationStatus | Unset
        if isinstance(_registration_status, Unset):
            registration_status = UNSET
        else:
            registration_status = check_ng_trigger_details_response_dto_registration_status(_registration_status)

        enabled = d.pop("enabled", UNSET)

        is_pipeline_input_outdated = d.pop("isPipelineInputOutdated", UNSET)

        yaml_version = d.pop("yamlVersion", UNSET)

        pipeline_input_outdated = d.pop("pipelineInputOutdated", UNSET)

        ng_trigger_details_response_dto = cls(
            name=name,
            identifier=identifier,
            description=description,
            type_=type_,
            trigger_status=trigger_status,
            last_trigger_execution_details=last_trigger_execution_details,
            webhook_details=webhook_details,
            build_details=build_details,
            tags=tags,
            executions=executions,
            yaml=yaml,
            webhook_url=webhook_url,
            webhook_curl_command=webhook_curl_command,
            registration_status=registration_status,
            enabled=enabled,
            is_pipeline_input_outdated=is_pipeline_input_outdated,
            yaml_version=yaml_version,
            pipeline_input_outdated=pipeline_input_outdated,
        )

        ng_trigger_details_response_dto.additional_properties = d
        return ng_trigger_details_response_dto

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ng_trigger_response_type import NGTriggerResponseType, check_ng_trigger_response_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ng_trigger_response_errors import NGTriggerResponseErrors
    from ..models.parameter_field_list_string import ParameterFieldListString


T = TypeVar("T", bound="NGTriggerResponse")


@_attrs_define
class NGTriggerResponse:
    """This contains the trigger details

    Attributes:
        name (str | Unset):
        identifier (str | Unset):
        description (str | Unset):
        type_ (NGTriggerResponseType | Unset):
        account_identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        target_identifier (str | Unset):
        yaml (str | Unset):
        enabled (bool | Unset):
        errors (NGTriggerResponseErrors | Unset):
        error_response (bool | Unset):
        stages_to_execute (ParameterFieldListString | Unset):
        yaml_version (str | Unset):
        webhook_url (str | Unset):
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    type_: NGTriggerResponseType | Unset = UNSET
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    target_identifier: str | Unset = UNSET
    yaml: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    errors: NGTriggerResponseErrors | Unset = UNSET
    error_response: bool | Unset = UNSET
    stages_to_execute: ParameterFieldListString | Unset = UNSET
    yaml_version: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        description = self.description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        target_identifier = self.target_identifier

        yaml = self.yaml

        enabled = self.enabled

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        error_response = self.error_response

        stages_to_execute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stages_to_execute, Unset):
            stages_to_execute = self.stages_to_execute.to_dict()

        yaml_version = self.yaml_version

        webhook_url = self.webhook_url

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
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if target_identifier is not UNSET:
            field_dict["targetIdentifier"] = target_identifier
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if errors is not UNSET:
            field_dict["errors"] = errors
        if error_response is not UNSET:
            field_dict["errorResponse"] = error_response
        if stages_to_execute is not UNSET:
            field_dict["stagesToExecute"] = stages_to_execute
        if yaml_version is not UNSET:
            field_dict["yamlVersion"] = yaml_version
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ng_trigger_response_errors import NGTriggerResponseErrors
        from ..models.parameter_field_list_string import ParameterFieldListString

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NGTriggerResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_ng_trigger_response_type(_type_)

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        target_identifier = d.pop("targetIdentifier", UNSET)

        yaml = d.pop("yaml", UNSET)

        enabled = d.pop("enabled", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: NGTriggerResponseErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = NGTriggerResponseErrors.from_dict(_errors)

        error_response = d.pop("errorResponse", UNSET)

        _stages_to_execute = d.pop("stagesToExecute", UNSET)
        stages_to_execute: ParameterFieldListString | Unset
        if isinstance(_stages_to_execute, Unset):
            stages_to_execute = UNSET
        else:
            stages_to_execute = ParameterFieldListString.from_dict(_stages_to_execute)

        yaml_version = d.pop("yamlVersion", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        ng_trigger_response = cls(
            name=name,
            identifier=identifier,
            description=description,
            type_=type_,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            target_identifier=target_identifier,
            yaml=yaml,
            enabled=enabled,
            errors=errors,
            error_response=error_response,
            stages_to_execute=stages_to_execute,
            yaml_version=yaml_version,
            webhook_url=webhook_url,
        )

        ng_trigger_response.additional_properties = d
        return ng_trigger_response

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

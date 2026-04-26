from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.input_set_error_wrapper import InputSetErrorWrapper
    from ..models.input_set_response_tags import InputSetResponseTags


T = TypeVar("T", bound="InputSetResponse")


@_attrs_define
class InputSetResponse:
    """This contains Input Set details.

    Attributes:
        account_id (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        pipeline_identifier (str | Unset): Pipeline Identifier for the entity.
        identifier (str | Unset): Input Set Identifier
        input_set_yaml (str | Unset): Input Set YAML
        name (str | Unset): Input Set Name
        description (str | Unset): Input Set description
        tags (InputSetResponseTags | Unset): Input Set tags
        is_outdated (bool | Unset):
        is_error_response (bool | Unset):
        input_set_error_wrapper (InputSetErrorWrapper | Unset): This contains the error response if the Input Set save
            failed
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        outdated (bool | Unset):
        error_response (bool | Unset):
    """

    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    input_set_yaml: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: InputSetResponseTags | Unset = UNSET
    is_outdated: bool | Unset = UNSET
    is_error_response: bool | Unset = UNSET
    input_set_error_wrapper: InputSetErrorWrapper | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    outdated: bool | Unset = UNSET
    error_response: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        pipeline_identifier = self.pipeline_identifier

        identifier = self.identifier

        input_set_yaml = self.input_set_yaml

        name = self.name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        is_outdated = self.is_outdated

        is_error_response = self.is_error_response

        input_set_error_wrapper: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_set_error_wrapper, Unset):
            input_set_error_wrapper = self.input_set_error_wrapper.to_dict()

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        outdated = self.outdated

        error_response = self.error_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if input_set_yaml is not UNSET:
            field_dict["inputSetYaml"] = input_set_yaml
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_outdated is not UNSET:
            field_dict["isOutdated"] = is_outdated
        if is_error_response is not UNSET:
            field_dict["isErrorResponse"] = is_error_response
        if input_set_error_wrapper is not UNSET:
            field_dict["inputSetErrorWrapper"] = input_set_error_wrapper
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if error_response is not UNSET:
            field_dict["errorResponse"] = error_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.input_set_error_wrapper import InputSetErrorWrapper
        from ..models.input_set_response_tags import InputSetResponseTags

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        input_set_yaml = d.pop("inputSetYaml", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: InputSetResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = InputSetResponseTags.from_dict(_tags)

        is_outdated = d.pop("isOutdated", UNSET)

        is_error_response = d.pop("isErrorResponse", UNSET)

        _input_set_error_wrapper = d.pop("inputSetErrorWrapper", UNSET)
        input_set_error_wrapper: InputSetErrorWrapper | Unset
        if isinstance(_input_set_error_wrapper, Unset):
            input_set_error_wrapper = UNSET
        else:
            input_set_error_wrapper = InputSetErrorWrapper.from_dict(_input_set_error_wrapper)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        _entity_validity_details = d.pop("entityValidityDetails", UNSET)
        entity_validity_details: EntityGitDetails | Unset
        if isinstance(_entity_validity_details, Unset):
            entity_validity_details = UNSET
        else:
            entity_validity_details = EntityGitDetails.from_dict(_entity_validity_details)

        outdated = d.pop("outdated", UNSET)

        error_response = d.pop("errorResponse", UNSET)

        input_set_response = cls(
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            pipeline_identifier=pipeline_identifier,
            identifier=identifier,
            input_set_yaml=input_set_yaml,
            name=name,
            description=description,
            tags=tags,
            is_outdated=is_outdated,
            is_error_response=is_error_response,
            input_set_error_wrapper=input_set_error_wrapper,
            git_details=git_details,
            entity_validity_details=entity_validity_details,
            outdated=outdated,
            error_response=error_response,
        )

        input_set_response.additional_properties = d
        return input_set_response

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

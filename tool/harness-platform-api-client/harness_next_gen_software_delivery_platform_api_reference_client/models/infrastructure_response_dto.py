from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.infrastructure_response_dto_deployment_type import (
    InfrastructureResponseDTODeploymentType,
    check_infrastructure_response_dto_deployment_type,
)
from ..models.infrastructure_response_dto_type import (
    InfrastructureResponseDTOType,
    check_infrastructure_response_dto_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.infrastructure_response_dto_tags import InfrastructureResponseDTOTags


T = TypeVar("T", bound="InfrastructureResponseDTO")


@_attrs_define
class InfrastructureResponseDTO:
    """This is the InfrastructureResponseDTO entity defined in Harness

    Attributes:
        account_id (str | Unset):
        identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_ref (str | Unset):
        name (str | Unset):
        description (str | Unset):
        tags (InfrastructureResponseDTOTags | Unset):
        type_ (InfrastructureResponseDTOType | Unset):
        deployment_type (InfrastructureResponseDTODeploymentType | Unset):
        yaml (str | Unset):
    """

    account_id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    environment_ref: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: InfrastructureResponseDTOTags | Unset = UNSET
    type_: InfrastructureResponseDTOType | Unset = UNSET
    deployment_type: InfrastructureResponseDTODeploymentType | Unset = UNSET
    yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        identifier = self.identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        environment_ref = self.environment_ref

        name = self.name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        deployment_type: str | Unset = UNSET
        if not isinstance(self.deployment_type, Unset):
            deployment_type = self.deployment_type

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if environment_ref is not UNSET:
            field_dict["environmentRef"] = environment_ref
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if deployment_type is not UNSET:
            field_dict["deploymentType"] = deployment_type
        if yaml is not UNSET:
            field_dict["yaml"] = yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.infrastructure_response_dto_tags import InfrastructureResponseDTOTags

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        identifier = d.pop("identifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        environment_ref = d.pop("environmentRef", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: InfrastructureResponseDTOTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = InfrastructureResponseDTOTags.from_dict(_tags)

        _type_ = d.pop("type", UNSET)
        type_: InfrastructureResponseDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_infrastructure_response_dto_type(_type_)

        _deployment_type = d.pop("deploymentType", UNSET)
        deployment_type: InfrastructureResponseDTODeploymentType | Unset
        if isinstance(_deployment_type, Unset):
            deployment_type = UNSET
        else:
            deployment_type = check_infrastructure_response_dto_deployment_type(_deployment_type)

        yaml = d.pop("yaml", UNSET)

        infrastructure_response_dto = cls(
            account_id=account_id,
            identifier=identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_ref=environment_ref,
            name=name,
            description=description,
            tags=tags,
            type_=type_,
            deployment_type=deployment_type,
            yaml=yaml,
        )

        infrastructure_response_dto.additional_properties = d
        return infrastructure_response_dto

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

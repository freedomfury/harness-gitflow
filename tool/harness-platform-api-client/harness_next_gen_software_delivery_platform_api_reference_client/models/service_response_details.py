from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_response_details_type import ServiceResponseDetailsType, check_service_response_details_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_response_details_tags import ServiceResponseDetailsTags


T = TypeVar("T", bound="ServiceResponseDetails")


@_attrs_define
class ServiceResponseDetails:
    """This is the Service entity defined in Harness

    Attributes:
        account_id (str | Unset):
        identifier (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        name (str | Unset):
        description (str | Unset):
        deleted (bool | Unset):
        tags (ServiceResponseDetailsTags | Unset):
        yaml (str | Unset):
        type_ (ServiceResponseDetailsType | Unset):
        git_ops_enabled (bool | Unset): Indicates if GitOps is enabled for this service
    """

    account_id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    tags: ServiceResponseDetailsTags | Unset = UNSET
    yaml: str | Unset = UNSET
    type_: ServiceResponseDetailsType | Unset = UNSET
    git_ops_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        identifier = self.identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        name = self.name

        description = self.description

        deleted = self.deleted

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        yaml = self.yaml

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        git_ops_enabled = self.git_ops_enabled

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
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if tags is not UNSET:
            field_dict["tags"] = tags
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if type_ is not UNSET:
            field_dict["type"] = type_
        if git_ops_enabled is not UNSET:
            field_dict["gitOpsEnabled"] = git_ops_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_response_details_tags import ServiceResponseDetailsTags

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        identifier = d.pop("identifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        deleted = d.pop("deleted", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ServiceResponseDetailsTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ServiceResponseDetailsTags.from_dict(_tags)

        yaml = d.pop("yaml", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceResponseDetailsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_service_response_details_type(_type_)

        git_ops_enabled = d.pop("gitOpsEnabled", UNSET)

        service_response_details = cls(
            account_id=account_id,
            identifier=identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            name=name,
            description=description,
            deleted=deleted,
            tags=tags,
            yaml=yaml,
            type_=type_,
            git_ops_enabled=git_ops_enabled,
        )

        service_response_details.additional_properties = d
        return service_response_details

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

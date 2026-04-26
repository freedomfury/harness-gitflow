from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_response_details_type import (
    EnvironmentResponseDetailsType,
    check_environment_response_details_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_response_details_tags import EnvironmentResponseDetailsTags


T = TypeVar("T", bound="EnvironmentResponseDetails")


@_attrs_define
class EnvironmentResponseDetails:
    """This is the Environment entity defined in Harness

    Attributes:
        account_id (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        identifier (str | Unset):
        name (str | Unset):
        description (str | Unset):
        color (str | Unset):
        type_ (EnvironmentResponseDetailsType | Unset):
        deleted (bool | Unset):
        tags (EnvironmentResponseDetailsTags | Unset):
        yaml (str | Unset):
    """

    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    color: str | Unset = UNSET
    type_: EnvironmentResponseDetailsType | Unset = UNSET
    deleted: bool | Unset = UNSET
    tags: EnvironmentResponseDetailsTags | Unset = UNSET
    yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        name = self.name

        description = self.description

        color = self.color

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        deleted = self.deleted

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if type_ is not UNSET:
            field_dict["type"] = type_
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if tags is not UNSET:
            field_dict["tags"] = tags
        if yaml is not UNSET:
            field_dict["yaml"] = yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_response_details_tags import EnvironmentResponseDetailsTags

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnvironmentResponseDetailsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_environment_response_details_type(_type_)

        deleted = d.pop("deleted", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: EnvironmentResponseDetailsTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = EnvironmentResponseDetailsTags.from_dict(_tags)

        yaml = d.pop("yaml", UNSET)

        environment_response_details = cls(
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            name=name,
            description=description,
            color=color,
            type_=type_,
            deleted=deleted,
            tags=tags,
            yaml=yaml,
        )

        environment_response_details.additional_properties = d
        return environment_response_details

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

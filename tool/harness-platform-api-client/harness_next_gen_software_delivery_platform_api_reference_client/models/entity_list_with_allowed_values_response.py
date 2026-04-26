from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_details import GitDetails


T = TypeVar("T", bound="EntityListWithAllowedValuesResponse")


@_attrs_define
class EntityListWithAllowedValuesResponse:
    """This is the list of entities which are using the allowedValues

    Attributes:
        account_id (str | Unset):
        project_identifier (str | Unset):
        org_identifier (str | Unset):
        identifier (str | Unset):
        entity_type (str | Unset):
        git_details (GitDetails | Unset):
    """

    account_id: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    entity_type: str | Unset = UNSET
    git_details: GitDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        identifier = self.identifier

        entity_type = self.entity_type

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_details import GitDetails

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        entity_type = d.pop("entityType", UNSET)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: GitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = GitDetails.from_dict(_git_details)

        entity_list_with_allowed_values_response = cls(
            account_id=account_id,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            identifier=identifier,
            entity_type=entity_type,
            git_details=git_details,
        )

        entity_list_with_allowed_values_response.additional_properties = d
        return entity_list_with_allowed_values_response

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

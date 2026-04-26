from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.environment_group_response_tags import EnvironmentGroupResponseTags
    from ..models.environment_response import EnvironmentResponse


T = TypeVar("T", bound="EnvironmentGroupResponse")


@_attrs_define
class EnvironmentGroupResponse:
    """This is the Environment Group Entity defined in Harness

    Attributes:
        account_id (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        identifier (str | Unset): Identifier for the Entity.
        name (str | Unset): Name of the Entity
        description (str | Unset): Description of the entity
        color (str | Unset): Color Code for the Entity
        deleted (bool | Unset): Deletion status for Entity
        tags (EnvironmentGroupResponseTags | Unset): Tags
        env_identifiers (list[str] | Unset): Environment Identifiers linked with Environment Group Identity
        env_response (list[EnvironmentResponse] | Unset): Info of Environments linked with Entity
        yaml (str | Unset): Yaml of the Environment Group
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
    """

    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    color: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    tags: EnvironmentGroupResponseTags | Unset = UNSET
    env_identifiers: list[str] | Unset = UNSET
    env_response: list[EnvironmentResponse] | Unset = UNSET
    yaml: str | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        name = self.name

        description = self.description

        color = self.color

        deleted = self.deleted

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        env_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.env_identifiers, Unset):
            env_identifiers = self.env_identifiers

        env_response: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.env_response, Unset):
            env_response = []
            for env_response_item_data in self.env_response:
                env_response_item = env_response_item_data.to_dict()
                env_response.append(env_response_item)

        yaml = self.yaml

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

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
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if tags is not UNSET:
            field_dict["tags"] = tags
        if env_identifiers is not UNSET:
            field_dict["envIdentifiers"] = env_identifiers
        if env_response is not UNSET:
            field_dict["envResponse"] = env_response
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.environment_group_response_tags import EnvironmentGroupResponseTags
        from ..models.environment_response import EnvironmentResponse

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        deleted = d.pop("deleted", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: EnvironmentGroupResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = EnvironmentGroupResponseTags.from_dict(_tags)

        env_identifiers = cast(list[str], d.pop("envIdentifiers", UNSET))

        _env_response = d.pop("envResponse", UNSET)
        env_response: list[EnvironmentResponse] | Unset = UNSET
        if _env_response is not UNSET:
            env_response = []
            for env_response_item_data in _env_response:
                env_response_item = EnvironmentResponse.from_dict(env_response_item_data)

                env_response.append(env_response_item)

        yaml = d.pop("yaml", UNSET)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        environment_group_response = cls(
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            name=name,
            description=description,
            color=color,
            deleted=deleted,
            tags=tags,
            env_identifiers=env_identifiers,
            env_response=env_response,
            yaml=yaml,
            git_details=git_details,
        )

        environment_group_response.additional_properties = d
        return environment_group_response

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

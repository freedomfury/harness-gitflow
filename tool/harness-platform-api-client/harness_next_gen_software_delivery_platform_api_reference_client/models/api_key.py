from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_api_key_type import ApiKeyApiKeyType, check_api_key_api_key_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_tags import ApiKeyTags
    from ..models.governance_metadata import GovernanceMetadata


T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """This has API Key details defined in Harness.

    Attributes:
        identifier (str): Identifier of the API Key
        name (str): Name of the API Key
        parent_identifier (str): Parent Entity Identifier of the API Key
        account_identifier (str): Account Identifier for the Entity.
        description (str | Unset): Description of the API Key
        tags (ApiKeyTags | Unset): Tags for the API Key
        api_key_type (ApiKeyApiKeyType | Unset): Type of the API Key
        default_time_to_expire_token (int | Unset): Default expiration time of the Token within API Key.
        project_identifier (str | Unset): Project Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    identifier: str
    name: str
    parent_identifier: str
    account_identifier: str
    description: str | Unset = UNSET
    tags: ApiKeyTags | Unset = UNSET
    api_key_type: ApiKeyApiKeyType | Unset = UNSET
    default_time_to_expire_token: int | Unset = UNSET
    project_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        parent_identifier = self.parent_identifier

        account_identifier = self.account_identifier

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        api_key_type: str | Unset = UNSET
        if not isinstance(self.api_key_type, Unset):
            api_key_type = self.api_key_type

        default_time_to_expire_token = self.default_time_to_expire_token

        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "parentIdentifier": parent_identifier,
                "accountIdentifier": account_identifier,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if api_key_type is not UNSET:
            field_dict["apiKeyType"] = api_key_type
        if default_time_to_expire_token is not UNSET:
            field_dict["defaultTimeToExpireToken"] = default_time_to_expire_token
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_tags import ApiKeyTags
        from ..models.governance_metadata import GovernanceMetadata

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        parent_identifier = d.pop("parentIdentifier")

        account_identifier = d.pop("accountIdentifier")

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ApiKeyTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ApiKeyTags.from_dict(_tags)

        _api_key_type = d.pop("apiKeyType", UNSET)
        api_key_type: ApiKeyApiKeyType | Unset
        if isinstance(_api_key_type, Unset):
            api_key_type = UNSET
        else:
            api_key_type = check_api_key_api_key_type(_api_key_type)

        default_time_to_expire_token = d.pop("defaultTimeToExpireToken", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        api_key = cls(
            identifier=identifier,
            name=name,
            parent_identifier=parent_identifier,
            account_identifier=account_identifier,
            description=description,
            tags=tags,
            api_key_type=api_key_type,
            default_time_to_expire_token=default_time_to_expire_token,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            governance_metadata=governance_metadata,
        )

        api_key.additional_properties = d
        return api_key

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

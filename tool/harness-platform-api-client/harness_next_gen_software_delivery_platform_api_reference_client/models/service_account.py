from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.service_account_tags import ServiceAccountTags


T = TypeVar("T", bound="ServiceAccount")


@_attrs_define
class ServiceAccount:
    """This has the details of Service Account in Harness.

    Attributes:
        identifier (str): Identifier of the Service Account.
        name (str): Name of the Service Account.
        email (str): Email of the Service Account.
        account_identifier (str): Account Identifier for the Entity.
        description (str | Unset): Description of the Service Account.
        tags (ServiceAccountTags | Unset): Tags of the Service Account.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    identifier: str
    name: str
    email: str
    account_identifier: str
    description: str | Unset = UNSET
    tags: ServiceAccountTags | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        email = self.email

        account_identifier = self.account_identifier

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "email": email,
                "accountIdentifier": account_identifier,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.service_account_tags import ServiceAccountTags

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        email = d.pop("email")

        account_identifier = d.pop("accountIdentifier")

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ServiceAccountTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ServiceAccountTags.from_dict(_tags)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        service_account = cls(
            identifier=identifier,
            name=name,
            email=email,
            account_identifier=account_identifier,
            description=description,
            tags=tags,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            governance_metadata=governance_metadata,
        )

        service_account.additional_properties = d
        return service_account

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

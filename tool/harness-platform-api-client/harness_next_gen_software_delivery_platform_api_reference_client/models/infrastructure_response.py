from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_details import EntityGitDetails
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.infrastructure_response_dto import InfrastructureResponseDTO


T = TypeVar("T", bound="InfrastructureResponse")


@_attrs_define
class InfrastructureResponse:
    """
    Attributes:
        infrastructure (InfrastructureResponseDTO | Unset): This is the InfrastructureResponseDTO entity defined in
            Harness
        created_at (int | Unset):
        last_modified_at (int | Unset):
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    infrastructure: InfrastructureResponseDTO | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        infrastructure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.infrastructure, Unset):
            infrastructure = self.infrastructure.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if infrastructure is not UNSET:
            field_dict["infrastructure"] = infrastructure
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_details import EntityGitDetails
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.infrastructure_response_dto import InfrastructureResponseDTO

        d = dict(src_dict)
        _infrastructure = d.pop("infrastructure", UNSET)
        infrastructure: InfrastructureResponseDTO | Unset
        if isinstance(_infrastructure, Unset):
            infrastructure = UNSET
        else:
            infrastructure = InfrastructureResponseDTO.from_dict(_infrastructure)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _entity_validity_details = d.pop("entityValidityDetails", UNSET)
        entity_validity_details: EntityGitDetails | Unset
        if isinstance(_entity_validity_details, Unset):
            entity_validity_details = UNSET
        else:
            entity_validity_details = EntityGitDetails.from_dict(_entity_validity_details)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        infrastructure_response = cls(
            infrastructure=infrastructure,
            created_at=created_at,
            last_modified_at=last_modified_at,
            entity_validity_details=entity_validity_details,
            governance_metadata=governance_metadata,
        )

        infrastructure_response.additional_properties = d
        return infrastructure_response

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

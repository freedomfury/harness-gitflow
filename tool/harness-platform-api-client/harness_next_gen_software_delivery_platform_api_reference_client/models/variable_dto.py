from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.variable_dto_type import VariableDTOType, check_variable_dto_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.variable_config_dto import VariableConfigDTO


T = TypeVar("T", bound="VariableDTO")


@_attrs_define
class VariableDTO:
    """
    Attributes:
        identifier (str): Identifier of the Variable.
        name (str): Name of the Variable.
        type_ (VariableDTOType): Type of the Variable.
        spec (VariableConfigDTO):
        description (str | Unset): Description of the entity
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    identifier: str
    name: str
    type_: VariableDTOType
    spec: VariableConfigDTO
    description: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        type_: str = self.type_

        spec = self.spec.to_dict()

        description = self.description

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
                "type": type_,
                "spec": spec,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.variable_config_dto import VariableConfigDTO

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        type_ = check_variable_dto_type(d.pop("type"))

        spec = VariableConfigDTO.from_dict(d.pop("spec"))

        description = d.pop("description", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        variable_dto = cls(
            identifier=identifier,
            name=name,
            type_=type_,
            spec=spec,
            description=description,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            governance_metadata=governance_metadata,
        )

        variable_dto.additional_properties = d
        return variable_dto

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

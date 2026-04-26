from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.governance_metadata import GovernanceMetadata


T = TypeVar("T", bound="ServiceOverrideResponse")


@_attrs_define
class ServiceOverrideResponse:
    """This is the Service Override Response entity defined in Harness

    Attributes:
        account_id (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        yaml (str | Unset):
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    environment_ref: str | Unset = UNSET
    service_ref: str | Unset = UNSET
    yaml: str | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        environment_ref = self.environment_ref

        service_ref = self.service_ref

        yaml = self.yaml

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if environment_ref is not UNSET:
            field_dict["environmentRef"] = environment_ref
        if service_ref is not UNSET:
            field_dict["serviceRef"] = service_ref
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.governance_metadata import GovernanceMetadata

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        environment_ref = d.pop("environmentRef", UNSET)

        service_ref = d.pop("serviceRef", UNSET)

        yaml = d.pop("yaml", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        service_override_response = cls(
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_ref=environment_ref,
            service_ref=service_ref,
            yaml=yaml,
            governance_metadata=governance_metadata,
        )

        service_override_response.additional_properties = d
        return service_override_response

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

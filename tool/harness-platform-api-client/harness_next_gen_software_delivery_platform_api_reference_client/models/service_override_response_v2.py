from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_override_response_v2_type import (
    ServiceOverrideResponseV2Type,
    check_service_override_response_v2_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.service_override_spec import ServiceOverrideSpec


T = TypeVar("T", bound="ServiceOverrideResponseV2")


@_attrs_define
class ServiceOverrideResponseV2:
    """This is the Service Override Response entity defined in Harness

    Attributes:
        identifier (str | Unset):
        account_id (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        environment_ref (str | Unset):
        service_ref (str | Unset):
        infra_identifier (str | Unset):
        cluster_identifier (str | Unset):
        type_ (ServiceOverrideResponseV2Type | Unset):
        spec (ServiceOverrideSpec | Unset): This is the Service Override Spec entity defined in Harness
        is_newly_created (bool | Unset):
        yaml (str | Unset):
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
        newly_created (bool | Unset):
    """

    identifier: str | Unset = UNSET
    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    environment_ref: str | Unset = UNSET
    service_ref: str | Unset = UNSET
    infra_identifier: str | Unset = UNSET
    cluster_identifier: str | Unset = UNSET
    type_: ServiceOverrideResponseV2Type | Unset = UNSET
    spec: ServiceOverrideSpec | Unset = UNSET
    is_newly_created: bool | Unset = UNSET
    yaml: str | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    newly_created: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        environment_ref = self.environment_ref

        service_ref = self.service_ref

        infra_identifier = self.infra_identifier

        cluster_identifier = self.cluster_identifier

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        is_newly_created = self.is_newly_created

        yaml = self.yaml

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        newly_created = self.newly_created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
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
        if infra_identifier is not UNSET:
            field_dict["infraIdentifier"] = infra_identifier
        if cluster_identifier is not UNSET:
            field_dict["clusterIdentifier"] = cluster_identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if spec is not UNSET:
            field_dict["spec"] = spec
        if is_newly_created is not UNSET:
            field_dict["isNewlyCreated"] = is_newly_created
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata
        if newly_created is not UNSET:
            field_dict["newlyCreated"] = newly_created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.service_override_spec import ServiceOverrideSpec

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        environment_ref = d.pop("environmentRef", UNSET)

        service_ref = d.pop("serviceRef", UNSET)

        infra_identifier = d.pop("infraIdentifier", UNSET)

        cluster_identifier = d.pop("clusterIdentifier", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceOverrideResponseV2Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_service_override_response_v2_type(_type_)

        _spec = d.pop("spec", UNSET)
        spec: ServiceOverrideSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = ServiceOverrideSpec.from_dict(_spec)

        is_newly_created = d.pop("isNewlyCreated", UNSET)

        yaml = d.pop("yaml", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        newly_created = d.pop("newlyCreated", UNSET)

        service_override_response_v2 = cls(
            identifier=identifier,
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_ref=environment_ref,
            service_ref=service_ref,
            infra_identifier=infra_identifier,
            cluster_identifier=cluster_identifier,
            type_=type_,
            spec=spec,
            is_newly_created=is_newly_created,
            yaml=yaml,
            governance_metadata=governance_metadata,
            newly_created=newly_created,
        )

        service_override_response_v2.additional_properties = d
        return service_override_response_v2

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_override_request_v2_type import (
    ServiceOverrideRequestV2Type,
    check_service_override_request_v2_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_override_spec import ServiceOverrideSpec


T = TypeVar("T", bound="ServiceOverrideRequestV2")


@_attrs_define
class ServiceOverrideRequestV2:
    """This is the Service Override Request entity defined in Harness

    Attributes:
        environment_ref (str): Environment Reference for the Entity.
        type_ (ServiceOverrideRequestV2Type): Type of the override which is based on source of overrides
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        service_ref (str | Unset): Service Reference for Entity
        infra_identifier (str | Unset): infraIdentifier
        cluster_identifier (str | Unset): clusterIdentifier
        spec (ServiceOverrideSpec | Unset): This is the Service Override Spec entity defined in Harness
        yaml (str | Unset):
        identifier (str | Unset): Service Overrides Identifier. Can be user-provided during creation; if omitted, auto-
            generated from environmentRef, serviceRef, and infraIdentifier based on override type.
    """

    environment_ref: str
    type_: ServiceOverrideRequestV2Type
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    service_ref: str | Unset = UNSET
    infra_identifier: str | Unset = UNSET
    cluster_identifier: str | Unset = UNSET
    spec: ServiceOverrideSpec | Unset = UNSET
    yaml: str | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_ref = self.environment_ref

        type_: str = self.type_

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        service_ref = self.service_ref

        infra_identifier = self.infra_identifier

        cluster_identifier = self.cluster_identifier

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        yaml = self.yaml

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentRef": environment_ref,
                "type": type_,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if service_ref is not UNSET:
            field_dict["serviceRef"] = service_ref
        if infra_identifier is not UNSET:
            field_dict["infraIdentifier"] = infra_identifier
        if cluster_identifier is not UNSET:
            field_dict["clusterIdentifier"] = cluster_identifier
        if spec is not UNSET:
            field_dict["spec"] = spec
        if yaml is not UNSET:
            field_dict["yaml"] = yaml
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_override_spec import ServiceOverrideSpec

        d = dict(src_dict)
        environment_ref = d.pop("environmentRef")

        type_ = check_service_override_request_v2_type(d.pop("type"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        service_ref = d.pop("serviceRef", UNSET)

        infra_identifier = d.pop("infraIdentifier", UNSET)

        cluster_identifier = d.pop("clusterIdentifier", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: ServiceOverrideSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = ServiceOverrideSpec.from_dict(_spec)

        yaml = d.pop("yaml", UNSET)

        identifier = d.pop("identifier", UNSET)

        service_override_request_v2 = cls(
            environment_ref=environment_ref,
            type_=type_,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            service_ref=service_ref,
            infra_identifier=infra_identifier,
            cluster_identifier=cluster_identifier,
            spec=spec,
            yaml=yaml,
            identifier=identifier,
        )

        service_override_request_v2.additional_properties = d
        return service_override_request_v2

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

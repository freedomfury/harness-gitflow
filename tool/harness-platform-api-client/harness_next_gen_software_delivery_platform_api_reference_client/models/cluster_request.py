from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_request_scope import ClusterRequestScope, check_cluster_request_scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterRequest")


@_attrs_define
class ClusterRequest:
    """This is the ClusterRequest entity defined in Harness

    Attributes:
        env_ref (str): environment identifier of the cluster
        identifier (str | Unset): identifier of the cluster
        org_identifier (str | Unset): organization identifier of the cluster
        agent_identifier (str | Unset): agent identifier of the cluster
        project_identifier (str | Unset): project identifier of the cluster
        scope (ClusterRequestScope | Unset): scope at which the cluster exists in harness gitops, project vs org vs
            account
    """

    env_ref: str
    identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    agent_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    scope: ClusterRequestScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_ref = self.env_ref

        identifier = self.identifier

        org_identifier = self.org_identifier

        agent_identifier = self.agent_identifier

        project_identifier = self.project_identifier

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "envRef": env_ref,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if agent_identifier is not UNSET:
            field_dict["agentIdentifier"] = agent_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        env_ref = d.pop("envRef")

        identifier = d.pop("identifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        agent_identifier = d.pop("agentIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ClusterRequestScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_cluster_request_scope(_scope)

        cluster_request = cls(
            env_ref=env_ref,
            identifier=identifier,
            org_identifier=org_identifier,
            agent_identifier=agent_identifier,
            project_identifier=project_identifier,
            scope=scope,
        )

        cluster_request.additional_properties = d
        return cluster_request

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

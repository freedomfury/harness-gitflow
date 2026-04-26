from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_response_scope import ClusterResponseScope, check_cluster_response_scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_response_tags import ClusterResponseTags


T = TypeVar("T", bound="ClusterResponse")


@_attrs_define
class ClusterResponse:
    """This is the ClusterRequest entity defined in Harness

    Attributes:
        env_ref (str): environment identifier of the cluster
        cluster_ref (str | Unset): identifier of the gitops cluster
        org_identifier (str | Unset): organization identifier of the cluster
        project_identifier (str | Unset): project identifier of the cluster
        agent_identifier (str | Unset): agent identifier of the cluster
        account_identifier (str | Unset): account identifier of the cluster
        linked_at (int | Unset): time at which the cluster was linked
        scope (ClusterResponseScope | Unset): scope at which the cluster exists in harness gitops, project vs org vs
            account
        name (str | Unset): name of the gitops cluster
        tags (ClusterResponseTags | Unset): name of the gitops cluster
    """

    env_ref: str
    cluster_ref: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    agent_identifier: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    linked_at: int | Unset = UNSET
    scope: ClusterResponseScope | Unset = UNSET
    name: str | Unset = UNSET
    tags: ClusterResponseTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_ref = self.env_ref

        cluster_ref = self.cluster_ref

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        agent_identifier = self.agent_identifier

        account_identifier = self.account_identifier

        linked_at = self.linked_at

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        name = self.name

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "envRef": env_ref,
            }
        )
        if cluster_ref is not UNSET:
            field_dict["clusterRef"] = cluster_ref
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if agent_identifier is not UNSET:
            field_dict["agentIdentifier"] = agent_identifier
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if linked_at is not UNSET:
            field_dict["linkedAt"] = linked_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_response_tags import ClusterResponseTags

        d = dict(src_dict)
        env_ref = d.pop("envRef")

        cluster_ref = d.pop("clusterRef", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        agent_identifier = d.pop("agentIdentifier", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        linked_at = d.pop("linkedAt", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ClusterResponseScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_cluster_response_scope(_scope)

        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ClusterResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ClusterResponseTags.from_dict(_tags)

        cluster_response = cls(
            env_ref=env_ref,
            cluster_ref=cluster_ref,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            agent_identifier=agent_identifier,
            account_identifier=account_identifier,
            linked_at=linked_at,
            scope=scope,
            name=name,
            tags=tags,
        )

        cluster_response.additional_properties = d
        return cluster_response

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

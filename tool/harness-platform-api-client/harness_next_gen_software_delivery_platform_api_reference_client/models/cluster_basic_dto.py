from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_basic_dto_scope import ClusterBasicDTOScope, check_cluster_basic_dto_scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterBasicDTO")


@_attrs_define
class ClusterBasicDTO:
    """List of cluster identifiers and names

    Attributes:
        identifier (str | Unset): identifier of the cluster
        agent_identifier (str | Unset): agent identifier of the cluster
        name (str | Unset): name of the cluster
        scope (ClusterBasicDTOScope | Unset): scope at which the cluster exists in harness gitops, project vs org vs
            account
    """

    identifier: str | Unset = UNSET
    agent_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    scope: ClusterBasicDTOScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        agent_identifier = self.agent_identifier

        name = self.name

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if agent_identifier is not UNSET:
            field_dict["agentIdentifier"] = agent_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        agent_identifier = d.pop("agentIdentifier", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ClusterBasicDTOScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_cluster_basic_dto_scope(_scope)

        cluster_basic_dto = cls(
            identifier=identifier,
            agent_identifier=agent_identifier,
            name=name,
            scope=scope,
        )

        cluster_basic_dto.additional_properties = d
        return cluster_basic_dto

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

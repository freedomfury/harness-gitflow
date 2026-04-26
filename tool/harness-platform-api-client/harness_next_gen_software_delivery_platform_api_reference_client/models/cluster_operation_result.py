from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterOperationResult")


@_attrs_define
class ClusterOperationResult:
    """Result of a cluster link/unlink operation with success or failure details

    Attributes:
        cluster_ref (str | Unset): Cluster reference with scope prefix. Format: 'account.<identifier>' for ACCOUNT
            scope, 'org.<identifier>' for ORGANIZATION scope, '<identifier>' for PROJECT scope.
        agent_identifier (str | Unset): Agent identifier
        name (str | Unset): Cluster name from GitOps service
        failure_reason (str | Unset): Failure reason (only present for failed operations)
        error_code (str | Unset): Error code (only present for failed operations)
    """

    cluster_ref: str | Unset = UNSET
    agent_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    failure_reason: str | Unset = UNSET
    error_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_ref = self.cluster_ref

        agent_identifier = self.agent_identifier

        name = self.name

        failure_reason = self.failure_reason

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_ref is not UNSET:
            field_dict["clusterRef"] = cluster_ref
        if agent_identifier is not UNSET:
            field_dict["agentIdentifier"] = agent_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_ref = d.pop("clusterRef", UNSET)

        agent_identifier = d.pop("agentIdentifier", UNSET)

        name = d.pop("name", UNSET)

        failure_reason = d.pop("failureReason", UNSET)

        error_code = d.pop("errorCode", UNSET)

        cluster_operation_result = cls(
            cluster_ref=cluster_ref,
            agent_identifier=agent_identifier,
            name=name,
            failure_reason=failure_reason,
            error_code=error_code,
        )

        cluster_operation_result.additional_properties = d
        return cluster_operation_result

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

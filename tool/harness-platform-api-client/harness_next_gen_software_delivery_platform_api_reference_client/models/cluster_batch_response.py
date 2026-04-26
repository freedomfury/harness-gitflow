from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_operation_result import ClusterOperationResult


T = TypeVar("T", bound="ClusterBatchResponse")


@_attrs_define
class ClusterBatchResponse:
    """This is the Cluster Batch Response defined in Harness

    Attributes:
        linked (int | Unset): number of clusters linked
        unlinked (int | Unset): number of clusters unlinked
        success (list[ClusterOperationResult] | Unset): List of successfully processed clusters
        failed (list[ClusterOperationResult] | Unset): List of failed cluster operations with reasons
    """

    linked: int | Unset = UNSET
    unlinked: int | Unset = UNSET
    success: list[ClusterOperationResult] | Unset = UNSET
    failed: list[ClusterOperationResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linked = self.linked

        unlinked = self.unlinked

        success: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.success, Unset):
            success = []
            for success_item_data in self.success:
                success_item = success_item_data.to_dict()
                success.append(success_item)

        failed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item = failed_item_data.to_dict()
                failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linked is not UNSET:
            field_dict["linked"] = linked
        if unlinked is not UNSET:
            field_dict["unlinked"] = unlinked
        if success is not UNSET:
            field_dict["success"] = success
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_operation_result import ClusterOperationResult

        d = dict(src_dict)
        linked = d.pop("linked", UNSET)

        unlinked = d.pop("unlinked", UNSET)

        _success = d.pop("success", UNSET)
        success: list[ClusterOperationResult] | Unset = UNSET
        if _success is not UNSET:
            success = []
            for success_item_data in _success:
                success_item = ClusterOperationResult.from_dict(success_item_data)

                success.append(success_item)

        _failed = d.pop("failed", UNSET)
        failed: list[ClusterOperationResult] | Unset = UNSET
        if _failed is not UNSET:
            failed = []
            for failed_item_data in _failed:
                failed_item = ClusterOperationResult.from_dict(failed_item_data)

                failed.append(failed_item)

        cluster_batch_response = cls(
            linked=linked,
            unlinked=unlinked,
            success=success,
            failed=failed,
        )

        cluster_batch_response.additional_properties = d
        return cluster_batch_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineCount")


@_attrs_define
class PipelineCount:
    """This is the view of the Pipeline Execution Count Info for a particular Date

    Attributes:
        total (int | Unset):
        success (int | Unset):
        failure (int | Unset):
        expired (int | Unset):
        aborted (int | Unset):
    """

    total: int | Unset = UNSET
    success: int | Unset = UNSET
    failure: int | Unset = UNSET
    expired: int | Unset = UNSET
    aborted: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        success = self.success

        failure = self.failure

        expired = self.expired

        aborted = self.aborted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if success is not UNSET:
            field_dict["success"] = success
        if failure is not UNSET:
            field_dict["failure"] = failure
        if expired is not UNSET:
            field_dict["expired"] = expired
        if aborted is not UNSET:
            field_dict["aborted"] = aborted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        success = d.pop("success", UNSET)

        failure = d.pop("failure", UNSET)

        expired = d.pop("expired", UNSET)

        aborted = d.pop("aborted", UNSET)

        pipeline_count = cls(
            total=total,
            success=success,
            failure=failure,
            expired=expired,
            aborted=aborted,
        )

        pipeline_count.additional_properties = d
        return pipeline_count

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

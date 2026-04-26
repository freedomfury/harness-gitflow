from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiReviewerAddPullReqRequest")


@_attrs_define
class OpenapiReviewerAddPullReqRequest:
    """
    Attributes:
        reviewer_id (int | Unset):
    """

    reviewer_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviewer_id = self.reviewer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reviewer_id is not UNSET:
            field_dict["reviewer_id"] = reviewer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reviewer_id = d.pop("reviewer_id", UNSET)

        openapi_reviewer_add_pull_req_request = cls(
            reviewer_id=reviewer_id,
        )

        openapi_reviewer_add_pull_req_request.additional_properties = d
        return openapi_reviewer_add_pull_req_request

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

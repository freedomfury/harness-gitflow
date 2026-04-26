from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiUserGroupReviewerAddRequest")


@_attrs_define
class OpenapiUserGroupReviewerAddRequest:
    """
    Attributes:
        usergroup_id (int | Unset):
    """

    usergroup_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usergroup_id = self.usergroup_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usergroup_id is not UNSET:
            field_dict["usergroup_id"] = usergroup_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usergroup_id = d.pop("usergroup_id", UNSET)

        openapi_user_group_reviewer_add_request = cls(
            usergroup_id=usergroup_id,
        )

        openapi_user_group_reviewer_add_request.additional_properties = d
        return openapi_user_group_reviewer_add_request

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

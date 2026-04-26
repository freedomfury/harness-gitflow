from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefReviewers")


@_attrs_define
class ProtectionDefReviewers:
    """
    Attributes:
        default_reviewer_ids (list[int] | Unset):
        default_user_group_reviewer_ids (list[int] | Unset):
        request_code_owners (bool | Unset):
    """

    default_reviewer_ids: list[int] | Unset = UNSET
    default_user_group_reviewer_ids: list[int] | Unset = UNSET
    request_code_owners: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_reviewer_ids: list[int] | Unset = UNSET
        if not isinstance(self.default_reviewer_ids, Unset):
            default_reviewer_ids = self.default_reviewer_ids

        default_user_group_reviewer_ids: list[int] | Unset = UNSET
        if not isinstance(self.default_user_group_reviewer_ids, Unset):
            default_user_group_reviewer_ids = self.default_user_group_reviewer_ids

        request_code_owners = self.request_code_owners

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_reviewer_ids is not UNSET:
            field_dict["default_reviewer_ids"] = default_reviewer_ids
        if default_user_group_reviewer_ids is not UNSET:
            field_dict["default_user_group_reviewer_ids"] = default_user_group_reviewer_ids
        if request_code_owners is not UNSET:
            field_dict["request_code_owners"] = request_code_owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_reviewer_ids = cast(list[int], d.pop("default_reviewer_ids", UNSET))

        default_user_group_reviewer_ids = cast(list[int], d.pop("default_user_group_reviewer_ids", UNSET))

        request_code_owners = d.pop("request_code_owners", UNSET)

        protection_def_reviewers = cls(
            default_reviewer_ids=default_reviewer_ids,
            default_user_group_reviewer_ids=default_user_group_reviewer_ids,
            request_code_owners=request_code_owners,
        )

        protection_def_reviewers.additional_properties = d
        return protection_def_reviewers

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

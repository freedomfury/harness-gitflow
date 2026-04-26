from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPullReqActivitySuggestionsMetadata")


@_attrs_define
class TypesPullReqActivitySuggestionsMetadata:
    """
    Attributes:
        applied_check_sum (str | Unset):
        applied_commit_sha (str | Unset):
        check_sums (list[str] | Unset):
    """

    applied_check_sum: str | Unset = UNSET
    applied_commit_sha: str | Unset = UNSET
    check_sums: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_check_sum = self.applied_check_sum

        applied_commit_sha = self.applied_commit_sha

        check_sums: list[str] | Unset = UNSET
        if not isinstance(self.check_sums, Unset):
            check_sums = self.check_sums

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_check_sum is not UNSET:
            field_dict["applied_check_sum"] = applied_check_sum
        if applied_commit_sha is not UNSET:
            field_dict["applied_commit_sha"] = applied_commit_sha
        if check_sums is not UNSET:
            field_dict["check_sums"] = check_sums

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied_check_sum = d.pop("applied_check_sum", UNSET)

        applied_commit_sha = d.pop("applied_commit_sha", UNSET)

        check_sums = cast(list[str], d.pop("check_sums", UNSET))

        types_pull_req_activity_suggestions_metadata = cls(
            applied_check_sum=applied_check_sum,
            applied_commit_sha=applied_commit_sha,
            check_sums=check_sums,
        )

        types_pull_req_activity_suggestions_metadata.additional_properties = d
        return types_pull_req_activity_suggestions_metadata

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

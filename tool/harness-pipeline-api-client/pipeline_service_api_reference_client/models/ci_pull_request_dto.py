from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CIPullRequestDTO")


@_attrs_define
class CIPullRequestDTO:
    """
    Attributes:
        source_branch (str | Unset):
        target_branch (str | Unset):
    """

    source_branch: str | Unset = UNSET
    target_branch: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_branch = self.source_branch

        target_branch = self.target_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_branch is not UNSET:
            field_dict["sourceBranch"] = source_branch
        if target_branch is not UNSET:
            field_dict["targetBranch"] = target_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_branch = d.pop("sourceBranch", UNSET)

        target_branch = d.pop("targetBranch", UNSET)

        ci_pull_request_dto = cls(
            source_branch=source_branch,
            target_branch=target_branch,
        )

        ci_pull_request_dto.additional_properties = d
        return ci_pull_request_dto

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

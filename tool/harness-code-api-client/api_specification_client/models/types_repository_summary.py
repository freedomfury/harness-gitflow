from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_repository_pull_req_summary import TypesRepositoryPullReqSummary


T = TypeVar("T", bound="TypesRepositorySummary")


@_attrs_define
class TypesRepositorySummary:
    """
    Attributes:
        branch_count (int | Unset):
        default_branch_commit_count (int | Unset):
        pull_req_summary (TypesRepositoryPullReqSummary | Unset):
        tag_count (int | Unset):
    """

    branch_count: int | Unset = UNSET
    default_branch_commit_count: int | Unset = UNSET
    pull_req_summary: TypesRepositoryPullReqSummary | Unset = UNSET
    tag_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_count = self.branch_count

        default_branch_commit_count = self.default_branch_commit_count

        pull_req_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pull_req_summary, Unset):
            pull_req_summary = self.pull_req_summary.to_dict()

        tag_count = self.tag_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_count is not UNSET:
            field_dict["branch_count"] = branch_count
        if default_branch_commit_count is not UNSET:
            field_dict["default_branch_commit_count"] = default_branch_commit_count
        if pull_req_summary is not UNSET:
            field_dict["pull_req_summary"] = pull_req_summary
        if tag_count is not UNSET:
            field_dict["tag_count"] = tag_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_repository_pull_req_summary import TypesRepositoryPullReqSummary

        d = dict(src_dict)
        branch_count = d.pop("branch_count", UNSET)

        default_branch_commit_count = d.pop("default_branch_commit_count", UNSET)

        _pull_req_summary = d.pop("pull_req_summary", UNSET)
        pull_req_summary: TypesRepositoryPullReqSummary | Unset
        if isinstance(_pull_req_summary, Unset):
            pull_req_summary = UNSET
        else:
            pull_req_summary = TypesRepositoryPullReqSummary.from_dict(_pull_req_summary)

        tag_count = d.pop("tag_count", UNSET)

        types_repository_summary = cls(
            branch_count=branch_count,
            default_branch_commit_count=default_branch_commit_count,
            pull_req_summary=pull_req_summary,
            tag_count=tag_count,
        )

        types_repository_summary.additional_properties = d
        return types_repository_summary

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

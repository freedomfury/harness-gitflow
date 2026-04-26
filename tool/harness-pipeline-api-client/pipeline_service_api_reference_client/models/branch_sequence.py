from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchSequence")


@_attrs_define
class BranchSequence:
    """Branch-scoped build sequence information

    Attributes:
        normalized_repo_url (str | Unset): The normalized repository URL (e.g., github.com/org/repo)
        branch (str | Unset): The branch name
        sequence_id (int | Unset): The current sequence ID for this branch
        created_at (int | Unset): Timestamp when this branch sequence was first created
        last_updated_at (int | Unset): Timestamp when this branch sequence was last updated
    """

    normalized_repo_url: str | Unset = UNSET
    branch: str | Unset = UNSET
    sequence_id: int | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        normalized_repo_url = self.normalized_repo_url

        branch = self.branch

        sequence_id = self.sequence_id

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if normalized_repo_url is not UNSET:
            field_dict["normalizedRepoUrl"] = normalized_repo_url
        if branch is not UNSET:
            field_dict["branch"] = branch
        if sequence_id is not UNSET:
            field_dict["sequenceId"] = sequence_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        normalized_repo_url = d.pop("normalizedRepoUrl", UNSET)

        branch = d.pop("branch", UNSET)

        sequence_id = d.pop("sequenceId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        branch_sequence = cls(
            normalized_repo_url=normalized_repo_url,
            branch=branch,
            sequence_id=sequence_id,
            created_at=created_at,
            last_updated_at=last_updated_at,
        )

        branch_sequence.additional_properties = d
        return branch_sequence

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

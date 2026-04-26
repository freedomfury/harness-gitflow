from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_commit_file_stats import GitCommitFileStats
    from ..models.git_signature import GitSignature


T = TypeVar("T", bound="GitCommitType0")


@_attrs_define
class GitCommitType0:
    """
    Attributes:
        author (GitSignature | Unset):
        committer (GitSignature | Unset):
        file_stats (list[GitCommitFileStats] | Unset):
        message (str | Unset):
        parent_shas (list[str] | Unset):
        sha (str | Unset): Git object hash
        title (str | Unset):
    """

    author: GitSignature | Unset = UNSET
    committer: GitSignature | Unset = UNSET
    file_stats: list[GitCommitFileStats] | Unset = UNSET
    message: str | Unset = UNSET
    parent_shas: list[str] | Unset = UNSET
    sha: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        file_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_stats, Unset):
            file_stats = []
            for file_stats_item_data in self.file_stats:
                file_stats_item = file_stats_item_data.to_dict()
                file_stats.append(file_stats_item)

        message = self.message

        parent_shas: list[str] | Unset = UNSET
        if not isinstance(self.parent_shas, Unset):
            parent_shas = self.parent_shas

        sha = self.sha

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if file_stats is not UNSET:
            field_dict["file_stats"] = file_stats
        if message is not UNSET:
            field_dict["message"] = message
        if parent_shas is not UNSET:
            field_dict["parent_shas"] = parent_shas
        if sha is not UNSET:
            field_dict["sha"] = sha
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_commit_file_stats import GitCommitFileStats
        from ..models.git_signature import GitSignature

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: GitSignature | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = GitSignature.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: GitSignature | Unset
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = GitSignature.from_dict(_committer)

        _file_stats = d.pop("file_stats", UNSET)
        file_stats: list[GitCommitFileStats] | Unset = UNSET
        if _file_stats is not UNSET:
            file_stats = []
            for file_stats_item_data in _file_stats:
                file_stats_item = GitCommitFileStats.from_dict(file_stats_item_data)

                file_stats.append(file_stats_item)

        message = d.pop("message", UNSET)

        parent_shas = cast(list[str], d.pop("parent_shas", UNSET))

        sha = d.pop("sha", UNSET)

        title = d.pop("title", UNSET)

        git_commit_type_0 = cls(
            author=author,
            committer=committer,
            file_stats=file_stats,
            message=message,
            parent_shas=parent_shas,
            sha=sha,
            title=title,
        )

        git_commit_type_0.additional_properties = d
        return git_commit_type_0

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

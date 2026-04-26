from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_blame_part_previous import GitBlamePartPrevious
    from ..models.git_commit_type_0 import GitCommitType0


T = TypeVar("T", bound="GitBlamePart")


@_attrs_define
class GitBlamePart:
    """
    Attributes:
        commit (GitCommitType0 | None | Unset):
        lines (list[str] | None | Unset):
        previous (GitBlamePartPrevious | Unset):
    """

    commit: GitCommitType0 | None | Unset = UNSET
    lines: list[str] | None | Unset = UNSET
    previous: GitBlamePartPrevious | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.git_commit_type_0 import GitCommitType0

        commit: dict[str, Any] | None | Unset
        if isinstance(self.commit, Unset):
            commit = UNSET
        elif isinstance(self.commit, GitCommitType0):
            commit = self.commit.to_dict()
        else:
            commit = self.commit

        lines: list[str] | None | Unset
        if isinstance(self.lines, Unset):
            lines = UNSET
        elif isinstance(self.lines, list):
            lines = self.lines

        else:
            lines = self.lines

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if lines is not UNSET:
            field_dict["lines"] = lines
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_blame_part_previous import GitBlamePartPrevious
        from ..models.git_commit_type_0 import GitCommitType0

        d = dict(src_dict)

        def _parse_commit(data: object) -> GitCommitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_commit_type_0 = GitCommitType0.from_dict(data)

                return componentsschemas_git_commit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GitCommitType0 | None | Unset, data)

        commit = _parse_commit(d.pop("commit", UNSET))

        def _parse_lines(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lines_type_0 = cast(list[str], data)

                return lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        lines = _parse_lines(d.pop("lines", UNSET))

        _previous = d.pop("previous", UNSET)
        previous: GitBlamePartPrevious | Unset
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = GitBlamePartPrevious.from_dict(_previous)

        git_blame_part = cls(
            commit=commit,
            lines=lines,
            previous=previous,
        )

        git_blame_part.additional_properties = d
        return git_blame_part

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

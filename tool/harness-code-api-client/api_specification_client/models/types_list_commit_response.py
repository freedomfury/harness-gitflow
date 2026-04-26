from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit import TypesCommit
    from ..models.types_rename_details import TypesRenameDetails


T = TypeVar("T", bound="TypesListCommitResponse")


@_attrs_define
class TypesListCommitResponse:
    """
    Attributes:
        commits (list[TypesCommit] | None | Unset):
        rename_details (list[TypesRenameDetails] | None | Unset):
        total_commits (int | Unset):
    """

    commits: list[TypesCommit] | None | Unset = UNSET
    rename_details: list[TypesRenameDetails] | None | Unset = UNSET
    total_commits: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commits: list[dict[str, Any]] | None | Unset
        if isinstance(self.commits, Unset):
            commits = UNSET
        elif isinstance(self.commits, list):
            commits = []
            for commits_type_0_item_data in self.commits:
                commits_type_0_item = commits_type_0_item_data.to_dict()
                commits.append(commits_type_0_item)

        else:
            commits = self.commits

        rename_details: list[dict[str, Any]] | None | Unset
        if isinstance(self.rename_details, Unset):
            rename_details = UNSET
        elif isinstance(self.rename_details, list):
            rename_details = []
            for rename_details_type_0_item_data in self.rename_details:
                rename_details_type_0_item = rename_details_type_0_item_data.to_dict()
                rename_details.append(rename_details_type_0_item)

        else:
            rename_details = self.rename_details

        total_commits = self.total_commits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commits is not UNSET:
            field_dict["commits"] = commits
        if rename_details is not UNSET:
            field_dict["rename_details"] = rename_details
        if total_commits is not UNSET:
            field_dict["total_commits"] = total_commits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit import TypesCommit
        from ..models.types_rename_details import TypesRenameDetails

        d = dict(src_dict)

        def _parse_commits(data: object) -> list[TypesCommit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                commits_type_0 = []
                _commits_type_0 = data
                for commits_type_0_item_data in _commits_type_0:
                    commits_type_0_item = TypesCommit.from_dict(commits_type_0_item_data)

                    commits_type_0.append(commits_type_0_item)

                return commits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesCommit] | None | Unset, data)

        commits = _parse_commits(d.pop("commits", UNSET))

        def _parse_rename_details(data: object) -> list[TypesRenameDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rename_details_type_0 = []
                _rename_details_type_0 = data
                for rename_details_type_0_item_data in _rename_details_type_0:
                    rename_details_type_0_item = TypesRenameDetails.from_dict(rename_details_type_0_item_data)

                    rename_details_type_0.append(rename_details_type_0_item)

                return rename_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesRenameDetails] | None | Unset, data)

        rename_details = _parse_rename_details(d.pop("rename_details", UNSET))

        total_commits = d.pop("total_commits", UNSET)

        types_list_commit_response = cls(
            commits=commits,
            rename_details=rename_details,
            total_commits=total_commits,
        )

        types_list_commit_response.additional_properties = d
        return types_list_commit_response

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

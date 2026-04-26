from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit import TypesCommit


T = TypeVar("T", bound="TypesRevertResponse")


@_attrs_define
class TypesRevertResponse:
    """
    Attributes:
        branch (str | Unset):
        commit (TypesCommit | Unset):
    """

    branch: str | Unset = UNSET
    commit: TypesCommit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if commit is not UNSET:
            field_dict["commit"] = commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit import TypesCommit

        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        _commit = d.pop("commit", UNSET)
        commit: TypesCommit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = TypesCommit.from_dict(_commit)

        types_revert_response = cls(
            branch=branch,
            commit=commit,
        )

        types_revert_response.additional_properties = d
        return types_revert_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hook_reference_update import HookReferenceUpdate


T = TypeVar("T", bound="RepoLinkedSyncOutput")


@_attrs_define
class RepoLinkedSyncOutput:
    """
    Attributes:
        branches (list[HookReferenceUpdate] | None | Unset):
    """

    branches: list[HookReferenceUpdate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches: list[dict[str, Any]] | None | Unset
        if isinstance(self.branches, Unset):
            branches = UNSET
        elif isinstance(self.branches, list):
            branches = []
            for branches_type_0_item_data in self.branches:
                branches_type_0_item = branches_type_0_item_data.to_dict()
                branches.append(branches_type_0_item)

        else:
            branches = self.branches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branches is not UNSET:
            field_dict["branches"] = branches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_reference_update import HookReferenceUpdate

        d = dict(src_dict)

        def _parse_branches(data: object) -> list[HookReferenceUpdate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                branches_type_0 = []
                _branches_type_0 = data
                for branches_type_0_item_data in _branches_type_0:
                    branches_type_0_item = HookReferenceUpdate.from_dict(branches_type_0_item_data)

                    branches_type_0.append(branches_type_0_item)

                return branches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HookReferenceUpdate] | None | Unset, data)

        branches = _parse_branches(d.pop("branches", UNSET))

        repo_linked_sync_output = cls(
            branches=branches,
        )

        repo_linked_sync_output.additional_properties = d
        return repo_linked_sync_output

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

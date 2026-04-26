from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_assignment_metadata import RoleAssignmentMetadata
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="UserAggregate")


@_attrs_define
class UserAggregate:
    """Returns User's metadata and Role Assignments metadata

    Attributes:
        user (UserMetadata | Unset): This is the view of the UserMetadata entity defined in Harness
        role_assignment_metadata (list[RoleAssignmentMetadata] | Unset):
    """

    user: UserMetadata | Unset = UNSET
    role_assignment_metadata: list[RoleAssignmentMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        role_assignment_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_assignment_metadata, Unset):
            role_assignment_metadata = []
            for role_assignment_metadata_item_data in self.role_assignment_metadata:
                role_assignment_metadata_item = role_assignment_metadata_item_data.to_dict()
                role_assignment_metadata.append(role_assignment_metadata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if role_assignment_metadata is not UNSET:
            field_dict["roleAssignmentMetadata"] = role_assignment_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_assignment_metadata import RoleAssignmentMetadata
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: UserMetadata | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserMetadata.from_dict(_user)

        _role_assignment_metadata = d.pop("roleAssignmentMetadata", UNSET)
        role_assignment_metadata: list[RoleAssignmentMetadata] | Unset = UNSET
        if _role_assignment_metadata is not UNSET:
            role_assignment_metadata = []
            for role_assignment_metadata_item_data in _role_assignment_metadata:
                role_assignment_metadata_item = RoleAssignmentMetadata.from_dict(role_assignment_metadata_item_data)

                role_assignment_metadata.append(role_assignment_metadata_item)

        user_aggregate = cls(
            user=user,
            role_assignment_metadata=role_assignment_metadata,
        )

        user_aggregate.additional_properties = d
        return user_aggregate

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

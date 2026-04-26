from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_group_response import EnvironmentGroupResponse


T = TypeVar("T", bound="EnvironmentGroup")


@_attrs_define
class EnvironmentGroup:
    """This is the view of Environment Group Entity defined in Harness

    Attributes:
        env_group (EnvironmentGroupResponse | Unset): This is the Environment Group Entity defined in Harness
        created_at (int | Unset): Time at which the entity was created
        last_modified_at (int | Unset): Time at which the entity was last updated
    """

    env_group: EnvironmentGroupResponse | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_group, Unset):
            env_group = self.env_group.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env_group is not UNSET:
            field_dict["envGroup"] = env_group
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_group_response import EnvironmentGroupResponse

        d = dict(src_dict)
        _env_group = d.pop("envGroup", UNSET)
        env_group: EnvironmentGroupResponse | Unset
        if isinstance(_env_group, Unset):
            env_group = UNSET
        else:
            env_group = EnvironmentGroupResponse.from_dict(_env_group)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        environment_group = cls(
            env_group=env_group,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

        environment_group.additional_properties = d
        return environment_group

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

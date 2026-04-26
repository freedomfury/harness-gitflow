from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_users_response_add_user_response_map import AddUsersResponseAddUserResponseMap


T = TypeVar("T", bound="AddUsersResponse")


@_attrs_define
class AddUsersResponse:
    """
    Attributes:
        add_user_response_map (AddUsersResponseAddUserResponseMap | Unset):
    """

    add_user_response_map: AddUsersResponseAddUserResponseMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_user_response_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_user_response_map, Unset):
            add_user_response_map = self.add_user_response_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_user_response_map is not UNSET:
            field_dict["addUserResponseMap"] = add_user_response_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_users_response_add_user_response_map import AddUsersResponseAddUserResponseMap

        d = dict(src_dict)
        _add_user_response_map = d.pop("addUserResponseMap", UNSET)
        add_user_response_map: AddUsersResponseAddUserResponseMap | Unset
        if isinstance(_add_user_response_map, Unset):
            add_user_response_map = UNSET
        else:
            add_user_response_map = AddUsersResponseAddUserResponseMap.from_dict(_add_user_response_map)

        add_users_response = cls(
            add_user_response_map=add_user_response_map,
        )

        add_users_response.additional_properties = d
        return add_users_response

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

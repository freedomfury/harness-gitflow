from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category


T = TypeVar("T", bound="CannyCategoriesResponse")


@_attrs_define
class CannyCategoriesResponse:
    """Contains list of Categories and their ID's from Canny for a given board

    Attributes:
        board_id (str | Unset):
        category_list (list[Category] | Unset):
    """

    board_id: str | Unset = UNSET
    category_list: list[Category] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        category_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category_list, Unset):
            category_list = []
            for category_list_item_data in self.category_list:
                category_list_item = category_list_item_data.to_dict()
                category_list.append(category_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if category_list is not UNSET:
            field_dict["categoryList"] = category_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category

        d = dict(src_dict)
        board_id = d.pop("boardId", UNSET)

        _category_list = d.pop("categoryList", UNSET)
        category_list: list[Category] | Unset = UNSET
        if _category_list is not UNSET:
            category_list = []
            for category_list_item_data in _category_list:
                category_list_item = Category.from_dict(category_list_item_data)

                category_list.append(category_list_item)

        canny_categories_response = cls(
            board_id=board_id,
            category_list=category_list,
        )

        canny_categories_response.additional_properties = d
        return canny_categories_response

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

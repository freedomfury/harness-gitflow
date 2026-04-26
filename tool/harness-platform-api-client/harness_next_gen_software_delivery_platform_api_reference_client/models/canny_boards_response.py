from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board import Board


T = TypeVar("T", bound="CannyBoardsResponse")


@_attrs_define
class CannyBoardsResponse:
    """Contains list of Boards and their ID's from Canny

    Attributes:
        message (str | Unset):
        boards (list[Board] | Unset):
    """

    message: str | Unset = UNSET
    boards: list[Board] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        boards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.boards, Unset):
            boards = []
            for boards_item_data in self.boards:
                boards_item = boards_item_data.to_dict()
                boards.append(boards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if boards is not UNSET:
            field_dict["boards"] = boards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board import Board

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _boards = d.pop("boards", UNSET)
        boards: list[Board] | Unset = UNSET
        if _boards is not UNSET:
            boards = []
            for boards_item_data in _boards:
                boards_item = Board.from_dict(boards_item_data)

                boards.append(boards_item)

        canny_boards_response = cls(
            message=message,
            boards=boards,
        )

        canny_boards_response.additional_properties = d
        return canny_boards_response

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

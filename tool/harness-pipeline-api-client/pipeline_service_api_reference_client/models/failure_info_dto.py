from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_info_dto_failure_type_list_item import (
    FailureInfoDTOFailureTypeListItem,
    check_failure_info_dto_failure_type_list_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_message import ResponseMessage


T = TypeVar("T", bound="FailureInfoDTO")


@_attrs_define
class FailureInfoDTO:
    """
    Attributes:
        message (str | Unset):
        failure_type_list (list[FailureInfoDTOFailureTypeListItem] | Unset):
        response_messages (list[ResponseMessage] | Unset):
    """

    message: str | Unset = UNSET
    failure_type_list: list[FailureInfoDTOFailureTypeListItem] | Unset = UNSET
    response_messages: list[ResponseMessage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        failure_type_list: list[str] | Unset = UNSET
        if not isinstance(self.failure_type_list, Unset):
            failure_type_list = []
            for failure_type_list_item_data in self.failure_type_list:
                failure_type_list_item: str = failure_type_list_item_data
                failure_type_list.append(failure_type_list_item)

        response_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.response_messages, Unset):
            response_messages = []
            for response_messages_item_data in self.response_messages:
                response_messages_item = response_messages_item_data.to_dict()
                response_messages.append(response_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if failure_type_list is not UNSET:
            field_dict["failureTypeList"] = failure_type_list
        if response_messages is not UNSET:
            field_dict["responseMessages"] = response_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_message import ResponseMessage

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _failure_type_list = d.pop("failureTypeList", UNSET)
        failure_type_list: list[FailureInfoDTOFailureTypeListItem] | Unset = UNSET
        if _failure_type_list is not UNSET:
            failure_type_list = []
            for failure_type_list_item_data in _failure_type_list:
                failure_type_list_item = check_failure_info_dto_failure_type_list_item(failure_type_list_item_data)

                failure_type_list.append(failure_type_list_item)

        _response_messages = d.pop("responseMessages", UNSET)
        response_messages: list[ResponseMessage] | Unset = UNSET
        if _response_messages is not UNSET:
            response_messages = []
            for response_messages_item_data in _response_messages:
                response_messages_item = ResponseMessage.from_dict(response_messages_item_data)

                response_messages.append(response_messages_item)

        failure_info_dto = cls(
            message=message,
            failure_type_list=failure_type_list,
            response_messages=response_messages,
        )

        failure_info_dto.additional_properties = d
        return failure_info_dto

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

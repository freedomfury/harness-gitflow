from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_message_code import ResponseMessageCode, check_response_message_code
from ..models.response_message_failure_sub_types_item import (
    ResponseMessageFailureSubTypesItem,
    check_response_message_failure_sub_types_item,
)
from ..models.response_message_failure_types_item import (
    ResponseMessageFailureTypesItem,
    check_response_message_failure_types_item,
)
from ..models.response_message_level import ResponseMessageLevel, check_response_message_level
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_message_additional_info import ResponseMessageAdditionalInfo
    from ..models.response_message_exception import ResponseMessageException


T = TypeVar("T", bound="ResponseMessage")


@_attrs_define
class ResponseMessage:
    """
    Attributes:
        code (ResponseMessageCode | Unset):
        level (ResponseMessageLevel | Unset):
        message (str | Unset):
        exception (ResponseMessageException | Unset):
        failure_types (list[ResponseMessageFailureTypesItem] | Unset):
        failure_sub_types (list[ResponseMessageFailureSubTypesItem] | Unset):
        additional_info (ResponseMessageAdditionalInfo | Unset):
    """

    code: ResponseMessageCode | Unset = UNSET
    level: ResponseMessageLevel | Unset = UNSET
    message: str | Unset = UNSET
    exception: ResponseMessageException | Unset = UNSET
    failure_types: list[ResponseMessageFailureTypesItem] | Unset = UNSET
    failure_sub_types: list[ResponseMessageFailureSubTypesItem] | Unset = UNSET
    additional_info: ResponseMessageAdditionalInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level

        message = self.message

        exception: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exception, Unset):
            exception = self.exception.to_dict()

        failure_types: list[str] | Unset = UNSET
        if not isinstance(self.failure_types, Unset):
            failure_types = []
            for failure_types_item_data in self.failure_types:
                failure_types_item: str = failure_types_item_data
                failure_types.append(failure_types_item)

        failure_sub_types: list[str] | Unset = UNSET
        if not isinstance(self.failure_sub_types, Unset):
            failure_sub_types = []
            for failure_sub_types_item_data in self.failure_sub_types:
                failure_sub_types_item: str = failure_sub_types_item_data
                failure_sub_types.append(failure_sub_types_item)

        additional_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message
        if exception is not UNSET:
            field_dict["exception"] = exception
        if failure_types is not UNSET:
            field_dict["failureTypes"] = failure_types
        if failure_sub_types is not UNSET:
            field_dict["failureSubTypes"] = failure_sub_types
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_message_additional_info import ResponseMessageAdditionalInfo
        from ..models.response_message_exception import ResponseMessageException

        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: ResponseMessageCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_response_message_code(_code)

        _level = d.pop("level", UNSET)
        level: ResponseMessageLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = check_response_message_level(_level)

        message = d.pop("message", UNSET)

        _exception = d.pop("exception", UNSET)
        exception: ResponseMessageException | Unset
        if isinstance(_exception, Unset):
            exception = UNSET
        else:
            exception = ResponseMessageException.from_dict(_exception)

        _failure_types = d.pop("failureTypes", UNSET)
        failure_types: list[ResponseMessageFailureTypesItem] | Unset = UNSET
        if _failure_types is not UNSET:
            failure_types = []
            for failure_types_item_data in _failure_types:
                failure_types_item = check_response_message_failure_types_item(failure_types_item_data)

                failure_types.append(failure_types_item)

        _failure_sub_types = d.pop("failureSubTypes", UNSET)
        failure_sub_types: list[ResponseMessageFailureSubTypesItem] | Unset = UNSET
        if _failure_sub_types is not UNSET:
            failure_sub_types = []
            for failure_sub_types_item_data in _failure_sub_types:
                failure_sub_types_item = check_response_message_failure_sub_types_item(failure_sub_types_item_data)

                failure_sub_types.append(failure_sub_types_item)

        _additional_info = d.pop("additionalInfo", UNSET)
        additional_info: ResponseMessageAdditionalInfo | Unset
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = ResponseMessageAdditionalInfo.from_dict(_additional_info)

        response_message = cls(
            code=code,
            level=level,
            message=message,
            exception=exception,
            failure_types=failure_types,
            failure_sub_types=failure_sub_types,
            additional_info=additional_info,
        )

        response_message.additional_properties = d
        return response_message

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_dto_map_string_string_status import (
    ResponseDTOMapStringStringStatus,
    check_response_dto_map_string_string_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_dto_map_string_string_data import ResponseDTOMapStringStringData
    from ..models.response_dto_map_string_string_meta_data import ResponseDTOMapStringStringMetaData


T = TypeVar("T", bound="ResponseDTOMapStringString")


@_attrs_define
class ResponseDTOMapStringString:
    """
    Attributes:
        status (ResponseDTOMapStringStringStatus | Unset):
        data (ResponseDTOMapStringStringData | Unset):
        meta_data (ResponseDTOMapStringStringMetaData | Unset):
        correlation_id (str | Unset):
    """

    status: ResponseDTOMapStringStringStatus | Unset = UNSET
    data: ResponseDTOMapStringStringData | Unset = UNSET
    meta_data: ResponseDTOMapStringStringMetaData | Unset = UNSET
    correlation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        correlation_id = self.correlation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_dto_map_string_string_data import ResponseDTOMapStringStringData
        from ..models.response_dto_map_string_string_meta_data import ResponseDTOMapStringStringMetaData

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ResponseDTOMapStringStringStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_response_dto_map_string_string_status(_status)

        _data = d.pop("data", UNSET)
        data: ResponseDTOMapStringStringData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ResponseDTOMapStringStringData.from_dict(_data)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: ResponseDTOMapStringStringMetaData | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = ResponseDTOMapStringStringMetaData.from_dict(_meta_data)

        correlation_id = d.pop("correlationId", UNSET)

        response_dto_map_string_string = cls(
            status=status,
            data=data,
            meta_data=meta_data,
            correlation_id=correlation_id,
        )

        response_dto_map_string_string.additional_properties = d
        return response_dto_map_string_string

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

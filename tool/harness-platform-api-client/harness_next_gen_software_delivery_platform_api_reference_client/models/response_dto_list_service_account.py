from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_dto_list_service_account_status import (
    ResponseDTOListServiceAccountStatus,
    check_response_dto_list_service_account_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_dto_list_service_account_meta_data import ResponseDTOListServiceAccountMetaData
    from ..models.service_account import ServiceAccount


T = TypeVar("T", bound="ResponseDTOListServiceAccount")


@_attrs_define
class ResponseDTOListServiceAccount:
    """
    Attributes:
        status (ResponseDTOListServiceAccountStatus | Unset):
        data (list[ServiceAccount] | Unset):
        meta_data (ResponseDTOListServiceAccountMetaData | Unset):
        correlation_id (str | Unset):
    """

    status: ResponseDTOListServiceAccountStatus | Unset = UNSET
    data: list[ServiceAccount] | Unset = UNSET
    meta_data: ResponseDTOListServiceAccountMetaData | Unset = UNSET
    correlation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

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
        from ..models.response_dto_list_service_account_meta_data import ResponseDTOListServiceAccountMetaData
        from ..models.service_account import ServiceAccount

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ResponseDTOListServiceAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_response_dto_list_service_account_status(_status)

        _data = d.pop("data", UNSET)
        data: list[ServiceAccount] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ServiceAccount.from_dict(data_item_data)

                data.append(data_item)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: ResponseDTOListServiceAccountMetaData | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = ResponseDTOListServiceAccountMetaData.from_dict(_meta_data)

        correlation_id = d.pop("correlationId", UNSET)

        response_dto_list_service_account = cls(
            status=status,
            data=data,
            meta_data=meta_data,
            correlation_id=correlation_id,
        )

        response_dto_list_service_account.additional_properties = d
        return response_dto_list_service_account

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

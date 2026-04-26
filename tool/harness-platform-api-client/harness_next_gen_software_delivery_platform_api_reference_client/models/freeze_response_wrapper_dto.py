from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeze_error_response_dto import FreezeErrorResponseDTO
    from ..models.freeze_response import FreezeResponse


T = TypeVar("T", bound="FreezeResponseWrapperDTO")


@_attrs_define
class FreezeResponseWrapperDTO:
    """
    Attributes:
        no_of_success (int | Unset):
        no_of_failed (int | Unset):
        successful_freeze_response_dto_list (list[FreezeResponse] | Unset):
        freeze_error_response_dto_list (list[FreezeErrorResponseDTO] | Unset):
    """

    no_of_success: int | Unset = UNSET
    no_of_failed: int | Unset = UNSET
    successful_freeze_response_dto_list: list[FreezeResponse] | Unset = UNSET
    freeze_error_response_dto_list: list[FreezeErrorResponseDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_of_success = self.no_of_success

        no_of_failed = self.no_of_failed

        successful_freeze_response_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successful_freeze_response_dto_list, Unset):
            successful_freeze_response_dto_list = []
            for successful_freeze_response_dto_list_item_data in self.successful_freeze_response_dto_list:
                successful_freeze_response_dto_list_item = successful_freeze_response_dto_list_item_data.to_dict()
                successful_freeze_response_dto_list.append(successful_freeze_response_dto_list_item)

        freeze_error_response_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.freeze_error_response_dto_list, Unset):
            freeze_error_response_dto_list = []
            for freeze_error_response_dto_list_item_data in self.freeze_error_response_dto_list:
                freeze_error_response_dto_list_item = freeze_error_response_dto_list_item_data.to_dict()
                freeze_error_response_dto_list.append(freeze_error_response_dto_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_of_success is not UNSET:
            field_dict["noOfSuccess"] = no_of_success
        if no_of_failed is not UNSET:
            field_dict["noOfFailed"] = no_of_failed
        if successful_freeze_response_dto_list is not UNSET:
            field_dict["successfulFreezeResponseDTOList"] = successful_freeze_response_dto_list
        if freeze_error_response_dto_list is not UNSET:
            field_dict["freezeErrorResponseDTOList"] = freeze_error_response_dto_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeze_error_response_dto import FreezeErrorResponseDTO
        from ..models.freeze_response import FreezeResponse

        d = dict(src_dict)
        no_of_success = d.pop("noOfSuccess", UNSET)

        no_of_failed = d.pop("noOfFailed", UNSET)

        _successful_freeze_response_dto_list = d.pop("successfulFreezeResponseDTOList", UNSET)
        successful_freeze_response_dto_list: list[FreezeResponse] | Unset = UNSET
        if _successful_freeze_response_dto_list is not UNSET:
            successful_freeze_response_dto_list = []
            for successful_freeze_response_dto_list_item_data in _successful_freeze_response_dto_list:
                successful_freeze_response_dto_list_item = FreezeResponse.from_dict(
                    successful_freeze_response_dto_list_item_data
                )

                successful_freeze_response_dto_list.append(successful_freeze_response_dto_list_item)

        _freeze_error_response_dto_list = d.pop("freezeErrorResponseDTOList", UNSET)
        freeze_error_response_dto_list: list[FreezeErrorResponseDTO] | Unset = UNSET
        if _freeze_error_response_dto_list is not UNSET:
            freeze_error_response_dto_list = []
            for freeze_error_response_dto_list_item_data in _freeze_error_response_dto_list:
                freeze_error_response_dto_list_item = FreezeErrorResponseDTO.from_dict(
                    freeze_error_response_dto_list_item_data
                )

                freeze_error_response_dto_list.append(freeze_error_response_dto_list_item)

        freeze_response_wrapper_dto = cls(
            no_of_success=no_of_success,
            no_of_failed=no_of_failed,
            successful_freeze_response_dto_list=successful_freeze_response_dto_list,
            freeze_error_response_dto_list=freeze_error_response_dto_list,
        )

        freeze_response_wrapper_dto.additional_properties = d
        return freeze_response_wrapper_dto

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

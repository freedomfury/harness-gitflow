from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_instance_response_status import (
    ApprovalInstanceResponseStatus,
    check_approval_instance_response_status,
)
from ..models.approval_instance_response_type import ApprovalInstanceResponseType, check_approval_instance_response_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_instance_details_dto import ApprovalInstanceDetailsDTO


T = TypeVar("T", bound="ApprovalInstanceResponse")


@_attrs_define
class ApprovalInstanceResponse:
    """This contains details of Approval Instance response

    Attributes:
        id (str):
        type_ (ApprovalInstanceResponseType):
        status (ApprovalInstanceResponseStatus):
        details (ApprovalInstanceDetailsDTO):
        deadline (int | Unset):
        created_at (int | Unset):
        last_modified_at (int | Unset):
        error_message (str | Unset):
    """

    id: str
    type_: ApprovalInstanceResponseType
    status: ApprovalInstanceResponseStatus
    details: ApprovalInstanceDetailsDTO
    deadline: int | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        status: str = self.status

        details = self.details.to_dict()

        deadline = self.deadline

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "details": details,
            }
        )
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_instance_details_dto import ApprovalInstanceDetailsDTO

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_approval_instance_response_type(d.pop("type"))

        status = check_approval_instance_response_status(d.pop("status"))

        details = ApprovalInstanceDetailsDTO.from_dict(d.pop("details"))

        deadline = d.pop("deadline", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        approval_instance_response = cls(
            id=id,
            type_=type_,
            status=status,
            details=details,
            deadline=deadline,
            created_at=created_at,
            last_modified_at=last_modified_at,
            error_message=error_message,
        )

        approval_instance_response.additional_properties = d
        return approval_instance_response

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

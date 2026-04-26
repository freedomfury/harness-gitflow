from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_assignment_metadata import RoleAssignmentMetadata
    from ..models.service_account import ServiceAccount


T = TypeVar("T", bound="ServiceAccountAggregate")


@_attrs_define
class ServiceAccountAggregate:
    """This contains the Service Account details and its metadata.

    Attributes:
        service_account (ServiceAccount): This has the details of Service Account in Harness.
        created_at (int): This is the time at which Service Account was created.
        last_modified_at (int): This is the time at which Service Account was last modified.
        tokens_count (int | Unset): This is the total number of tokens in a Service Account.
        role_assignments_metadata_dto (list[RoleAssignmentMetadata] | Unset): This is the list of Role Assignments for
            the Service Account.
    """

    service_account: ServiceAccount
    created_at: int
    last_modified_at: int
    tokens_count: int | Unset = UNSET
    role_assignments_metadata_dto: list[RoleAssignmentMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_account = self.service_account.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        tokens_count = self.tokens_count

        role_assignments_metadata_dto: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_assignments_metadata_dto, Unset):
            role_assignments_metadata_dto = []
            for role_assignments_metadata_dto_item_data in self.role_assignments_metadata_dto:
                role_assignments_metadata_dto_item = role_assignments_metadata_dto_item_data.to_dict()
                role_assignments_metadata_dto.append(role_assignments_metadata_dto_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceAccount": service_account,
                "createdAt": created_at,
                "lastModifiedAt": last_modified_at,
            }
        )
        if tokens_count is not UNSET:
            field_dict["tokensCount"] = tokens_count
        if role_assignments_metadata_dto is not UNSET:
            field_dict["roleAssignmentsMetadataDTO"] = role_assignments_metadata_dto

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_assignment_metadata import RoleAssignmentMetadata
        from ..models.service_account import ServiceAccount

        d = dict(src_dict)
        service_account = ServiceAccount.from_dict(d.pop("serviceAccount"))

        created_at = d.pop("createdAt")

        last_modified_at = d.pop("lastModifiedAt")

        tokens_count = d.pop("tokensCount", UNSET)

        _role_assignments_metadata_dto = d.pop("roleAssignmentsMetadataDTO", UNSET)
        role_assignments_metadata_dto: list[RoleAssignmentMetadata] | Unset = UNSET
        if _role_assignments_metadata_dto is not UNSET:
            role_assignments_metadata_dto = []
            for role_assignments_metadata_dto_item_data in _role_assignments_metadata_dto:
                role_assignments_metadata_dto_item = RoleAssignmentMetadata.from_dict(
                    role_assignments_metadata_dto_item_data
                )

                role_assignments_metadata_dto.append(role_assignments_metadata_dto_item)

        service_account_aggregate = cls(
            service_account=service_account,
            created_at=created_at,
            last_modified_at=last_modified_at,
            tokens_count=tokens_count,
            role_assignments_metadata_dto=role_assignments_metadata_dto,
        )

        service_account_aggregate.additional_properties = d
        return service_account_aggregate

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

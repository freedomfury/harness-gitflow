from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization


T = TypeVar("T", bound="OrganizationResponse")


@_attrs_define
class OrganizationResponse:
    """This has details of the Organization along with its metadata in Harness.

    Attributes:
        organization (Organization): This has details of the Organization as defined in Harness.
        created_at (int | Unset): This is the time at which Organization was created.
        last_modified_at (int | Unset): This is the time at which Organization was last modified.
        harness_managed (bool | Unset): This indicates if this Organization is managed by Harness or not. If True,
            Harness can manage and modify this Organization.
    """

    organization: Organization
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    harness_managed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = self.organization.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        harness_managed = self.harness_managed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if harness_managed is not UNSET:
            field_dict["harnessManaged"] = harness_managed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization import Organization

        d = dict(src_dict)
        organization = Organization.from_dict(d.pop("organization"))

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        harness_managed = d.pop("harnessManaged", UNSET)

        organization_response = cls(
            organization=organization,
            created_at=created_at,
            last_modified_at=last_modified_at,
            harness_managed=harness_managed,
        )

        organization_response.additional_properties = d
        return organization_response

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

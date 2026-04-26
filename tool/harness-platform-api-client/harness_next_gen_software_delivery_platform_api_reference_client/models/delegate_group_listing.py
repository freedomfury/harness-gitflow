from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_group_details import DelegateGroupDetails
    from ..models.delegate_version_status_instance_level_count import DelegateVersionStatusInstanceLevelCount


T = TypeVar("T", bound="DelegateGroupListing")


@_attrs_define
class DelegateGroupListing:
    """
    Attributes:
        delegate_group_details (list[DelegateGroupDetails] | Unset):
        delegate_version_status_aggregated_count (DelegateVersionStatusInstanceLevelCount | Unset):
        auto_upgrade_off_count (int | Unset):
    """

    delegate_group_details: list[DelegateGroupDetails] | Unset = UNSET
    delegate_version_status_aggregated_count: DelegateVersionStatusInstanceLevelCount | Unset = UNSET
    auto_upgrade_off_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegate_group_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delegate_group_details, Unset):
            delegate_group_details = []
            for delegate_group_details_item_data in self.delegate_group_details:
                delegate_group_details_item = delegate_group_details_item_data.to_dict()
                delegate_group_details.append(delegate_group_details_item)

        delegate_version_status_aggregated_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delegate_version_status_aggregated_count, Unset):
            delegate_version_status_aggregated_count = self.delegate_version_status_aggregated_count.to_dict()

        auto_upgrade_off_count = self.auto_upgrade_off_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delegate_group_details is not UNSET:
            field_dict["delegateGroupDetails"] = delegate_group_details
        if delegate_version_status_aggregated_count is not UNSET:
            field_dict["delegateVersionStatusAggregatedCount"] = delegate_version_status_aggregated_count
        if auto_upgrade_off_count is not UNSET:
            field_dict["autoUpgradeOffCount"] = auto_upgrade_off_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_group_details import DelegateGroupDetails
        from ..models.delegate_version_status_instance_level_count import DelegateVersionStatusInstanceLevelCount

        d = dict(src_dict)
        _delegate_group_details = d.pop("delegateGroupDetails", UNSET)
        delegate_group_details: list[DelegateGroupDetails] | Unset = UNSET
        if _delegate_group_details is not UNSET:
            delegate_group_details = []
            for delegate_group_details_item_data in _delegate_group_details:
                delegate_group_details_item = DelegateGroupDetails.from_dict(delegate_group_details_item_data)

                delegate_group_details.append(delegate_group_details_item)

        _delegate_version_status_aggregated_count = d.pop("delegateVersionStatusAggregatedCount", UNSET)
        delegate_version_status_aggregated_count: DelegateVersionStatusInstanceLevelCount | Unset
        if isinstance(_delegate_version_status_aggregated_count, Unset):
            delegate_version_status_aggregated_count = UNSET
        else:
            delegate_version_status_aggregated_count = DelegateVersionStatusInstanceLevelCount.from_dict(
                _delegate_version_status_aggregated_count
            )

        auto_upgrade_off_count = d.pop("autoUpgradeOffCount", UNSET)

        delegate_group_listing = cls(
            delegate_group_details=delegate_group_details,
            delegate_version_status_aggregated_count=delegate_version_status_aggregated_count,
            auto_upgrade_off_count=auto_upgrade_off_count,
        )

        delegate_group_listing.additional_properties = d
        return delegate_group_listing

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

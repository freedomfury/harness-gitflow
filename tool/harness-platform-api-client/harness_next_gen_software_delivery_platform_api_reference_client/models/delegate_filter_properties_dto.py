from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_filter_properties_dto_delegate_instance_filter import (
    DelegateFilterPropertiesDTODelegateInstanceFilter,
    check_delegate_filter_properties_dto_delegate_instance_filter,
)
from ..models.delegate_filter_properties_dto_filter_type import (
    DelegateFilterPropertiesDTOFilterType,
    check_delegate_filter_properties_dto_filter_type,
)
from ..models.delegate_filter_properties_dto_status import (
    DelegateFilterPropertiesDTOStatus,
    check_delegate_filter_properties_dto_status,
)
from ..models.delegate_filter_properties_dto_version_status import (
    DelegateFilterPropertiesDTOVersionStatus,
    check_delegate_filter_properties_dto_version_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_filter_properties_dto_tags import DelegateFilterPropertiesDTOTags


T = TypeVar("T", bound="DelegateFilterPropertiesDTO")


@_attrs_define
class DelegateFilterPropertiesDTO:
    """Properties to filter delegates

    Attributes:
        filter_type (DelegateFilterPropertiesDTOFilterType): This specifies the corresponding Entity of the filter.
        status (DelegateFilterPropertiesDTOStatus | Unset): Filter on delegate connectivity
        description (str | Unset): Filter on delegate description
        host_name (str | Unset): Filter on delegate hostName
        delegate_name (str | Unset): Filter on delegate name
        delegate_type (str | Unset): Filter on delegate type
        delegate_group_identifier (str | Unset): Filter on delegate group id
        delegate_tags (list[str] | Unset): Filter on delegate tags
        delegate_instance_filter (DelegateFilterPropertiesDTODelegateInstanceFilter | Unset): Filter on delegate
            instance status
        auto_upgrade (str | Unset): Filter on delegate auto upgrade
        version_status (DelegateFilterPropertiesDTOVersionStatus | Unset): Filter on delegate version status
        runner (bool | Unset): Filter for Delegate 2.0
        tags (DelegateFilterPropertiesDTOTags | Unset): Filter tags as a key-value pair.
    """

    filter_type: DelegateFilterPropertiesDTOFilterType
    status: DelegateFilterPropertiesDTOStatus | Unset = UNSET
    description: str | Unset = UNSET
    host_name: str | Unset = UNSET
    delegate_name: str | Unset = UNSET
    delegate_type: str | Unset = UNSET
    delegate_group_identifier: str | Unset = UNSET
    delegate_tags: list[str] | Unset = UNSET
    delegate_instance_filter: DelegateFilterPropertiesDTODelegateInstanceFilter | Unset = UNSET
    auto_upgrade: str | Unset = UNSET
    version_status: DelegateFilterPropertiesDTOVersionStatus | Unset = UNSET
    runner: bool | Unset = UNSET
    tags: DelegateFilterPropertiesDTOTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type: str = self.filter_type

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description = self.description

        host_name = self.host_name

        delegate_name = self.delegate_name

        delegate_type = self.delegate_type

        delegate_group_identifier = self.delegate_group_identifier

        delegate_tags: list[str] | Unset = UNSET
        if not isinstance(self.delegate_tags, Unset):
            delegate_tags = self.delegate_tags

        delegate_instance_filter: str | Unset = UNSET
        if not isinstance(self.delegate_instance_filter, Unset):
            delegate_instance_filter = self.delegate_instance_filter

        auto_upgrade = self.auto_upgrade

        version_status: str | Unset = UNSET
        if not isinstance(self.version_status, Unset):
            version_status = self.version_status

        runner = self.runner

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterType": filter_type,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if delegate_name is not UNSET:
            field_dict["delegateName"] = delegate_name
        if delegate_type is not UNSET:
            field_dict["delegateType"] = delegate_type
        if delegate_group_identifier is not UNSET:
            field_dict["delegateGroupIdentifier"] = delegate_group_identifier
        if delegate_tags is not UNSET:
            field_dict["delegateTags"] = delegate_tags
        if delegate_instance_filter is not UNSET:
            field_dict["delegateInstanceFilter"] = delegate_instance_filter
        if auto_upgrade is not UNSET:
            field_dict["autoUpgrade"] = auto_upgrade
        if version_status is not UNSET:
            field_dict["versionStatus"] = version_status
        if runner is not UNSET:
            field_dict["runner"] = runner
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_filter_properties_dto_tags import DelegateFilterPropertiesDTOTags

        d = dict(src_dict)
        filter_type = check_delegate_filter_properties_dto_filter_type(d.pop("filterType"))

        _status = d.pop("status", UNSET)
        status: DelegateFilterPropertiesDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_delegate_filter_properties_dto_status(_status)

        description = d.pop("description", UNSET)

        host_name = d.pop("hostName", UNSET)

        delegate_name = d.pop("delegateName", UNSET)

        delegate_type = d.pop("delegateType", UNSET)

        delegate_group_identifier = d.pop("delegateGroupIdentifier", UNSET)

        delegate_tags = cast(list[str], d.pop("delegateTags", UNSET))

        _delegate_instance_filter = d.pop("delegateInstanceFilter", UNSET)
        delegate_instance_filter: DelegateFilterPropertiesDTODelegateInstanceFilter | Unset
        if isinstance(_delegate_instance_filter, Unset):
            delegate_instance_filter = UNSET
        else:
            delegate_instance_filter = check_delegate_filter_properties_dto_delegate_instance_filter(
                _delegate_instance_filter
            )

        auto_upgrade = d.pop("autoUpgrade", UNSET)

        _version_status = d.pop("versionStatus", UNSET)
        version_status: DelegateFilterPropertiesDTOVersionStatus | Unset
        if isinstance(_version_status, Unset):
            version_status = UNSET
        else:
            version_status = check_delegate_filter_properties_dto_version_status(_version_status)

        runner = d.pop("runner", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: DelegateFilterPropertiesDTOTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = DelegateFilterPropertiesDTOTags.from_dict(_tags)

        delegate_filter_properties_dto = cls(
            filter_type=filter_type,
            status=status,
            description=description,
            host_name=host_name,
            delegate_name=delegate_name,
            delegate_type=delegate_type,
            delegate_group_identifier=delegate_group_identifier,
            delegate_tags=delegate_tags,
            delegate_instance_filter=delegate_instance_filter,
            auto_upgrade=auto_upgrade,
            version_status=version_status,
            runner=runner,
            tags=tags,
        )

        delegate_filter_properties_dto.additional_properties = d
        return delegate_filter_properties_dto

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

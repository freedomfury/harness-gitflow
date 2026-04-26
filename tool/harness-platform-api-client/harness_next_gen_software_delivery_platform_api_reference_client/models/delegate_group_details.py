from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_group_details_auto_upgrade import (
    DelegateGroupDetailsAutoUpgrade,
    check_delegate_group_details_auto_upgrade,
)
from ..models.delegate_group_details_delegate_group_version_status import (
    DelegateGroupDetailsDelegateGroupVersionStatus,
    check_delegate_group_details_delegate_group_version_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_group_details_group_implicit_selectors import DelegateGroupDetailsGroupImplicitSelectors
    from ..models.delegate_group_inner import DelegateGroupInner
    from ..models.delegate_version_status_instance_level_count import DelegateVersionStatusInstanceLevelCount


T = TypeVar("T", bound="DelegateGroupDetails")


@_attrs_define
class DelegateGroupDetails:
    """
    Attributes:
        group_id (str | Unset):
        delegate_group_identifier (str | Unset):
        delegate_type (str | Unset):
        group_name (str | Unset):
        delegate_description (str | Unset):
        delegate_configuration_id (str | Unset):
        group_implicit_selectors (DelegateGroupDetailsGroupImplicitSelectors | Unset):
        group_custom_selectors (list[str] | Unset):
        last_heart_beat (int | Unset):
        connectivity_status (str | Unset):
        actively_connected (bool | Unset):
        grpc_active (bool | Unset):
        delegate_instance_details (list[DelegateGroupInner] | Unset):
        token_active (bool | Unset):
        auto_upgrade (DelegateGroupDetailsAutoUpgrade | Unset):
        delegate_group_expiration_time (int | Unset):
        delegate_version (str | Unset):
        upgrader_last_updated (int | Unset):
        immutable (bool | Unset):
        group_version (str | Unset):
        is_unsupported (bool | Unset):
        delegate_group_version_status (DelegateGroupDetailsDelegateGroupVersionStatus | Unset):
        delegate_version_status_instance_level_count (DelegateVersionStatusInstanceLevelCount | Unset):
        unsupported (bool | Unset):
    """

    group_id: str | Unset = UNSET
    delegate_group_identifier: str | Unset = UNSET
    delegate_type: str | Unset = UNSET
    group_name: str | Unset = UNSET
    delegate_description: str | Unset = UNSET
    delegate_configuration_id: str | Unset = UNSET
    group_implicit_selectors: DelegateGroupDetailsGroupImplicitSelectors | Unset = UNSET
    group_custom_selectors: list[str] | Unset = UNSET
    last_heart_beat: int | Unset = UNSET
    connectivity_status: str | Unset = UNSET
    actively_connected: bool | Unset = UNSET
    grpc_active: bool | Unset = UNSET
    delegate_instance_details: list[DelegateGroupInner] | Unset = UNSET
    token_active: bool | Unset = UNSET
    auto_upgrade: DelegateGroupDetailsAutoUpgrade | Unset = UNSET
    delegate_group_expiration_time: int | Unset = UNSET
    delegate_version: str | Unset = UNSET
    upgrader_last_updated: int | Unset = UNSET
    immutable: bool | Unset = UNSET
    group_version: str | Unset = UNSET
    is_unsupported: bool | Unset = UNSET
    delegate_group_version_status: DelegateGroupDetailsDelegateGroupVersionStatus | Unset = UNSET
    delegate_version_status_instance_level_count: DelegateVersionStatusInstanceLevelCount | Unset = UNSET
    unsupported: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        delegate_group_identifier = self.delegate_group_identifier

        delegate_type = self.delegate_type

        group_name = self.group_name

        delegate_description = self.delegate_description

        delegate_configuration_id = self.delegate_configuration_id

        group_implicit_selectors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_implicit_selectors, Unset):
            group_implicit_selectors = self.group_implicit_selectors.to_dict()

        group_custom_selectors: list[str] | Unset = UNSET
        if not isinstance(self.group_custom_selectors, Unset):
            group_custom_selectors = self.group_custom_selectors

        last_heart_beat = self.last_heart_beat

        connectivity_status = self.connectivity_status

        actively_connected = self.actively_connected

        grpc_active = self.grpc_active

        delegate_instance_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delegate_instance_details, Unset):
            delegate_instance_details = []
            for delegate_instance_details_item_data in self.delegate_instance_details:
                delegate_instance_details_item = delegate_instance_details_item_data.to_dict()
                delegate_instance_details.append(delegate_instance_details_item)

        token_active = self.token_active

        auto_upgrade: str | Unset = UNSET
        if not isinstance(self.auto_upgrade, Unset):
            auto_upgrade = self.auto_upgrade

        delegate_group_expiration_time = self.delegate_group_expiration_time

        delegate_version = self.delegate_version

        upgrader_last_updated = self.upgrader_last_updated

        immutable = self.immutable

        group_version = self.group_version

        is_unsupported = self.is_unsupported

        delegate_group_version_status: str | Unset = UNSET
        if not isinstance(self.delegate_group_version_status, Unset):
            delegate_group_version_status = self.delegate_group_version_status

        delegate_version_status_instance_level_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delegate_version_status_instance_level_count, Unset):
            delegate_version_status_instance_level_count = self.delegate_version_status_instance_level_count.to_dict()

        unsupported = self.unsupported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if delegate_group_identifier is not UNSET:
            field_dict["delegateGroupIdentifier"] = delegate_group_identifier
        if delegate_type is not UNSET:
            field_dict["delegateType"] = delegate_type
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if delegate_description is not UNSET:
            field_dict["delegateDescription"] = delegate_description
        if delegate_configuration_id is not UNSET:
            field_dict["delegateConfigurationId"] = delegate_configuration_id
        if group_implicit_selectors is not UNSET:
            field_dict["groupImplicitSelectors"] = group_implicit_selectors
        if group_custom_selectors is not UNSET:
            field_dict["groupCustomSelectors"] = group_custom_selectors
        if last_heart_beat is not UNSET:
            field_dict["lastHeartBeat"] = last_heart_beat
        if connectivity_status is not UNSET:
            field_dict["connectivityStatus"] = connectivity_status
        if actively_connected is not UNSET:
            field_dict["activelyConnected"] = actively_connected
        if grpc_active is not UNSET:
            field_dict["grpcActive"] = grpc_active
        if delegate_instance_details is not UNSET:
            field_dict["delegateInstanceDetails"] = delegate_instance_details
        if token_active is not UNSET:
            field_dict["tokenActive"] = token_active
        if auto_upgrade is not UNSET:
            field_dict["autoUpgrade"] = auto_upgrade
        if delegate_group_expiration_time is not UNSET:
            field_dict["delegateGroupExpirationTime"] = delegate_group_expiration_time
        if delegate_version is not UNSET:
            field_dict["delegateVersion"] = delegate_version
        if upgrader_last_updated is not UNSET:
            field_dict["upgraderLastUpdated"] = upgrader_last_updated
        if immutable is not UNSET:
            field_dict["immutable"] = immutable
        if group_version is not UNSET:
            field_dict["groupVersion"] = group_version
        if is_unsupported is not UNSET:
            field_dict["isUnsupported"] = is_unsupported
        if delegate_group_version_status is not UNSET:
            field_dict["delegateGroupVersionStatus"] = delegate_group_version_status
        if delegate_version_status_instance_level_count is not UNSET:
            field_dict["delegateVersionStatusInstanceLevelCount"] = delegate_version_status_instance_level_count
        if unsupported is not UNSET:
            field_dict["unsupported"] = unsupported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_group_details_group_implicit_selectors import DelegateGroupDetailsGroupImplicitSelectors
        from ..models.delegate_group_inner import DelegateGroupInner
        from ..models.delegate_version_status_instance_level_count import DelegateVersionStatusInstanceLevelCount

        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        delegate_group_identifier = d.pop("delegateGroupIdentifier", UNSET)

        delegate_type = d.pop("delegateType", UNSET)

        group_name = d.pop("groupName", UNSET)

        delegate_description = d.pop("delegateDescription", UNSET)

        delegate_configuration_id = d.pop("delegateConfigurationId", UNSET)

        _group_implicit_selectors = d.pop("groupImplicitSelectors", UNSET)
        group_implicit_selectors: DelegateGroupDetailsGroupImplicitSelectors | Unset
        if isinstance(_group_implicit_selectors, Unset):
            group_implicit_selectors = UNSET
        else:
            group_implicit_selectors = DelegateGroupDetailsGroupImplicitSelectors.from_dict(_group_implicit_selectors)

        group_custom_selectors = cast(list[str], d.pop("groupCustomSelectors", UNSET))

        last_heart_beat = d.pop("lastHeartBeat", UNSET)

        connectivity_status = d.pop("connectivityStatus", UNSET)

        actively_connected = d.pop("activelyConnected", UNSET)

        grpc_active = d.pop("grpcActive", UNSET)

        _delegate_instance_details = d.pop("delegateInstanceDetails", UNSET)
        delegate_instance_details: list[DelegateGroupInner] | Unset = UNSET
        if _delegate_instance_details is not UNSET:
            delegate_instance_details = []
            for delegate_instance_details_item_data in _delegate_instance_details:
                delegate_instance_details_item = DelegateGroupInner.from_dict(delegate_instance_details_item_data)

                delegate_instance_details.append(delegate_instance_details_item)

        token_active = d.pop("tokenActive", UNSET)

        _auto_upgrade = d.pop("autoUpgrade", UNSET)
        auto_upgrade: DelegateGroupDetailsAutoUpgrade | Unset
        if isinstance(_auto_upgrade, Unset):
            auto_upgrade = UNSET
        else:
            auto_upgrade = check_delegate_group_details_auto_upgrade(_auto_upgrade)

        delegate_group_expiration_time = d.pop("delegateGroupExpirationTime", UNSET)

        delegate_version = d.pop("delegateVersion", UNSET)

        upgrader_last_updated = d.pop("upgraderLastUpdated", UNSET)

        immutable = d.pop("immutable", UNSET)

        group_version = d.pop("groupVersion", UNSET)

        is_unsupported = d.pop("isUnsupported", UNSET)

        _delegate_group_version_status = d.pop("delegateGroupVersionStatus", UNSET)
        delegate_group_version_status: DelegateGroupDetailsDelegateGroupVersionStatus | Unset
        if isinstance(_delegate_group_version_status, Unset):
            delegate_group_version_status = UNSET
        else:
            delegate_group_version_status = check_delegate_group_details_delegate_group_version_status(
                _delegate_group_version_status
            )

        _delegate_version_status_instance_level_count = d.pop("delegateVersionStatusInstanceLevelCount", UNSET)
        delegate_version_status_instance_level_count: DelegateVersionStatusInstanceLevelCount | Unset
        if isinstance(_delegate_version_status_instance_level_count, Unset):
            delegate_version_status_instance_level_count = UNSET
        else:
            delegate_version_status_instance_level_count = DelegateVersionStatusInstanceLevelCount.from_dict(
                _delegate_version_status_instance_level_count
            )

        unsupported = d.pop("unsupported", UNSET)

        delegate_group_details = cls(
            group_id=group_id,
            delegate_group_identifier=delegate_group_identifier,
            delegate_type=delegate_type,
            group_name=group_name,
            delegate_description=delegate_description,
            delegate_configuration_id=delegate_configuration_id,
            group_implicit_selectors=group_implicit_selectors,
            group_custom_selectors=group_custom_selectors,
            last_heart_beat=last_heart_beat,
            connectivity_status=connectivity_status,
            actively_connected=actively_connected,
            grpc_active=grpc_active,
            delegate_instance_details=delegate_instance_details,
            token_active=token_active,
            auto_upgrade=auto_upgrade,
            delegate_group_expiration_time=delegate_group_expiration_time,
            delegate_version=delegate_version,
            upgrader_last_updated=upgrader_last_updated,
            immutable=immutable,
            group_version=group_version,
            is_unsupported=is_unsupported,
            delegate_group_version_status=delegate_group_version_status,
            delegate_version_status_instance_level_count=delegate_version_status_instance_level_count,
            unsupported=unsupported,
        )

        delegate_group_details.additional_properties = d
        return delegate_group_details

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

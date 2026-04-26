from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_group_inner_delegate_instance_version_status import (
    DelegateGroupInnerDelegateInstanceVersionStatus,
    check_delegate_group_inner_delegate_instance_version_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_connection_details import DelegateConnectionDetails


T = TypeVar("T", bound="DelegateGroupInner")


@_attrs_define
class DelegateGroupInner:
    """
    Attributes:
        uuid (str | Unset):
        last_heartbeat (int | Unset):
        actively_connected (bool | Unset):
        host_name (str | Unset):
        token_active (bool | Unset):
        version (str | Unset):
        delegate_expiration_time (int | Unset):
        pollling_mode_enabled (bool | Unset):
        connections (list[DelegateConnectionDetails] | Unset):
        delegate_instance_version_status (DelegateGroupInnerDelegateInstanceVersionStatus | Unset):
        runner (bool | Unset):
        disabled (bool | Unset):
    """

    uuid: str | Unset = UNSET
    last_heartbeat: int | Unset = UNSET
    actively_connected: bool | Unset = UNSET
    host_name: str | Unset = UNSET
    token_active: bool | Unset = UNSET
    version: str | Unset = UNSET
    delegate_expiration_time: int | Unset = UNSET
    pollling_mode_enabled: bool | Unset = UNSET
    connections: list[DelegateConnectionDetails] | Unset = UNSET
    delegate_instance_version_status: DelegateGroupInnerDelegateInstanceVersionStatus | Unset = UNSET
    runner: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        last_heartbeat = self.last_heartbeat

        actively_connected = self.actively_connected

        host_name = self.host_name

        token_active = self.token_active

        version = self.version

        delegate_expiration_time = self.delegate_expiration_time

        pollling_mode_enabled = self.pollling_mode_enabled

        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        delegate_instance_version_status: str | Unset = UNSET
        if not isinstance(self.delegate_instance_version_status, Unset):
            delegate_instance_version_status = self.delegate_instance_version_status

        runner = self.runner

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if last_heartbeat is not UNSET:
            field_dict["lastHeartbeat"] = last_heartbeat
        if actively_connected is not UNSET:
            field_dict["activelyConnected"] = actively_connected
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if token_active is not UNSET:
            field_dict["tokenActive"] = token_active
        if version is not UNSET:
            field_dict["version"] = version
        if delegate_expiration_time is not UNSET:
            field_dict["delegateExpirationTime"] = delegate_expiration_time
        if pollling_mode_enabled is not UNSET:
            field_dict["polllingModeEnabled"] = pollling_mode_enabled
        if connections is not UNSET:
            field_dict["connections"] = connections
        if delegate_instance_version_status is not UNSET:
            field_dict["delegateInstanceVersionStatus"] = delegate_instance_version_status
        if runner is not UNSET:
            field_dict["runner"] = runner
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_connection_details import DelegateConnectionDetails

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        last_heartbeat = d.pop("lastHeartbeat", UNSET)

        actively_connected = d.pop("activelyConnected", UNSET)

        host_name = d.pop("hostName", UNSET)

        token_active = d.pop("tokenActive", UNSET)

        version = d.pop("version", UNSET)

        delegate_expiration_time = d.pop("delegateExpirationTime", UNSET)

        pollling_mode_enabled = d.pop("polllingModeEnabled", UNSET)

        _connections = d.pop("connections", UNSET)
        connections: list[DelegateConnectionDetails] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = DelegateConnectionDetails.from_dict(connections_item_data)

                connections.append(connections_item)

        _delegate_instance_version_status = d.pop("delegateInstanceVersionStatus", UNSET)
        delegate_instance_version_status: DelegateGroupInnerDelegateInstanceVersionStatus | Unset
        if isinstance(_delegate_instance_version_status, Unset):
            delegate_instance_version_status = UNSET
        else:
            delegate_instance_version_status = check_delegate_group_inner_delegate_instance_version_status(
                _delegate_instance_version_status
            )

        runner = d.pop("runner", UNSET)

        disabled = d.pop("disabled", UNSET)

        delegate_group_inner = cls(
            uuid=uuid,
            last_heartbeat=last_heartbeat,
            actively_connected=actively_connected,
            host_name=host_name,
            token_active=token_active,
            version=version,
            delegate_expiration_time=delegate_expiration_time,
            pollling_mode_enabled=pollling_mode_enabled,
            connections=connections,
            delegate_instance_version_status=delegate_instance_version_status,
            runner=runner,
            disabled=disabled,
        )

        delegate_group_inner.additional_properties = d
        return delegate_group_inner

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

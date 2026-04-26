from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DelegateReplica")


@_attrs_define
class DelegateReplica:
    """
    Attributes:
        uuid (str | Unset):
        last_heartbeat (int | Unset):
        connected (bool | Unset):
        host_name (str | Unset):
        version (str | Unset):
        expiring_at (int | Unset):
        status (str | Unset):
        runner (bool | Unset):
    """

    uuid: str | Unset = UNSET
    last_heartbeat: int | Unset = UNSET
    connected: bool | Unset = UNSET
    host_name: str | Unset = UNSET
    version: str | Unset = UNSET
    expiring_at: int | Unset = UNSET
    status: str | Unset = UNSET
    runner: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        last_heartbeat = self.last_heartbeat

        connected = self.connected

        host_name = self.host_name

        version = self.version

        expiring_at = self.expiring_at

        status = self.status

        runner = self.runner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if last_heartbeat is not UNSET:
            field_dict["lastHeartbeat"] = last_heartbeat
        if connected is not UNSET:
            field_dict["connected"] = connected
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if version is not UNSET:
            field_dict["version"] = version
        if expiring_at is not UNSET:
            field_dict["expiringAt"] = expiring_at
        if status is not UNSET:
            field_dict["status"] = status
        if runner is not UNSET:
            field_dict["runner"] = runner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        last_heartbeat = d.pop("lastHeartbeat", UNSET)

        connected = d.pop("connected", UNSET)

        host_name = d.pop("hostName", UNSET)

        version = d.pop("version", UNSET)

        expiring_at = d.pop("expiringAt", UNSET)

        status = d.pop("status", UNSET)

        runner = d.pop("runner", UNSET)

        delegate_replica = cls(
            uuid=uuid,
            last_heartbeat=last_heartbeat,
            connected=connected,
            host_name=host_name,
            version=version,
            expiring_at=expiring_at,
            status=status,
            runner=runner,
        )

        delegate_replica.additional_properties = d
        return delegate_replica

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

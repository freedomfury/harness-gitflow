from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DelegateConnectionDetails")


@_attrs_define
class DelegateConnectionDetails:
    """
    Attributes:
        uuid (str | Unset):
        version (str | Unset):
        last_heartbeat (int | Unset):
        last_grpc_heartbeat (int | Unset):
    """

    uuid: str | Unset = UNSET
    version: str | Unset = UNSET
    last_heartbeat: int | Unset = UNSET
    last_grpc_heartbeat: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        version = self.version

        last_heartbeat = self.last_heartbeat

        last_grpc_heartbeat = self.last_grpc_heartbeat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version is not UNSET:
            field_dict["version"] = version
        if last_heartbeat is not UNSET:
            field_dict["lastHeartbeat"] = last_heartbeat
        if last_grpc_heartbeat is not UNSET:
            field_dict["lastGrpcHeartbeat"] = last_grpc_heartbeat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        version = d.pop("version", UNSET)

        last_heartbeat = d.pop("lastHeartbeat", UNSET)

        last_grpc_heartbeat = d.pop("lastGrpcHeartbeat", UNSET)

        delegate_connection_details = cls(
            uuid=uuid,
            version=version,
            last_heartbeat=last_heartbeat,
            last_grpc_heartbeat=last_grpc_heartbeat,
        )

        delegate_connection_details.additional_properties = d
        return delegate_connection_details

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

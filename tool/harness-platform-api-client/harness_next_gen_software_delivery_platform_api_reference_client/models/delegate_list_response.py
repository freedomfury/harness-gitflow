from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_list_response_auto_upgrade import (
    DelegateListResponseAutoUpgrade,
    check_delegate_list_response_auto_upgrade,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delegate_replica import DelegateReplica


T = TypeVar("T", bound="DelegateListResponse")


@_attrs_define
class DelegateListResponse:
    """
    Attributes:
        type_ (str | Unset):
        name (str | Unset):
        description (str | Unset):
        tags (list[str] | Unset):
        last_heart_beat (int | Unset):
        connected (bool | Unset):
        delegate_replicas (list[DelegateReplica] | Unset):
        auto_upgrade (DelegateListResponseAutoUpgrade | Unset):
        legacy (bool | Unset):
        org_name (str | Unset):
        project_name (str | Unset):
    """

    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    last_heart_beat: int | Unset = UNSET
    connected: bool | Unset = UNSET
    delegate_replicas: list[DelegateReplica] | Unset = UNSET
    auto_upgrade: DelegateListResponseAutoUpgrade | Unset = UNSET
    legacy: bool | Unset = UNSET
    org_name: str | Unset = UNSET
    project_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        last_heart_beat = self.last_heart_beat

        connected = self.connected

        delegate_replicas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delegate_replicas, Unset):
            delegate_replicas = []
            for delegate_replicas_item_data in self.delegate_replicas:
                delegate_replicas_item = delegate_replicas_item_data.to_dict()
                delegate_replicas.append(delegate_replicas_item)

        auto_upgrade: str | Unset = UNSET
        if not isinstance(self.auto_upgrade, Unset):
            auto_upgrade = self.auto_upgrade

        legacy = self.legacy

        org_name = self.org_name

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if last_heart_beat is not UNSET:
            field_dict["lastHeartBeat"] = last_heart_beat
        if connected is not UNSET:
            field_dict["connected"] = connected
        if delegate_replicas is not UNSET:
            field_dict["delegateReplicas"] = delegate_replicas
        if auto_upgrade is not UNSET:
            field_dict["autoUpgrade"] = auto_upgrade
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if project_name is not UNSET:
            field_dict["projectName"] = project_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delegate_replica import DelegateReplica

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        last_heart_beat = d.pop("lastHeartBeat", UNSET)

        connected = d.pop("connected", UNSET)

        _delegate_replicas = d.pop("delegateReplicas", UNSET)
        delegate_replicas: list[DelegateReplica] | Unset = UNSET
        if _delegate_replicas is not UNSET:
            delegate_replicas = []
            for delegate_replicas_item_data in _delegate_replicas:
                delegate_replicas_item = DelegateReplica.from_dict(delegate_replicas_item_data)

                delegate_replicas.append(delegate_replicas_item)

        _auto_upgrade = d.pop("autoUpgrade", UNSET)
        auto_upgrade: DelegateListResponseAutoUpgrade | Unset
        if isinstance(_auto_upgrade, Unset):
            auto_upgrade = UNSET
        else:
            auto_upgrade = check_delegate_list_response_auto_upgrade(_auto_upgrade)

        legacy = d.pop("legacy", UNSET)

        org_name = d.pop("orgName", UNSET)

        project_name = d.pop("projectName", UNSET)

        delegate_list_response = cls(
            type_=type_,
            name=name,
            description=description,
            tags=tags,
            last_heart_beat=last_heart_beat,
            connected=connected,
            delegate_replicas=delegate_replicas,
            auto_upgrade=auto_upgrade,
            legacy=legacy,
            org_name=org_name,
            project_name=project_name,
        )

        delegate_list_response.additional_properties = d
        return delegate_list_response

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

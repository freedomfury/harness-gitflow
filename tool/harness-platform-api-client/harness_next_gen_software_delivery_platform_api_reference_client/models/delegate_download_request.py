from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_download_request_cluster_permission_type import (
    DelegateDownloadRequestClusterPermissionType,
    check_delegate_download_request_cluster_permission_type,
)
from ..models.delegate_download_request_size import DelegateDownloadRequestSize, check_delegate_download_request_size
from ..types import UNSET, Unset

T = TypeVar("T", bound="DelegateDownloadRequest")


@_attrs_define
class DelegateDownloadRequest:
    """
    Attributes:
        name (str):
        description (str | Unset):
        size (DelegateDownloadRequestSize | Unset):
        tags (list[str] | Unset):
        token_name (str | Unset):
        cluster_permission_type (DelegateDownloadRequestClusterPermissionType | Unset):
        custom_cluster_namespace (str | Unset):
    """

    name: str
    description: str | Unset = UNSET
    size: DelegateDownloadRequestSize | Unset = UNSET
    tags: list[str] | Unset = UNSET
    token_name: str | Unset = UNSET
    cluster_permission_type: DelegateDownloadRequestClusterPermissionType | Unset = UNSET
    custom_cluster_namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        size: str | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        token_name = self.token_name

        cluster_permission_type: str | Unset = UNSET
        if not isinstance(self.cluster_permission_type, Unset):
            cluster_permission_type = self.cluster_permission_type

        custom_cluster_namespace = self.custom_cluster_namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if size is not UNSET:
            field_dict["size"] = size
        if tags is not UNSET:
            field_dict["tags"] = tags
        if token_name is not UNSET:
            field_dict["tokenName"] = token_name
        if cluster_permission_type is not UNSET:
            field_dict["clusterPermissionType"] = cluster_permission_type
        if custom_cluster_namespace is not UNSET:
            field_dict["customClusterNamespace"] = custom_cluster_namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _size = d.pop("size", UNSET)
        size: DelegateDownloadRequestSize | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = check_delegate_download_request_size(_size)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_name = d.pop("tokenName", UNSET)

        _cluster_permission_type = d.pop("clusterPermissionType", UNSET)
        cluster_permission_type: DelegateDownloadRequestClusterPermissionType | Unset
        if isinstance(_cluster_permission_type, Unset):
            cluster_permission_type = UNSET
        else:
            cluster_permission_type = check_delegate_download_request_cluster_permission_type(_cluster_permission_type)

        custom_cluster_namespace = d.pop("customClusterNamespace", UNSET)

        delegate_download_request = cls(
            name=name,
            description=description,
            size=size,
            tags=tags,
            token_name=token_name,
            cluster_permission_type=cluster_permission_type,
            custom_cluster_namespace=custom_cluster_namespace,
        )

        delegate_download_request.additional_properties = d
        return delegate_download_request

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

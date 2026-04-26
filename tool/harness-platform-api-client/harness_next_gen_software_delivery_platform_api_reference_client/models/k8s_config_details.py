from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.k8s_config_details_k8s_permission_type import (
    K8SConfigDetailsK8SPermissionType,
    check_k8s_config_details_k8s_permission_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="K8SConfigDetails")


@_attrs_define
class K8SConfigDetails:
    """
    Attributes:
        k_8_s_permission_type (K8SConfigDetailsK8SPermissionType | Unset):
        namespace (str | Unset):
    """

    k_8_s_permission_type: K8SConfigDetailsK8SPermissionType | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        k_8_s_permission_type: str | Unset = UNSET
        if not isinstance(self.k_8_s_permission_type, Unset):
            k_8_s_permission_type = self.k_8_s_permission_type

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if k_8_s_permission_type is not UNSET:
            field_dict["k8sPermissionType"] = k_8_s_permission_type
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _k_8_s_permission_type = d.pop("k8sPermissionType", UNSET)
        k_8_s_permission_type: K8SConfigDetailsK8SPermissionType | Unset
        if isinstance(_k_8_s_permission_type, Unset):
            k_8_s_permission_type = UNSET
        else:
            k_8_s_permission_type = check_k8s_config_details_k8s_permission_type(_k_8_s_permission_type)

        namespace = d.pop("namespace", UNSET)

        k8s_config_details = cls(
            k_8_s_permission_type=k_8_s_permission_type,
            namespace=namespace,
        )

        k8s_config_details.additional_properties = d
        return k8s_config_details

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

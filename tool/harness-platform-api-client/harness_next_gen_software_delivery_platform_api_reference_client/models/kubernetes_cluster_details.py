from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.kubernetes_auth import KubernetesAuth


T = TypeVar("T", bound="KubernetesClusterDetails")


@_attrs_define
class KubernetesClusterDetails:
    """This contains kubernetes cluster details

    Attributes:
        master_url (str):
        auth (KubernetesAuth): This contains kubernetes auth details
    """

    master_url: str
    auth: KubernetesAuth
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_url = self.master_url

        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "masterUrl": master_url,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_auth import KubernetesAuth

        d = dict(src_dict)
        master_url = d.pop("masterUrl")

        auth = KubernetesAuth.from_dict(d.pop("auth"))

        kubernetes_cluster_details = cls(
            master_url=master_url,
            auth=auth,
        )

        kubernetes_cluster_details.additional_properties = d
        return kubernetes_cluster_details

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

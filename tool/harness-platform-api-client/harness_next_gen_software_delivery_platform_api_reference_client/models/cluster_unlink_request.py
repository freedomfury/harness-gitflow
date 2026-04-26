from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_basic_dto import ClusterBasicDTO


T = TypeVar("T", bound="ClusterUnlinkRequest")


@_attrs_define
class ClusterUnlinkRequest:
    """Batch Request to unlink clusters to the environment in a batch

    Attributes:
        env_ref (str): Environment identifier for the cluster
        org_identifier (str | Unset): Organization identifier of the environment
        project_identifier (str | Unset): Project identifier of the environment
        clusters (list[ClusterBasicDTO] | Unset): List of cluster identifiers and names
        unlink_all_clusters (bool | Unset): Unlink all clusters from the environment. Warning: Setting this to true will
            unlink ALL clusters linked to provided environment
    """

    env_ref: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    clusters: list[ClusterBasicDTO] | Unset = UNSET
    unlink_all_clusters: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_ref = self.env_ref

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        clusters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()
                clusters.append(clusters_item)

        unlink_all_clusters = self.unlink_all_clusters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "envRef": env_ref,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if unlink_all_clusters is not UNSET:
            field_dict["unlinkAllClusters"] = unlink_all_clusters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_basic_dto import ClusterBasicDTO

        d = dict(src_dict)
        env_ref = d.pop("envRef")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _clusters = d.pop("clusters", UNSET)
        clusters: list[ClusterBasicDTO] | Unset = UNSET
        if _clusters is not UNSET:
            clusters = []
            for clusters_item_data in _clusters:
                clusters_item = ClusterBasicDTO.from_dict(clusters_item_data)

                clusters.append(clusters_item)

        unlink_all_clusters = d.pop("unlinkAllClusters", UNSET)

        cluster_unlink_request = cls(
            env_ref=env_ref,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            clusters=clusters,
            unlink_all_clusters=unlink_all_clusters,
        )

        cluster_unlink_request.additional_properties = d
        return cluster_unlink_request

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

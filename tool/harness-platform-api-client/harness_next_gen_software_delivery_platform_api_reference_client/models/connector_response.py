from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_activity_details import ConnectorActivityDetails
    from ..models.connector_connectivity_details import ConnectorConnectivityDetails
    from ..models.connector_info import ConnectorInfo
    from ..models.entity_git_details import EntityGitDetails
    from ..models.governance_metadata import GovernanceMetadata


T = TypeVar("T", bound="ConnectorResponse")


@_attrs_define
class ConnectorResponse:
    """This has the Connector details along with its metadata.

    Attributes:
        connector (ConnectorInfo | Unset): This has the Connector details defined in Harness
        created_at (int | Unset): This is the time at which the Connector was created.
        last_modified_at (int | Unset): This is the time at which the Connector was last modified.
        status (ConnectorConnectivityDetails | Unset): Details of the connectivity status of the Connector.
        activity_details (ConnectorActivityDetails | Unset): This contains details of any kind of activities
            corresponding to the Connector.
        harness_managed (bool | Unset): This indicates if this Connector is managed by Harness or not. If True, Harness
            can manage and modify this Connector.
        git_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        entity_validity_details (EntityGitDetails | Unset): This contains Validity Details of the Entity
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
        is_favorite (bool | Unset):
    """

    connector: ConnectorInfo | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    status: ConnectorConnectivityDetails | Unset = UNSET
    activity_details: ConnectorActivityDetails | Unset = UNSET
    harness_managed: bool | Unset = UNSET
    git_details: EntityGitDetails | Unset = UNSET
    entity_validity_details: EntityGitDetails | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    is_favorite: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connector, Unset):
            connector = self.connector.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        activity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_details, Unset):
            activity_details = self.activity_details.to_dict()

        harness_managed = self.harness_managed

        git_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_details, Unset):
            git_details = self.git_details.to_dict()

        entity_validity_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_validity_details, Unset):
            entity_validity_details = self.entity_validity_details.to_dict()

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        is_favorite = self.is_favorite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connector is not UNSET:
            field_dict["connector"] = connector
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if status is not UNSET:
            field_dict["status"] = status
        if activity_details is not UNSET:
            field_dict["activityDetails"] = activity_details
        if harness_managed is not UNSET:
            field_dict["harnessManaged"] = harness_managed
        if git_details is not UNSET:
            field_dict["gitDetails"] = git_details
        if entity_validity_details is not UNSET:
            field_dict["entityValidityDetails"] = entity_validity_details
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_activity_details import ConnectorActivityDetails
        from ..models.connector_connectivity_details import ConnectorConnectivityDetails
        from ..models.connector_info import ConnectorInfo
        from ..models.entity_git_details import EntityGitDetails
        from ..models.governance_metadata import GovernanceMetadata

        d = dict(src_dict)
        _connector = d.pop("connector", UNSET)
        connector: ConnectorInfo | Unset
        if isinstance(_connector, Unset):
            connector = UNSET
        else:
            connector = ConnectorInfo.from_dict(_connector)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _status = d.pop("status", UNSET)
        status: ConnectorConnectivityDetails | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConnectorConnectivityDetails.from_dict(_status)

        _activity_details = d.pop("activityDetails", UNSET)
        activity_details: ConnectorActivityDetails | Unset
        if isinstance(_activity_details, Unset):
            activity_details = UNSET
        else:
            activity_details = ConnectorActivityDetails.from_dict(_activity_details)

        harness_managed = d.pop("harnessManaged", UNSET)

        _git_details = d.pop("gitDetails", UNSET)
        git_details: EntityGitDetails | Unset
        if isinstance(_git_details, Unset):
            git_details = UNSET
        else:
            git_details = EntityGitDetails.from_dict(_git_details)

        _entity_validity_details = d.pop("entityValidityDetails", UNSET)
        entity_validity_details: EntityGitDetails | Unset
        if isinstance(_entity_validity_details, Unset):
            entity_validity_details = UNSET
        else:
            entity_validity_details = EntityGitDetails.from_dict(_entity_validity_details)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        is_favorite = d.pop("isFavorite", UNSET)

        connector_response = cls(
            connector=connector,
            created_at=created_at,
            last_modified_at=last_modified_at,
            status=status,
            activity_details=activity_details,
            harness_managed=harness_managed,
            git_details=git_details,
            entity_validity_details=entity_validity_details,
            governance_metadata=governance_metadata,
            is_favorite=is_favorite,
        )

        connector_response.additional_properties = d
        return connector_response

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

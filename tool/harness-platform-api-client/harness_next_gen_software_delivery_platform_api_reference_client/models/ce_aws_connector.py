from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ce_aws_connector_autostopping_features_item import (
    CEAwsConnectorAutostoppingFeaturesItem,
    check_ce_aws_connector_autostopping_features_item,
)
from ..models.ce_aws_connector_commitment_features_item import (
    CEAwsConnectorCommitmentFeaturesItem,
    check_ce_aws_connector_commitment_features_item,
)
from ..models.ce_aws_connector_features_enabled_item import (
    CEAwsConnectorFeaturesEnabledItem,
    check_ce_aws_connector_features_enabled_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_cur_attributes import AwsCurAttributes
    from ..models.ce_aws_credential import CeAwsCredential
    from ..models.cross_account_access import CrossAccountAccess


T = TypeVar("T", bound="CEAwsConnector")


@_attrs_define
class CEAwsConnector:
    """This contains the cost explorer of AWS connector

    Attributes:
        connector_type (str):
        features_enabled (list[CEAwsConnectorFeaturesEnabledItem]):
        cross_account_access (CrossAccountAccess | Unset): This contains AWS connector cross account access details
        cur_attributes (AwsCurAttributes | Unset): This contains AWS cost and usage reports attributes
        aws_account_id (str | Unset):
        is_aws_gov_cloud_account (bool | Unset):
        autostopping_features (list[CEAwsConnectorAutostoppingFeaturesItem] | Unset):
        commitment_features (list[CEAwsConnectorCommitmentFeaturesItem] | Unset): List of commitment orchestration
            features enabled for the AWS connector
        ignore_test_connection (bool | Unset):
        credential (CeAwsCredential | Unset): This contains details of the CCM AWS connector credential
    """

    connector_type: str
    features_enabled: list[CEAwsConnectorFeaturesEnabledItem]
    cross_account_access: CrossAccountAccess | Unset = UNSET
    cur_attributes: AwsCurAttributes | Unset = UNSET
    aws_account_id: str | Unset = UNSET
    is_aws_gov_cloud_account: bool | Unset = UNSET
    autostopping_features: list[CEAwsConnectorAutostoppingFeaturesItem] | Unset = UNSET
    commitment_features: list[CEAwsConnectorCommitmentFeaturesItem] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    credential: CeAwsCredential | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        features_enabled = []
        for features_enabled_item_data in self.features_enabled:
            features_enabled_item: str = features_enabled_item_data
            features_enabled.append(features_enabled_item)

        cross_account_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_account_access, Unset):
            cross_account_access = self.cross_account_access.to_dict()

        cur_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cur_attributes, Unset):
            cur_attributes = self.cur_attributes.to_dict()

        aws_account_id = self.aws_account_id

        is_aws_gov_cloud_account = self.is_aws_gov_cloud_account

        autostopping_features: list[str] | Unset = UNSET
        if not isinstance(self.autostopping_features, Unset):
            autostopping_features = []
            for autostopping_features_item_data in self.autostopping_features:
                autostopping_features_item: str = autostopping_features_item_data
                autostopping_features.append(autostopping_features_item)

        commitment_features: list[str] | Unset = UNSET
        if not isinstance(self.commitment_features, Unset):
            commitment_features = []
            for commitment_features_item_data in self.commitment_features:
                commitment_features_item: str = commitment_features_item_data
                commitment_features.append(commitment_features_item)

        ignore_test_connection = self.ignore_test_connection

        credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "featuresEnabled": features_enabled,
            }
        )
        if cross_account_access is not UNSET:
            field_dict["crossAccountAccess"] = cross_account_access
        if cur_attributes is not UNSET:
            field_dict["curAttributes"] = cur_attributes
        if aws_account_id is not UNSET:
            field_dict["awsAccountId"] = aws_account_id
        if is_aws_gov_cloud_account is not UNSET:
            field_dict["isAWSGovCloudAccount"] = is_aws_gov_cloud_account
        if autostopping_features is not UNSET:
            field_dict["autostoppingFeatures"] = autostopping_features
        if commitment_features is not UNSET:
            field_dict["commitmentFeatures"] = commitment_features
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection
        if credential is not UNSET:
            field_dict["credential"] = credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_cur_attributes import AwsCurAttributes
        from ..models.ce_aws_credential import CeAwsCredential
        from ..models.cross_account_access import CrossAccountAccess

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        features_enabled = []
        _features_enabled = d.pop("featuresEnabled")
        for features_enabled_item_data in _features_enabled:
            features_enabled_item = check_ce_aws_connector_features_enabled_item(features_enabled_item_data)

            features_enabled.append(features_enabled_item)

        _cross_account_access = d.pop("crossAccountAccess", UNSET)
        cross_account_access: CrossAccountAccess | Unset
        if isinstance(_cross_account_access, Unset):
            cross_account_access = UNSET
        else:
            cross_account_access = CrossAccountAccess.from_dict(_cross_account_access)

        _cur_attributes = d.pop("curAttributes", UNSET)
        cur_attributes: AwsCurAttributes | Unset
        if isinstance(_cur_attributes, Unset):
            cur_attributes = UNSET
        else:
            cur_attributes = AwsCurAttributes.from_dict(_cur_attributes)

        aws_account_id = d.pop("awsAccountId", UNSET)

        is_aws_gov_cloud_account = d.pop("isAWSGovCloudAccount", UNSET)

        _autostopping_features = d.pop("autostoppingFeatures", UNSET)
        autostopping_features: list[CEAwsConnectorAutostoppingFeaturesItem] | Unset = UNSET
        if _autostopping_features is not UNSET:
            autostopping_features = []
            for autostopping_features_item_data in _autostopping_features:
                autostopping_features_item = check_ce_aws_connector_autostopping_features_item(
                    autostopping_features_item_data
                )

                autostopping_features.append(autostopping_features_item)

        _commitment_features = d.pop("commitmentFeatures", UNSET)
        commitment_features: list[CEAwsConnectorCommitmentFeaturesItem] | Unset = UNSET
        if _commitment_features is not UNSET:
            commitment_features = []
            for commitment_features_item_data in _commitment_features:
                commitment_features_item = check_ce_aws_connector_commitment_features_item(
                    commitment_features_item_data
                )

                commitment_features.append(commitment_features_item)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        _credential = d.pop("credential", UNSET)
        credential: CeAwsCredential | Unset
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = CeAwsCredential.from_dict(_credential)

        ce_aws_connector = cls(
            connector_type=connector_type,
            features_enabled=features_enabled,
            cross_account_access=cross_account_access,
            cur_attributes=cur_attributes,
            aws_account_id=aws_account_id,
            is_aws_gov_cloud_account=is_aws_gov_cloud_account,
            autostopping_features=autostopping_features,
            commitment_features=commitment_features,
            ignore_test_connection=ignore_test_connection,
            credential=credential,
        )

        ce_aws_connector.additional_properties = d
        return ce_aws_connector

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

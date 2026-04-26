from typing import Literal, cast

CEAwsConnectorCommitmentFeaturesItem = Literal["EC2", "ElastiCache", "RDS"]

CE_AWS_CONNECTOR_COMMITMENT_FEATURES_ITEM_VALUES: set[CEAwsConnectorCommitmentFeaturesItem] = {
    "EC2",
    "ElastiCache",
    "RDS",
}


def check_ce_aws_connector_commitment_features_item(value: str) -> CEAwsConnectorCommitmentFeaturesItem:
    if value in CE_AWS_CONNECTOR_COMMITMENT_FEATURES_ITEM_VALUES:
        return cast(CEAwsConnectorCommitmentFeaturesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CE_AWS_CONNECTOR_COMMITMENT_FEATURES_ITEM_VALUES!r}")

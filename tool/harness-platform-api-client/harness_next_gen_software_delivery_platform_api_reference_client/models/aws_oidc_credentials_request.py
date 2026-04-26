from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_oidc_token_request import AwsOidcTokenRequest
    from ..models.aws_sdk_retry_policy_spec import AwsSdkRetryPolicySpec


T = TypeVar("T", bound="AwsOidcCredentialsRequest")


@_attrs_define
class AwsOidcCredentialsRequest:
    """This contains Aws OIDC Credentials request details

    Attributes:
        iam_role_arn (str): IAM Role ARN
        oidc_id_token (str | Unset): The OIDC ID Token
        retry_policy (AwsSdkRetryPolicySpec | Unset): Retry policy for aws sdk calls
        aws_oidc_token_request_dto (AwsOidcTokenRequest | Unset): This contains AWS OIDC Token request details
    """

    iam_role_arn: str
    oidc_id_token: str | Unset = UNSET
    retry_policy: AwsSdkRetryPolicySpec | Unset = UNSET
    aws_oidc_token_request_dto: AwsOidcTokenRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iam_role_arn = self.iam_role_arn

        oidc_id_token = self.oidc_id_token

        retry_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_policy, Unset):
            retry_policy = self.retry_policy.to_dict()

        aws_oidc_token_request_dto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_oidc_token_request_dto, Unset):
            aws_oidc_token_request_dto = self.aws_oidc_token_request_dto.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iamRoleArn": iam_role_arn,
            }
        )
        if oidc_id_token is not UNSET:
            field_dict["oidcIdToken"] = oidc_id_token
        if retry_policy is not UNSET:
            field_dict["retryPolicy"] = retry_policy
        if aws_oidc_token_request_dto is not UNSET:
            field_dict["awsOidcTokenRequestDto"] = aws_oidc_token_request_dto

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_oidc_token_request import AwsOidcTokenRequest
        from ..models.aws_sdk_retry_policy_spec import AwsSdkRetryPolicySpec

        d = dict(src_dict)
        iam_role_arn = d.pop("iamRoleArn")

        oidc_id_token = d.pop("oidcIdToken", UNSET)

        _retry_policy = d.pop("retryPolicy", UNSET)
        retry_policy: AwsSdkRetryPolicySpec | Unset
        if isinstance(_retry_policy, Unset):
            retry_policy = UNSET
        else:
            retry_policy = AwsSdkRetryPolicySpec.from_dict(_retry_policy)

        _aws_oidc_token_request_dto = d.pop("awsOidcTokenRequestDto", UNSET)
        aws_oidc_token_request_dto: AwsOidcTokenRequest | Unset
        if isinstance(_aws_oidc_token_request_dto, Unset):
            aws_oidc_token_request_dto = UNSET
        else:
            aws_oidc_token_request_dto = AwsOidcTokenRequest.from_dict(_aws_oidc_token_request_dto)

        aws_oidc_credentials_request = cls(
            iam_role_arn=iam_role_arn,
            oidc_id_token=oidc_id_token,
            retry_policy=retry_policy,
            aws_oidc_token_request_dto=aws_oidc_token_request_dto,
        )

        aws_oidc_credentials_request.additional_properties = d
        return aws_oidc_credentials_request

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

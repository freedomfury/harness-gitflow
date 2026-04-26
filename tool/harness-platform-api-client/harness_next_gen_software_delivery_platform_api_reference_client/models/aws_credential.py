from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_credential_type import AwsCredentialType, check_aws_credential_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_credential_spec import AwsCredentialSpec
    from ..models.cross_account_access import CrossAccountAccess


T = TypeVar("T", bound="AwsCredential")


@_attrs_define
class AwsCredential:
    """This contains details of the AWS connector credential

    Attributes:
        type_ (AwsCredentialType):
        cross_account_access (CrossAccountAccess | Unset): This contains AWS connector cross account access details
        spec (AwsCredentialSpec | Unset): This contains AWS connector credential spec
        region (str | Unset):
    """

    type_: AwsCredentialType
    cross_account_access: CrossAccountAccess | Unset = UNSET
    spec: AwsCredentialSpec | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        cross_account_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_account_access, Unset):
            cross_account_access = self.cross_account_access.to_dict()

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if cross_account_access is not UNSET:
            field_dict["crossAccountAccess"] = cross_account_access
        if spec is not UNSET:
            field_dict["spec"] = spec
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_credential_spec import AwsCredentialSpec
        from ..models.cross_account_access import CrossAccountAccess

        d = dict(src_dict)
        type_ = check_aws_credential_type(d.pop("type"))

        _cross_account_access = d.pop("crossAccountAccess", UNSET)
        cross_account_access: CrossAccountAccess | Unset
        if isinstance(_cross_account_access, Unset):
            cross_account_access = UNSET
        else:
            cross_account_access = CrossAccountAccess.from_dict(_cross_account_access)

        _spec = d.pop("spec", UNSET)
        spec: AwsCredentialSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AwsCredentialSpec.from_dict(_spec)

        region = d.pop("region", UNSET)

        aws_credential = cls(
            type_=type_,
            cross_account_access=cross_account_access,
            spec=spec,
            region=region,
        )

        aws_credential.additional_properties = d
        return aws_credential

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

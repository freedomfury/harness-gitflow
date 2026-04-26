from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bitbucket_api_access_type import BitbucketApiAccessType, check_bitbucket_api_access_type

if TYPE_CHECKING:
    from ..models.bitbucket_api_access import BitbucketApiAccess


T = TypeVar("T", bound="BitbucketOauth")


@_attrs_define
class BitbucketOauth:
    """This contains details of the information such as references of tokens needed for OAuth API access

    Attributes:
        type_ (BitbucketApiAccessType):
        spec (BitbucketApiAccess): This contains details of the information needed for Bitbucket API access
        token_ref (str):
        refresh_token_ref (str):
    """

    type_: BitbucketApiAccessType
    spec: BitbucketApiAccess
    token_ref: str
    refresh_token_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        token_ref = self.token_ref

        refresh_token_ref = self.refresh_token_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
                "tokenRef": token_ref,
                "refreshTokenRef": refresh_token_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bitbucket_api_access import BitbucketApiAccess

        d = dict(src_dict)
        type_ = check_bitbucket_api_access_type(d.pop("type"))

        spec = BitbucketApiAccess.from_dict(d.pop("spec"))

        token_ref = d.pop("tokenRef")

        refresh_token_ref = d.pop("refreshTokenRef")

        bitbucket_oauth = cls(
            type_=type_,
            spec=spec,
            token_ref=token_ref,
            refresh_token_ref=refresh_token_ref,
        )

        bitbucket_oauth.additional_properties = d
        return bitbucket_oauth

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

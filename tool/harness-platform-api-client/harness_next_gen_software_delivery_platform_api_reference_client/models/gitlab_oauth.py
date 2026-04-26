from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GitlabOauth")


@_attrs_define
class GitlabOauth:
    """This contains details of the information such as references of tokens needed for Gitlab API access

    Attributes:
        token_ref (str):
        refresh_token_ref (str):
    """

    token_ref: str
    refresh_token_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_ref = self.token_ref

        refresh_token_ref = self.refresh_token_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenRef": token_ref,
                "refreshTokenRef": refresh_token_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_ref = d.pop("tokenRef")

        refresh_token_ref = d.pop("refreshTokenRef")

        gitlab_oauth = cls(
            token_ref=token_ref,
            refresh_token_ref=refresh_token_ref,
        )

        gitlab_oauth.additional_properties = d
        return gitlab_oauth

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

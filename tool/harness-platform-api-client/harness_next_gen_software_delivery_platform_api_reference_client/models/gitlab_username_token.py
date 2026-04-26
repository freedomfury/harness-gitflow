from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitlabUsernameToken")


@_attrs_define
class GitlabUsernameToken:
    """This contains details of the Gitlab credentials Specs such as references of username and token

    Attributes:
        token_ref (str):
        username (str | Unset):
        username_ref (str | Unset):
    """

    token_ref: str
    username: str | Unset = UNSET
    username_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_ref = self.token_ref

        username = self.username

        username_ref = self.username_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenRef": token_ref,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if username_ref is not UNSET:
            field_dict["usernameRef"] = username_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_ref = d.pop("tokenRef")

        username = d.pop("username", UNSET)

        username_ref = d.pop("usernameRef", UNSET)

        gitlab_username_token = cls(
            token_ref=token_ref,
            username=username,
            username_ref=username_ref,
        )

        gitlab_username_token.additional_properties = d
        return gitlab_username_token

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

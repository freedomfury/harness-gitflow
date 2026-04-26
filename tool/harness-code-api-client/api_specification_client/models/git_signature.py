from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git_identity_type_0 import GitIdentityType0


T = TypeVar("T", bound="GitSignature")


@_attrs_define
class GitSignature:
    """
    Attributes:
        identity (GitIdentityType0 | None | Unset):
        when (datetime.datetime | Unset):
    """

    identity: GitIdentityType0 | None | Unset = UNSET
    when: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.git_identity_type_0 import GitIdentityType0

        identity: dict[str, Any] | None | Unset
        if isinstance(self.identity, Unset):
            identity = UNSET
        elif isinstance(self.identity, GitIdentityType0):
            identity = self.identity.to_dict()
        else:
            identity = self.identity

        when: str | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity is not UNSET:
            field_dict["identity"] = identity
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_identity_type_0 import GitIdentityType0

        d = dict(src_dict)

        def _parse_identity(data: object) -> GitIdentityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_git_identity_type_0 = GitIdentityType0.from_dict(data)

                return componentsschemas_git_identity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GitIdentityType0 | None | Unset, data)

        identity = _parse_identity(d.pop("identity", UNSET))

        _when = d.pop("when", UNSET)
        when: datetime.datetime | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        git_signature = cls(
            identity=identity,
            when=when,
        )

        git_signature.additional_properties = d
        return git_signature

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

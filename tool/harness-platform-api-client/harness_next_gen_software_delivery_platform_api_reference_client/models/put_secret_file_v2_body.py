from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_secret_file_v2_body_file import PutSecretFileV2BodyFile


T = TypeVar("T", bound="PutSecretFileV2Body")


@_attrs_define
class PutSecretFileV2Body:
    """
    Attributes:
        file (PutSecretFileV2BodyFile | Unset): This is the encrypted Secret File that needs to be uploaded.
        spec (str | Unset): Specification of Secret file
    """

    file: PutSecretFileV2BodyFile | Unset = UNSET
    spec: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        spec = self.spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            files.append(("file", (None, json.dumps(self.file.to_dict()).encode(), "application/json")))

        if not isinstance(self.spec, Unset):
            files.append(("spec", (None, str(self.spec).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_secret_file_v2_body_file import PutSecretFileV2BodyFile

        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: PutSecretFileV2BodyFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = PutSecretFileV2BodyFile.from_dict(_file)

        spec = d.pop("spec", UNSET)

        put_secret_file_v2_body = cls(
            file=file,
            spec=spec,
        )

        put_secret_file_v2_body.additional_properties = d
        return put_secret_file_v2_body

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

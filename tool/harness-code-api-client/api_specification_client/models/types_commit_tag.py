from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit import TypesCommit
    from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0
    from ..models.types_signature import TypesSignature


T = TypeVar("T", bound="TypesCommitTag")


@_attrs_define
class TypesCommitTag:
    """
    Attributes:
        commit (TypesCommit | Unset):
        is_annotated (bool | Unset):
        message (str | Unset):
        name (str | Unset):
        sha (str | Unset): Git object hash
        signature (None | TypesGitSignatureResultType0 | Unset):
        tagger (TypesSignature | Unset):
        title (str | Unset):
    """

    commit: TypesCommit | Unset = UNSET
    is_annotated: bool | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    sha: str | Unset = UNSET
    signature: None | TypesGitSignatureResultType0 | Unset = UNSET
    tagger: TypesSignature | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        is_annotated = self.is_annotated

        message = self.message

        name = self.name

        sha = self.sha

        signature: dict[str, Any] | None | Unset
        if isinstance(self.signature, Unset):
            signature = UNSET
        elif isinstance(self.signature, TypesGitSignatureResultType0):
            signature = self.signature.to_dict()
        else:
            signature = self.signature

        tagger: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tagger, Unset):
            tagger = self.tagger.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if is_annotated is not UNSET:
            field_dict["is_annotated"] = is_annotated
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if sha is not UNSET:
            field_dict["sha"] = sha
        if signature is not UNSET:
            field_dict["signature"] = signature
        if tagger is not UNSET:
            field_dict["tagger"] = tagger
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit import TypesCommit
        from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0
        from ..models.types_signature import TypesSignature

        d = dict(src_dict)
        _commit = d.pop("commit", UNSET)
        commit: TypesCommit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = TypesCommit.from_dict(_commit)

        is_annotated = d.pop("is_annotated", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        sha = d.pop("sha", UNSET)

        def _parse_signature(data: object) -> None | TypesGitSignatureResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_git_signature_result_type_0 = TypesGitSignatureResultType0.from_dict(data)

                return componentsschemas_types_git_signature_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesGitSignatureResultType0 | Unset, data)

        signature = _parse_signature(d.pop("signature", UNSET))

        _tagger = d.pop("tagger", UNSET)
        tagger: TypesSignature | Unset
        if isinstance(_tagger, Unset):
            tagger = UNSET
        else:
            tagger = TypesSignature.from_dict(_tagger)

        title = d.pop("title", UNSET)

        types_commit_tag = cls(
            commit=commit,
            is_annotated=is_annotated,
            message=message,
            name=name,
            sha=sha,
            signature=signature,
            tagger=tagger,
            title=title,
        )

        types_commit_tag.additional_properties = d
        return types_commit_tag

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

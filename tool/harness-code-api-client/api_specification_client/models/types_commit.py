from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_commit_stats import TypesCommitStats
    from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0
    from ..models.types_signature import TypesSignature


T = TypeVar("T", bound="TypesCommit")


@_attrs_define
class TypesCommit:
    """
    Attributes:
        author (TypesSignature | Unset):
        committer (TypesSignature | Unset):
        message (str | Unset):
        parent_shas (list[str] | Unset):
        sha (str | Unset): Git object hash
        signature (None | TypesGitSignatureResultType0 | Unset):
        stats (TypesCommitStats | Unset):
        title (str | Unset):
    """

    author: TypesSignature | Unset = UNSET
    committer: TypesSignature | Unset = UNSET
    message: str | Unset = UNSET
    parent_shas: list[str] | Unset = UNSET
    sha: str | Unset = UNSET
    signature: None | TypesGitSignatureResultType0 | Unset = UNSET
    stats: TypesCommitStats | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        message = self.message

        parent_shas: list[str] | Unset = UNSET
        if not isinstance(self.parent_shas, Unset):
            parent_shas = self.parent_shas

        sha = self.sha

        signature: dict[str, Any] | None | Unset
        if isinstance(self.signature, Unset):
            signature = UNSET
        elif isinstance(self.signature, TypesGitSignatureResultType0):
            signature = self.signature.to_dict()
        else:
            signature = self.signature

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if message is not UNSET:
            field_dict["message"] = message
        if parent_shas is not UNSET:
            field_dict["parent_shas"] = parent_shas
        if sha is not UNSET:
            field_dict["sha"] = sha
        if signature is not UNSET:
            field_dict["signature"] = signature
        if stats is not UNSET:
            field_dict["stats"] = stats
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_commit_stats import TypesCommitStats
        from ..models.types_git_signature_result_type_0 import TypesGitSignatureResultType0
        from ..models.types_signature import TypesSignature

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: TypesSignature | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = TypesSignature.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: TypesSignature | Unset
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = TypesSignature.from_dict(_committer)

        message = d.pop("message", UNSET)

        parent_shas = cast(list[str], d.pop("parent_shas", UNSET))

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

        _stats = d.pop("stats", UNSET)
        stats: TypesCommitStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = TypesCommitStats.from_dict(_stats)

        title = d.pop("title", UNSET)

        types_commit = cls(
            author=author,
            committer=committer,
            message=message,
            parent_shas=parent_shas,
            sha=sha,
            signature=signature,
            stats=stats,
            title=title,
        )

        types_commit.additional_properties = d
        return types_commit

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

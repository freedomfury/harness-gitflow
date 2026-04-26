from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_pull_req_activity_mentions_metadata import TypesPullReqActivityMentionsMetadata
    from ..models.types_pull_req_activity_suggestions_metadata import TypesPullReqActivitySuggestionsMetadata


T = TypeVar("T", bound="TypesPullReqActivityMetadata")


@_attrs_define
class TypesPullReqActivityMetadata:
    """
    Attributes:
        mentions (TypesPullReqActivityMentionsMetadata | Unset):
        suggestions (TypesPullReqActivitySuggestionsMetadata | Unset):
    """

    mentions: TypesPullReqActivityMentionsMetadata | Unset = UNSET
    suggestions: TypesPullReqActivitySuggestionsMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions.to_dict()

        suggestions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = self.suggestions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_pull_req_activity_mentions_metadata import TypesPullReqActivityMentionsMetadata
        from ..models.types_pull_req_activity_suggestions_metadata import TypesPullReqActivitySuggestionsMetadata

        d = dict(src_dict)
        _mentions = d.pop("mentions", UNSET)
        mentions: TypesPullReqActivityMentionsMetadata | Unset
        if isinstance(_mentions, Unset):
            mentions = UNSET
        else:
            mentions = TypesPullReqActivityMentionsMetadata.from_dict(_mentions)

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: TypesPullReqActivitySuggestionsMetadata | Unset
        if isinstance(_suggestions, Unset):
            suggestions = UNSET
        else:
            suggestions = TypesPullReqActivitySuggestionsMetadata.from_dict(_suggestions)

        types_pull_req_activity_metadata = cls(
            mentions=mentions,
            suggestions=suggestions,
        )

        types_pull_req_activity_metadata.additional_properties = d
        return types_pull_req_activity_metadata

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

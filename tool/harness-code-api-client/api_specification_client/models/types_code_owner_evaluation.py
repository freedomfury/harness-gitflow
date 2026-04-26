from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_code_owner_evaluation_entry import TypesCodeOwnerEvaluationEntry


T = TypeVar("T", bound="TypesCodeOwnerEvaluation")


@_attrs_define
class TypesCodeOwnerEvaluation:
    """
    Attributes:
        evaluation_entries (list[TypesCodeOwnerEvaluationEntry] | None | Unset):
        file_sha (str | Unset):
    """

    evaluation_entries: list[TypesCodeOwnerEvaluationEntry] | None | Unset = UNSET
    file_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluation_entries: list[dict[str, Any]] | None | Unset
        if isinstance(self.evaluation_entries, Unset):
            evaluation_entries = UNSET
        elif isinstance(self.evaluation_entries, list):
            evaluation_entries = []
            for evaluation_entries_type_0_item_data in self.evaluation_entries:
                evaluation_entries_type_0_item = evaluation_entries_type_0_item_data.to_dict()
                evaluation_entries.append(evaluation_entries_type_0_item)

        else:
            evaluation_entries = self.evaluation_entries

        file_sha = self.file_sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluation_entries is not UNSET:
            field_dict["evaluation_entries"] = evaluation_entries
        if file_sha is not UNSET:
            field_dict["file_sha"] = file_sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_code_owner_evaluation_entry import TypesCodeOwnerEvaluationEntry

        d = dict(src_dict)

        def _parse_evaluation_entries(data: object) -> list[TypesCodeOwnerEvaluationEntry] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evaluation_entries_type_0 = []
                _evaluation_entries_type_0 = data
                for evaluation_entries_type_0_item_data in _evaluation_entries_type_0:
                    evaluation_entries_type_0_item = TypesCodeOwnerEvaluationEntry.from_dict(
                        evaluation_entries_type_0_item_data
                    )

                    evaluation_entries_type_0.append(evaluation_entries_type_0_item)

                return evaluation_entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesCodeOwnerEvaluationEntry] | None | Unset, data)

        evaluation_entries = _parse_evaluation_entries(d.pop("evaluation_entries", UNSET))

        file_sha = d.pop("file_sha", UNSET)

        types_code_owner_evaluation = cls(
            evaluation_entries=evaluation_entries,
            file_sha=file_sha,
        )

        types_code_owner_evaluation.additional_properties = d
        return types_code_owner_evaluation

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

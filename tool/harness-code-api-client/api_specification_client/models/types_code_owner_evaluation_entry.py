from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_owner_evaluation import TypesOwnerEvaluation
    from ..models.types_user_group_owner_evaluation import TypesUserGroupOwnerEvaluation


T = TypeVar("T", bound="TypesCodeOwnerEvaluationEntry")


@_attrs_define
class TypesCodeOwnerEvaluationEntry:
    """
    Attributes:
        line_number (int | Unset):
        owner_evaluations (list[TypesOwnerEvaluation] | None | Unset):
        pattern (str | Unset):
        user_group_owner_evaluations (list[TypesUserGroupOwnerEvaluation] | None | Unset):
    """

    line_number: int | Unset = UNSET
    owner_evaluations: list[TypesOwnerEvaluation] | None | Unset = UNSET
    pattern: str | Unset = UNSET
    user_group_owner_evaluations: list[TypesUserGroupOwnerEvaluation] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        owner_evaluations: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_evaluations, Unset):
            owner_evaluations = UNSET
        elif isinstance(self.owner_evaluations, list):
            owner_evaluations = []
            for owner_evaluations_type_0_item_data in self.owner_evaluations:
                owner_evaluations_type_0_item = owner_evaluations_type_0_item_data.to_dict()
                owner_evaluations.append(owner_evaluations_type_0_item)

        else:
            owner_evaluations = self.owner_evaluations

        pattern = self.pattern

        user_group_owner_evaluations: list[dict[str, Any]] | None | Unset
        if isinstance(self.user_group_owner_evaluations, Unset):
            user_group_owner_evaluations = UNSET
        elif isinstance(self.user_group_owner_evaluations, list):
            user_group_owner_evaluations = []
            for user_group_owner_evaluations_type_0_item_data in self.user_group_owner_evaluations:
                user_group_owner_evaluations_type_0_item = user_group_owner_evaluations_type_0_item_data.to_dict()
                user_group_owner_evaluations.append(user_group_owner_evaluations_type_0_item)

        else:
            user_group_owner_evaluations = self.user_group_owner_evaluations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["line_number"] = line_number
        if owner_evaluations is not UNSET:
            field_dict["owner_evaluations"] = owner_evaluations
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if user_group_owner_evaluations is not UNSET:
            field_dict["user_group_owner_evaluations"] = user_group_owner_evaluations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_owner_evaluation import TypesOwnerEvaluation
        from ..models.types_user_group_owner_evaluation import TypesUserGroupOwnerEvaluation

        d = dict(src_dict)
        line_number = d.pop("line_number", UNSET)

        def _parse_owner_evaluations(data: object) -> list[TypesOwnerEvaluation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_evaluations_type_0 = []
                _owner_evaluations_type_0 = data
                for owner_evaluations_type_0_item_data in _owner_evaluations_type_0:
                    owner_evaluations_type_0_item = TypesOwnerEvaluation.from_dict(owner_evaluations_type_0_item_data)

                    owner_evaluations_type_0.append(owner_evaluations_type_0_item)

                return owner_evaluations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesOwnerEvaluation] | None | Unset, data)

        owner_evaluations = _parse_owner_evaluations(d.pop("owner_evaluations", UNSET))

        pattern = d.pop("pattern", UNSET)

        def _parse_user_group_owner_evaluations(data: object) -> list[TypesUserGroupOwnerEvaluation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_owner_evaluations_type_0 = []
                _user_group_owner_evaluations_type_0 = data
                for user_group_owner_evaluations_type_0_item_data in _user_group_owner_evaluations_type_0:
                    user_group_owner_evaluations_type_0_item = TypesUserGroupOwnerEvaluation.from_dict(
                        user_group_owner_evaluations_type_0_item_data
                    )

                    user_group_owner_evaluations_type_0.append(user_group_owner_evaluations_type_0_item)

                return user_group_owner_evaluations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesUserGroupOwnerEvaluation] | None | Unset, data)

        user_group_owner_evaluations = _parse_user_group_owner_evaluations(d.pop("user_group_owner_evaluations", UNSET))

        types_code_owner_evaluation_entry = cls(
            line_number=line_number,
            owner_evaluations=owner_evaluations,
            pattern=pattern,
            user_group_owner_evaluations=user_group_owner_evaluations,
        )

        types_code_owner_evaluation_entry.additional_properties = d
        return types_code_owner_evaluation_entry

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

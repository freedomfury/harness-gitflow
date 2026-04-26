from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_owner_evaluation import TypesOwnerEvaluation


T = TypeVar("T", bound="TypesUserGroupOwnerEvaluation")


@_attrs_define
class TypesUserGroupOwnerEvaluation:
    """
    Attributes:
        evaluations (list[TypesOwnerEvaluation] | None | Unset):
        id (str | Unset):
        name (str | Unset):
    """

    evaluations: list[TypesOwnerEvaluation] | None | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluations: list[dict[str, Any]] | None | Unset
        if isinstance(self.evaluations, Unset):
            evaluations = UNSET
        elif isinstance(self.evaluations, list):
            evaluations = []
            for evaluations_type_0_item_data in self.evaluations:
                evaluations_type_0_item = evaluations_type_0_item_data.to_dict()
                evaluations.append(evaluations_type_0_item)

        else:
            evaluations = self.evaluations

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_owner_evaluation import TypesOwnerEvaluation

        d = dict(src_dict)

        def _parse_evaluations(data: object) -> list[TypesOwnerEvaluation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evaluations_type_0 = []
                _evaluations_type_0 = data
                for evaluations_type_0_item_data in _evaluations_type_0:
                    evaluations_type_0_item = TypesOwnerEvaluation.from_dict(evaluations_type_0_item_data)

                    evaluations_type_0.append(evaluations_type_0_item)

                return evaluations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesOwnerEvaluation] | None | Unset, data)

        evaluations = _parse_evaluations(d.pop("evaluations", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        types_user_group_owner_evaluation = cls(
            evaluations=evaluations,
            id=id,
            name=name,
        )

        types_user_group_owner_evaluation.additional_properties = d
        return types_user_group_owner_evaluation

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

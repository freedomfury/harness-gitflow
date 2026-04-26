from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_label_assignment import TypesLabelAssignment
    from ..models.types_scope_data import TypesScopeData


T = TypeVar("T", bound="TypesScopesLabels")


@_attrs_define
class TypesScopesLabels:
    """
    Attributes:
        label_data (list[TypesLabelAssignment] | None | Unset):
        scope_data (list[TypesScopeData] | None | Unset):
    """

    label_data: list[TypesLabelAssignment] | None | Unset = UNSET
    scope_data: list[TypesScopeData] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_data: list[dict[str, Any]] | None | Unset
        if isinstance(self.label_data, Unset):
            label_data = UNSET
        elif isinstance(self.label_data, list):
            label_data = []
            for label_data_type_0_item_data in self.label_data:
                label_data_type_0_item = label_data_type_0_item_data.to_dict()
                label_data.append(label_data_type_0_item)

        else:
            label_data = self.label_data

        scope_data: list[dict[str, Any]] | None | Unset
        if isinstance(self.scope_data, Unset):
            scope_data = UNSET
        elif isinstance(self.scope_data, list):
            scope_data = []
            for scope_data_type_0_item_data in self.scope_data:
                scope_data_type_0_item = scope_data_type_0_item_data.to_dict()
                scope_data.append(scope_data_type_0_item)

        else:
            scope_data = self.scope_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label_data is not UNSET:
            field_dict["label_data"] = label_data
        if scope_data is not UNSET:
            field_dict["scope_data"] = scope_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_label_assignment import TypesLabelAssignment
        from ..models.types_scope_data import TypesScopeData

        d = dict(src_dict)

        def _parse_label_data(data: object) -> list[TypesLabelAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                label_data_type_0 = []
                _label_data_type_0 = data
                for label_data_type_0_item_data in _label_data_type_0:
                    label_data_type_0_item = TypesLabelAssignment.from_dict(label_data_type_0_item_data)

                    label_data_type_0.append(label_data_type_0_item)

                return label_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesLabelAssignment] | None | Unset, data)

        label_data = _parse_label_data(d.pop("label_data", UNSET))

        def _parse_scope_data(data: object) -> list[TypesScopeData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_data_type_0 = []
                _scope_data_type_0 = data
                for scope_data_type_0_item_data in _scope_data_type_0:
                    scope_data_type_0_item = TypesScopeData.from_dict(scope_data_type_0_item_data)

                    scope_data_type_0.append(scope_data_type_0_item)

                return scope_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesScopeData] | None | Unset, data)

        scope_data = _parse_scope_data(d.pop("scope_data", UNSET))

        types_scopes_labels = cls(
            label_data=label_data,
            scope_data=scope_data,
        )

        types_scopes_labels.additional_properties = d
        return types_scopes_labels

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.yaml_schema_error_dto import YamlSchemaErrorDTO


T = TypeVar("T", bound="YamlSchemaErrorWrapperDTO")


@_attrs_define
class YamlSchemaErrorWrapperDTO:
    """
    Attributes:
        schema_errors (list[YamlSchemaErrorDTO] | Unset):
        type_ (str | Unset):
    """

    schema_errors: list[YamlSchemaErrorDTO] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schema_errors, Unset):
            schema_errors = []
            for schema_errors_item_data in self.schema_errors:
                schema_errors_item = schema_errors_item_data.to_dict()
                schema_errors.append(schema_errors_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema_errors is not UNSET:
            field_dict["schemaErrors"] = schema_errors
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.yaml_schema_error_dto import YamlSchemaErrorDTO

        d = dict(src_dict)
        _schema_errors = d.pop("schemaErrors", UNSET)
        schema_errors: list[YamlSchemaErrorDTO] | Unset = UNSET
        if _schema_errors is not UNSET:
            schema_errors = []
            for schema_errors_item_data in _schema_errors:
                schema_errors_item = YamlSchemaErrorDTO.from_dict(schema_errors_item_data)

                schema_errors.append(schema_errors_item)

        type_ = d.pop("type", UNSET)

        yaml_schema_error_wrapper_dto = cls(
            schema_errors=schema_errors,
            type_=type_,
        )

        yaml_schema_error_wrapper_dto.additional_properties = d
        return yaml_schema_error_wrapper_dto

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

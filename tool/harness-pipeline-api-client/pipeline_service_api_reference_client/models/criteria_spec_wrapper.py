from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.criteria_spec_wrapper_type import CriteriaSpecWrapperType, check_criteria_spec_wrapper_type

if TYPE_CHECKING:
    from ..models.criteria_spec_dto import CriteriaSpecDTO


T = TypeVar("T", bound="CriteriaSpecWrapper")


@_attrs_define
class CriteriaSpecWrapper:
    """This contains details of Criteria Specifications such as Criteria Type

    Attributes:
        type_ (CriteriaSpecWrapperType):
        spec (CriteriaSpecDTO):
    """

    type_: CriteriaSpecWrapperType
    spec: CriteriaSpecDTO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_spec_dto import CriteriaSpecDTO

        d = dict(src_dict)
        type_ = check_criteria_spec_wrapper_type(d.pop("type"))

        spec = CriteriaSpecDTO.from_dict(d.pop("spec"))

        criteria_spec_wrapper = cls(
            type_=type_,
            spec=spec,
        )

        criteria_spec_wrapper.additional_properties = d
        return criteria_spec_wrapper

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

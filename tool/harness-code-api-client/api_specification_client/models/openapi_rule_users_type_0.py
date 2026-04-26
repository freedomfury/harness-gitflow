from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="OpenapiRuleUsersType0")


@_attrs_define
class OpenapiRuleUsersType0:
    """ """

    additional_properties: dict[str, None | TypesPrincipalInfoType0] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, TypesPrincipalInfoType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)
        openapi_rule_users_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> None | TypesPrincipalInfoType0:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                    return componentsschemas_types_principal_info_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(None | TypesPrincipalInfoType0, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        openapi_rule_users_type_0.additional_properties = additional_properties
        return openapi_rule_users_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> None | TypesPrincipalInfoType0:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: None | TypesPrincipalInfoType0) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

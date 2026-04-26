from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ml_flow_authentication_type import MLFlowAuthenticationType, check_ml_flow_authentication_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ml_flow_auth_credentials import MLFlowAuthCredentials


T = TypeVar("T", bound="MLFlowAuthentication")


@_attrs_define
class MLFlowAuthentication:
    """This entity contains the details for MLFlow Authentication

    Attributes:
        type_ (MLFlowAuthenticationType):
        spec (MLFlowAuthCredentials | Unset): This contains details of credentials for MLFlow Authentication
    """

    type_: MLFlowAuthenticationType
    spec: MLFlowAuthCredentials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ml_flow_auth_credentials import MLFlowAuthCredentials

        d = dict(src_dict)
        type_ = check_ml_flow_authentication_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: MLFlowAuthCredentials | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = MLFlowAuthCredentials.from_dict(_spec)

        ml_flow_authentication = cls(
            type_=type_,
            spec=spec,
        )

        ml_flow_authentication.additional_properties = d
        return ml_flow_authentication

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

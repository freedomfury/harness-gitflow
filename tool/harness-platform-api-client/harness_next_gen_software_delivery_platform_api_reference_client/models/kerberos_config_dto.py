from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kerberos_config_dto_tgt_generation_method import (
    KerberosConfigDTOTgtGenerationMethod,
    check_kerberos_config_dto_tgt_generation_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tgt_generation_spec_dto import TGTGenerationSpecDTO


T = TypeVar("T", bound="KerberosConfigDTO")


@_attrs_define
class KerberosConfigDTO:
    """
    Attributes:
        type_ (str):
        principal (str): This is the authorization role, the user/service has in the realm.
        realm (str): Name of the Realm.
        tgt_generation_method (KerberosConfigDTOTgtGenerationMethod | Unset):
        spec (TGTGenerationSpecDTO | Unset):
    """

    type_: str
    principal: str
    realm: str
    tgt_generation_method: KerberosConfigDTOTgtGenerationMethod | Unset = UNSET
    spec: TGTGenerationSpecDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        principal = self.principal

        realm = self.realm

        tgt_generation_method: str | Unset = UNSET
        if not isinstance(self.tgt_generation_method, Unset):
            tgt_generation_method = self.tgt_generation_method

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "principal": principal,
                "realm": realm,
            }
        )
        if tgt_generation_method is not UNSET:
            field_dict["tgtGenerationMethod"] = tgt_generation_method
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tgt_generation_spec_dto import TGTGenerationSpecDTO

        d = dict(src_dict)
        type_ = d.pop("type")

        principal = d.pop("principal")

        realm = d.pop("realm")

        _tgt_generation_method = d.pop("tgtGenerationMethod", UNSET)
        tgt_generation_method: KerberosConfigDTOTgtGenerationMethod | Unset
        if isinstance(_tgt_generation_method, Unset):
            tgt_generation_method = UNSET
        else:
            tgt_generation_method = check_kerberos_config_dto_tgt_generation_method(_tgt_generation_method)

        _spec = d.pop("spec", UNSET)
        spec: TGTGenerationSpecDTO | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = TGTGenerationSpecDTO.from_dict(_spec)

        kerberos_config_dto = cls(
            type_=type_,
            principal=principal,
            realm=realm,
            tgt_generation_method=tgt_generation_method,
            spec=spec,
        )

        kerberos_config_dto.additional_properties = d
        return kerberos_config_dto

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

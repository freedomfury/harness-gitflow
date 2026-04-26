from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kerberos_win_rm_config_dto_tgt_generation_method import (
    KerberosWinRmConfigDTOTgtGenerationMethod,
    check_kerberos_win_rm_config_dto_tgt_generation_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tgt_generation_spec_dto import TGTGenerationSpecDTO


T = TypeVar("T", bound="KerberosWinRmConfigDTO")


@_attrs_define
class KerberosWinRmConfigDTO:
    """
    Attributes:
        type_ (str):
        principal (str): This is the authorization role, the user/service has in the realm.
        realm (str): Name of the Realm.
        tgt_generation_method (KerberosWinRmConfigDTOTgtGenerationMethod | Unset):
        spec (TGTGenerationSpecDTO | Unset):
        use_ssl (bool | Unset): This is the Kerberos either to use SSL/https .
        skip_cert_checks (bool | Unset): This is the Kerberos either to skip certificate checks .
        use_no_profile (bool | Unset): This is the Kerberos powershell runs without loading profile .
    """

    type_: str
    principal: str
    realm: str
    tgt_generation_method: KerberosWinRmConfigDTOTgtGenerationMethod | Unset = UNSET
    spec: TGTGenerationSpecDTO | Unset = UNSET
    use_ssl: bool | Unset = UNSET
    skip_cert_checks: bool | Unset = UNSET
    use_no_profile: bool | Unset = UNSET
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

        use_ssl = self.use_ssl

        skip_cert_checks = self.skip_cert_checks

        use_no_profile = self.use_no_profile

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
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if skip_cert_checks is not UNSET:
            field_dict["skipCertChecks"] = skip_cert_checks
        if use_no_profile is not UNSET:
            field_dict["useNoProfile"] = use_no_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tgt_generation_spec_dto import TGTGenerationSpecDTO

        d = dict(src_dict)
        type_ = d.pop("type")

        principal = d.pop("principal")

        realm = d.pop("realm")

        _tgt_generation_method = d.pop("tgtGenerationMethod", UNSET)
        tgt_generation_method: KerberosWinRmConfigDTOTgtGenerationMethod | Unset
        if isinstance(_tgt_generation_method, Unset):
            tgt_generation_method = UNSET
        else:
            tgt_generation_method = check_kerberos_win_rm_config_dto_tgt_generation_method(_tgt_generation_method)

        _spec = d.pop("spec", UNSET)
        spec: TGTGenerationSpecDTO | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = TGTGenerationSpecDTO.from_dict(_spec)

        use_ssl = d.pop("useSSL", UNSET)

        skip_cert_checks = d.pop("skipCertChecks", UNSET)

        use_no_profile = d.pop("useNoProfile", UNSET)

        kerberos_win_rm_config_dto = cls(
            type_=type_,
            principal=principal,
            realm=realm,
            tgt_generation_method=tgt_generation_method,
            spec=spec,
            use_ssl=use_ssl,
            skip_cert_checks=skip_cert_checks,
            use_no_profile=use_no_profile,
        )

        kerberos_win_rm_config_dto.additional_properties = d
        return kerberos_win_rm_config_dto

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

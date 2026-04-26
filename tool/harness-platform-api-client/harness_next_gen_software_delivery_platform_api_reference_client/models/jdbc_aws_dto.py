from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jdbc_aws_dto_type import JDBCAwsDTOType, check_jdbc_aws_dto_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_credential_spec import AwsCredentialSpec


T = TypeVar("T", bound="JDBCAwsDTO")


@_attrs_define
class JDBCAwsDTO:
    """This contains JDBC AWS authentication details

    Attributes:
        type_ (JDBCAwsDTOType):
        spec (AwsCredentialSpec | Unset): This contains AWS connector credential spec
    """

    type_: JDBCAwsDTOType
    spec: AwsCredentialSpec | Unset = UNSET
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
        from ..models.aws_credential_spec import AwsCredentialSpec

        d = dict(src_dict)
        type_ = check_jdbc_aws_dto_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: AwsCredentialSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AwsCredentialSpec.from_dict(_spec)

        jdbc_aws_dto = cls(
            type_=type_,
            spec=spec,
        )

        jdbc_aws_dto.additional_properties = d
        return jdbc_aws_dto

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

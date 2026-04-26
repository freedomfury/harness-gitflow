from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.win_rm_auth_type import WinRmAuthType, check_win_rm_auth_type

if TYPE_CHECKING:
    from ..models.base_win_rm_spec import BaseWinRmSpec


T = TypeVar("T", bound="WinRmAuth")


@_attrs_define
class WinRmAuth:
    """This is the WinRm Authentication specification defined in Harness.

    Attributes:
        spec (BaseWinRmSpec): This is the WinRm specification details as defined in Harness.
        type_ (WinRmAuthType): Specifies authentication scheme, NTLM or Kerberos
    """

    spec: BaseWinRmSpec
    type_: WinRmAuthType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        type_: str = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spec": spec,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_win_rm_spec import BaseWinRmSpec

        d = dict(src_dict)
        spec = BaseWinRmSpec.from_dict(d.pop("spec"))

        type_ = check_win_rm_auth_type(d.pop("type"))

        win_rm_auth = cls(
            spec=spec,
            type_=type_,
        )

        win_rm_auth.additional_properties = d
        return win_rm_auth

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

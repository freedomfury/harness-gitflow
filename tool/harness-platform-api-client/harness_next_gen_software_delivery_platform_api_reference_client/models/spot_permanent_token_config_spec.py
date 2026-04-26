from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotPermanentTokenConfigSpec")


@_attrs_define
class SpotPermanentTokenConfigSpec:
    """This contains Spot permanent token connector spec

    Attributes:
        api_token_ref (str):
        spot_account_id (str | Unset):
        spot_account_id_ref (str | Unset):
    """

    api_token_ref: str
    spot_account_id: str | Unset = UNSET
    spot_account_id_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_token_ref = self.api_token_ref

        spot_account_id = self.spot_account_id

        spot_account_id_ref = self.spot_account_id_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiTokenRef": api_token_ref,
            }
        )
        if spot_account_id is not UNSET:
            field_dict["spotAccountId"] = spot_account_id
        if spot_account_id_ref is not UNSET:
            field_dict["spotAccountIdRef"] = spot_account_id_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_token_ref = d.pop("apiTokenRef")

        spot_account_id = d.pop("spotAccountId", UNSET)

        spot_account_id_ref = d.pop("spotAccountIdRef", UNSET)

        spot_permanent_token_config_spec = cls(
            api_token_ref=api_token_ref,
            spot_account_id=spot_account_id,
            spot_account_id_ref=spot_account_id_ref,
        )

        spot_permanent_token_config_spec.additional_properties = d
        return spot_permanent_token_config_spec

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

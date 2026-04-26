from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_public_key_request_revocation_reason import (
    UpdatePublicKeyRequestRevocationReason,
    check_update_public_key_request_revocation_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePublicKeyRequest")


@_attrs_define
class UpdatePublicKeyRequest:
    """Request to update public key (SSH/PGP) validity or revocation status

    Attributes:
        revocation_reason (UpdatePublicKeyRequestRevocationReason | Unset): Revocation reason. Cannot be combined with
            validFrom/validTo.
        valid_from (int | Unset): Start of validity period (epoch millis). Cannot be combined with revocationReason.
        valid_to (int | Unset): End of validity period (epoch millis). Cannot be combined with revocationReason.
    """

    revocation_reason: UpdatePublicKeyRequestRevocationReason | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revocation_reason: str | Unset = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: UpdatePublicKeyRequestRevocationReason | Unset
        if isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = check_update_public_key_request_revocation_reason(_revocation_reason)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        update_public_key_request = cls(
            revocation_reason=revocation_reason,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        update_public_key_request.additional_properties = d
        return update_public_key_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordStrengthPolicy")


@_attrs_define
class PasswordStrengthPolicy:
    """This has information about the password strength policy in Harness.

    Attributes:
        enabled (bool | Unset): This value is true if the password strength policy is enabled. Otherwise, it is false.
        min_number_of_characters (int | Unset): Minimum number of characters required in a password.
        min_number_of_uppercase_characters (int | Unset): Minimum number of uppercase characters required in a password.
        min_number_of_lowercase_characters (int | Unset): Minimum number of lower characters required in a password.
        min_number_of_special_characters (int | Unset): Minimum number of special characters required in a password.
        min_number_of_digits (int | Unset): Minimum number of digits required in a password.
    """

    enabled: bool | Unset = UNSET
    min_number_of_characters: int | Unset = UNSET
    min_number_of_uppercase_characters: int | Unset = UNSET
    min_number_of_lowercase_characters: int | Unset = UNSET
    min_number_of_special_characters: int | Unset = UNSET
    min_number_of_digits: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        min_number_of_characters = self.min_number_of_characters

        min_number_of_uppercase_characters = self.min_number_of_uppercase_characters

        min_number_of_lowercase_characters = self.min_number_of_lowercase_characters

        min_number_of_special_characters = self.min_number_of_special_characters

        min_number_of_digits = self.min_number_of_digits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if min_number_of_characters is not UNSET:
            field_dict["minNumberOfCharacters"] = min_number_of_characters
        if min_number_of_uppercase_characters is not UNSET:
            field_dict["minNumberOfUppercaseCharacters"] = min_number_of_uppercase_characters
        if min_number_of_lowercase_characters is not UNSET:
            field_dict["minNumberOfLowercaseCharacters"] = min_number_of_lowercase_characters
        if min_number_of_special_characters is not UNSET:
            field_dict["minNumberOfSpecialCharacters"] = min_number_of_special_characters
        if min_number_of_digits is not UNSET:
            field_dict["minNumberOfDigits"] = min_number_of_digits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        min_number_of_characters = d.pop("minNumberOfCharacters", UNSET)

        min_number_of_uppercase_characters = d.pop("minNumberOfUppercaseCharacters", UNSET)

        min_number_of_lowercase_characters = d.pop("minNumberOfLowercaseCharacters", UNSET)

        min_number_of_special_characters = d.pop("minNumberOfSpecialCharacters", UNSET)

        min_number_of_digits = d.pop("minNumberOfDigits", UNSET)

        password_strength_policy = cls(
            enabled=enabled,
            min_number_of_characters=min_number_of_characters,
            min_number_of_uppercase_characters=min_number_of_uppercase_characters,
            min_number_of_lowercase_characters=min_number_of_lowercase_characters,
            min_number_of_special_characters=min_number_of_special_characters,
            min_number_of_digits=min_number_of_digits,
        )

        password_strength_policy.additional_properties = d
        return password_strength_policy

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

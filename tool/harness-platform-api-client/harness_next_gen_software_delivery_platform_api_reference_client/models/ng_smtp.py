from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.smtp_config import SmtpConfig


T = TypeVar("T", bound="NgSmtp")


@_attrs_define
class NgSmtp:
    """This is the view of the NgSmtp entity defined in Harness

    Attributes:
        account_id (str): Account Identifier for the Entity.
        name (str): Name of the SMTP config.
        value (SmtpConfig): This has the SMTP configuration details defined in Harness.
        uuid (str | Unset): Identifier of the SMTP config.
    """

    account_id: str
    name: str
    value: SmtpConfig
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        name = self.name

        value = self.value.to_dict()

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "name": name,
                "value": value,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smtp_config import SmtpConfig

        d = dict(src_dict)
        account_id = d.pop("accountId")

        name = d.pop("name")

        value = SmtpConfig.from_dict(d.pop("value"))

        uuid = d.pop("uuid", UNSET)

        ng_smtp = cls(
            account_id=account_id,
            name=name,
            value=value,
            uuid=uuid,
        )

        ng_smtp.additional_properties = d
        return ng_smtp

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

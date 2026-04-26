from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.host_validation_dto_status import HostValidationDTOStatus, check_host_validation_dto_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="HostValidationDTO")


@_attrs_define
class HostValidationDTO:
    """This has validation details for the host

    Attributes:
        host (str | Unset): Hostname
        port (str | Unset): Port
        status (HostValidationDTOStatus | Unset): This has the validation status for a host.
        error (ErrorDetail | Unset): Host error details
    """

    host: str | Unset = UNSET
    port: str | Unset = UNSET
    status: HostValidationDTOStatus | Unset = UNSET
    error: ErrorDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        _status = d.pop("status", UNSET)
        status: HostValidationDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_host_validation_dto_status(_status)

        _error = d.pop("error", UNSET)
        error: ErrorDetail | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorDetail.from_dict(_error)

        host_validation_dto = cls(
            host=host,
            port=port,
            status=status,
            error=error,
        )

        host_validation_dto.additional_properties = d
        return host_validation_dto

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

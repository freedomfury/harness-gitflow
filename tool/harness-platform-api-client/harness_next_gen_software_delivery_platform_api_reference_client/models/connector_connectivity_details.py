from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_connectivity_details_status import (
    ConnectorConnectivityDetailsStatus,
    check_connector_connectivity_details_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="ConnectorConnectivityDetails")


@_attrs_define
class ConnectorConnectivityDetails:
    """Details of the connectivity status of the Connector.

    Attributes:
        status (ConnectorConnectivityDetailsStatus | Unset): Connectivity status of a Connector.
        error_summary (str | Unset): Summary of errors.
        errors (list[ErrorDetail] | Unset): List of errors and their details.
        tested_at (int | Unset): Time at which Test Connection was completed
        last_tested_at (int | Unset):
        last_connected_at (int | Unset): This is the last time at which the Connector was successfully connected.
    """

    status: ConnectorConnectivityDetailsStatus | Unset = UNSET
    error_summary: str | Unset = UNSET
    errors: list[ErrorDetail] | Unset = UNSET
    tested_at: int | Unset = UNSET
    last_tested_at: int | Unset = UNSET
    last_connected_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        error_summary = self.error_summary

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        tested_at = self.tested_at

        last_tested_at = self.last_tested_at

        last_connected_at = self.last_connected_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if error_summary is not UNSET:
            field_dict["errorSummary"] = error_summary
        if errors is not UNSET:
            field_dict["errors"] = errors
        if tested_at is not UNSET:
            field_dict["testedAt"] = tested_at
        if last_tested_at is not UNSET:
            field_dict["lastTestedAt"] = last_tested_at
        if last_connected_at is not UNSET:
            field_dict["lastConnectedAt"] = last_connected_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ConnectorConnectivityDetailsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_connector_connectivity_details_status(_status)

        error_summary = d.pop("errorSummary", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        tested_at = d.pop("testedAt", UNSET)

        last_tested_at = d.pop("lastTestedAt", UNSET)

        last_connected_at = d.pop("lastConnectedAt", UNSET)

        connector_connectivity_details = cls(
            status=status,
            error_summary=error_summary,
            errors=errors,
            tested_at=tested_at,
            last_tested_at=last_tested_at,
            last_connected_at=last_connected_at,
        )

        connector_connectivity_details.additional_properties = d
        return connector_connectivity_details

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

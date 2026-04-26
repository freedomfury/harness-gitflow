from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.get_all_allowed_field_values_connector_type import (
    GetAllAllowedFieldValuesConnectorType,
)
from ...models.response_dto_field_values import ResponseDTOFieldValues
from ...types import UNSET, Response


def _get_kwargs(
    *,
    account_identifier: str,
    connector_type: GetAllAllowedFieldValuesConnectorType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    json_connector_type: str = connector_type
    params["connectorType"] = json_connector_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/connectors/fieldValues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOFieldValues:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOFieldValues.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOFieldValues]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    connector_type: GetAllAllowedFieldValuesConnectorType,
) -> Response[Error | Failure | ResponseDTOFieldValues]:
    """List all the configured field values for the given Connector type.

     Returns all the configured field values for the given Connector type, which can be used during
    connector creation.

    Args:
        account_identifier (str):
        connector_type (GetAllAllowedFieldValuesConnectorType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOFieldValues]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        connector_type=connector_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    connector_type: GetAllAllowedFieldValuesConnectorType,
) -> Error | Failure | ResponseDTOFieldValues | None:
    """List all the configured field values for the given Connector type.

     Returns all the configured field values for the given Connector type, which can be used during
    connector creation.

    Args:
        account_identifier (str):
        connector_type (GetAllAllowedFieldValuesConnectorType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOFieldValues
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        connector_type=connector_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    connector_type: GetAllAllowedFieldValuesConnectorType,
) -> Response[Error | Failure | ResponseDTOFieldValues]:
    """List all the configured field values for the given Connector type.

     Returns all the configured field values for the given Connector type, which can be used during
    connector creation.

    Args:
        account_identifier (str):
        connector_type (GetAllAllowedFieldValuesConnectorType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOFieldValues]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        connector_type=connector_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    connector_type: GetAllAllowedFieldValuesConnectorType,
) -> Error | Failure | ResponseDTOFieldValues | None:
    """List all the configured field values for the given Connector type.

     Returns all the configured field values for the given Connector type, which can be used during
    connector creation.

    Args:
        account_identifier (str):
        connector_type (GetAllAllowedFieldValuesConnectorType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOFieldValues
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            connector_type=connector_type,
        )
    ).parsed

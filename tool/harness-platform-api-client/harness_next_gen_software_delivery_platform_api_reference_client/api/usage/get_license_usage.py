from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_license_usage import ResponseDTOLicenseUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    module: str,
    *,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
    cd_license_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["timestamp"] = timestamp

    params["CDLicenseType"] = cd_license_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usage/{module}".format(
            module=quote(str(module), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOLicenseUsage:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOLicenseUsage.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOLicenseUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    module: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
    cd_license_type: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOLicenseUsage]:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        module (str):
        account_identifier (str | Unset):
        timestamp (int | Unset):
        cd_license_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOLicenseUsage]
    """

    kwargs = _get_kwargs(
        module=module,
        account_identifier=account_identifier,
        timestamp=timestamp,
        cd_license_type=cd_license_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    module: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
    cd_license_type: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOLicenseUsage | None:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        module (str):
        account_identifier (str | Unset):
        timestamp (int | Unset):
        cd_license_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOLicenseUsage
    """

    return sync_detailed(
        module=module,
        client=client,
        account_identifier=account_identifier,
        timestamp=timestamp,
        cd_license_type=cd_license_type,
    ).parsed


async def asyncio_detailed(
    module: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
    cd_license_type: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOLicenseUsage]:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        module (str):
        account_identifier (str | Unset):
        timestamp (int | Unset):
        cd_license_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOLicenseUsage]
    """

    kwargs = _get_kwargs(
        module=module,
        account_identifier=account_identifier,
        timestamp=timestamp,
        cd_license_type=cd_license_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    module: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
    cd_license_type: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOLicenseUsage | None:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        module (str):
        account_identifier (str | Unset):
        timestamp (int | Unset):
        cd_license_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOLicenseUsage
    """

    return (
        await asyncio_detailed(
            module=module,
            client=client,
            account_identifier=account_identifier,
            timestamp=timestamp,
            cd_license_type=cd_license_type,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_service_usage_dto import ResponseDTOServiceUsageDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["timestamp"] = timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usage/CD/servicesLicense",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOServiceUsageDTO:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOServiceUsageDTO.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOServiceUsageDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceUsageDTO]:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceUsageDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceUsageDTO | None:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceUsageDTO
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOServiceUsageDTO]:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOServiceUsageDTO]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str | Unset = UNSET,
    timestamp: int | Unset = UNSET,
) -> Error | Failure | ResponseDTOServiceUsageDTO | None:
    """Gets License Usage By Module, Timestamp, and Account Identifier

    Args:
        account_identifier (str | Unset):
        timestamp (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOServiceUsageDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            timestamp=timestamp,
        )
    ).parsed

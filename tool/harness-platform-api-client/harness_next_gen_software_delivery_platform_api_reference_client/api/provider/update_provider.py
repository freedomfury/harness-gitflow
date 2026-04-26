from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_update_provider_response import ResponseDTOUpdateProviderResponse
from ...models.update_provider_request_dto import UpdateProviderRequestDTO
from ...types import UNSET, Response


def _get_kwargs(
    provider_identifier: str,
    *,
    body: UpdateProviderRequestDTO,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/provider/{provider_identifier}".format(
            provider_identifier=quote(str(provider_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOUpdateProviderResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOUpdateProviderResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOUpdateProviderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProviderRequestDTO,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOUpdateProviderResponse]:
    """Update a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):
        body (UpdateProviderRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOUpdateProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_identifier=provider_identifier,
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProviderRequestDTO,
    account_identifier: str,
) -> Error | Failure | ResponseDTOUpdateProviderResponse | None:
    """Update a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):
        body (UpdateProviderRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOUpdateProviderResponse
    """

    return sync_detailed(
        provider_identifier=provider_identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProviderRequestDTO,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOUpdateProviderResponse]:
    """Update a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):
        body (UpdateProviderRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOUpdateProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_identifier=provider_identifier,
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateProviderRequestDTO,
    account_identifier: str,
) -> Error | Failure | ResponseDTOUpdateProviderResponse | None:
    """Update a Provider by identifier

    Args:
        provider_identifier (str):
        account_identifier (str):
        body (UpdateProviderRequestDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOUpdateProviderResponse
    """

    return (
        await asyncio_detailed(
            provider_identifier=provider_identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed

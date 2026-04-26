from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.environment_request import EnvironmentRequest
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_environment_response import ResponseDTOEnvironmentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EnvironmentRequest | Unset = UNSET,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/environmentsV2/upsert",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOEnvironmentResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOEnvironmentResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOEnvironmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EnvironmentRequest | Unset = UNSET,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOEnvironmentResponse]:
    """Upsert an Environment by identifier

    Args:
        account_identifier (str):
        if_match (str | Unset):
        body (EnvironmentRequest | Unset): This is the Environment entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EnvironmentRequest | Unset = UNSET,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOEnvironmentResponse | None:
    """Upsert an Environment by identifier

    Args:
        account_identifier (str):
        if_match (str | Unset):
        body (EnvironmentRequest | Unset): This is the Environment entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EnvironmentRequest | Unset = UNSET,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOEnvironmentResponse]:
    """Upsert an Environment by identifier

    Args:
        account_identifier (str):
        if_match (str | Unset):
        body (EnvironmentRequest | Unset): This is the Environment entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOEnvironmentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EnvironmentRequest | Unset = UNSET,
    account_identifier: str,
    if_match: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOEnvironmentResponse | None:
    """Upsert an Environment by identifier

    Args:
        account_identifier (str):
        if_match (str | Unset):
        body (EnvironmentRequest | Unset): This is the Environment entity defined in Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOEnvironmentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            if_match=if_match,
        )
    ).parsed

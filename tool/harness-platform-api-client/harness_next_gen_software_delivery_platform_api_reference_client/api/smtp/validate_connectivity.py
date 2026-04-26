from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_validation_result import ResponseDTOValidationResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    identifier: str,
    account_id: str,
    to: str,
    subject: str,
    body: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identifier"] = identifier

    params["accountId"] = account_id

    params["to"] = to

    params["subject"] = subject

    params["body"] = body

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/smtpConfig/validate-connectivity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOValidationResult:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOValidationResult.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOValidationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    account_id: str,
    to: str,
    subject: str,
    body: str,
) -> Response[Error | Failure | ResponseDTOValidationResult]:
    """Tests the config's connectivity by sending a test email

    Args:
        identifier (str):
        account_id (str):
        to (str):
        subject (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOValidationResult]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        account_id=account_id,
        to=to,
        subject=subject,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    account_id: str,
    to: str,
    subject: str,
    body: str,
) -> Error | Failure | ResponseDTOValidationResult | None:
    """Tests the config's connectivity by sending a test email

    Args:
        identifier (str):
        account_id (str):
        to (str):
        subject (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOValidationResult
    """

    return sync_detailed(
        client=client,
        identifier=identifier,
        account_id=account_id,
        to=to,
        subject=subject,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    account_id: str,
    to: str,
    subject: str,
    body: str,
) -> Response[Error | Failure | ResponseDTOValidationResult]:
    """Tests the config's connectivity by sending a test email

    Args:
        identifier (str):
        account_id (str):
        to (str):
        subject (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOValidationResult]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        account_id=account_id,
        to=to,
        subject=subject,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    identifier: str,
    account_id: str,
    to: str,
    subject: str,
    body: str,
) -> Error | Failure | ResponseDTOValidationResult | None:
    """Tests the config's connectivity by sending a test email

    Args:
        identifier (str):
        account_id (str):
        to (str):
        subject (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOValidationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier=identifier,
            account_id=account_id,
            to=to,
            subject=subject,
            body=body,
        )
    ).parsed

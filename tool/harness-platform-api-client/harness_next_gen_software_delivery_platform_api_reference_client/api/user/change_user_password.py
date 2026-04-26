from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.password_change import PasswordChange
from ...models.response_dto_password_change_response import ResponseDTOPasswordChangeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PasswordChange | Unset = UNSET,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user/password",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOPasswordChangeResponse:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOPasswordChangeResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOPasswordChangeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordChange | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOPasswordChangeResponse]:
    """Change user password

     Updates the User password

    Args:
        account_identifier (str):
        body (PasswordChange | Unset): This is the view of the PasswordChange entity defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPasswordChangeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordChange | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOPasswordChangeResponse | None:
    """Change user password

     Updates the User password

    Args:
        account_identifier (str):
        body (PasswordChange | Unset): This is the view of the PasswordChange entity defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPasswordChangeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordChange | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOPasswordChangeResponse]:
    """Change user password

     Updates the User password

    Args:
        account_identifier (str):
        body (PasswordChange | Unset): This is the view of the PasswordChange entity defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOPasswordChangeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordChange | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOPasswordChangeResponse | None:
    """Change user password

     Updates the User password

    Args:
        account_identifier (str):
        body (PasswordChange | Unset): This is the view of the PasswordChange entity defined in
            Harness

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOPasswordChangeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed

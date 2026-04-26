from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.impersonate_dto import ImpersonateDTO
from ...models.response_dto_boolean import ResponseDTOBoolean
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    body: ImpersonateDTO | Unset = UNSET,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user/impersonate/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOBoolean:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOBoolean.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOBoolean]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImpersonateDTO | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """impersonate User

    Args:
        user_id (str):
        account_identifier (str):
        body (ImpersonateDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImpersonateDTO | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """impersonate User

    Args:
        user_id (str):
        account_identifier (str):
        body (ImpersonateDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImpersonateDTO | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """impersonate User

    Args:
        user_id (str):
        account_identifier (str):
        body (ImpersonateDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ImpersonateDTO | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """impersonate User

    Args:
        user_id (str):
        account_identifier (str):
        body (ImpersonateDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed

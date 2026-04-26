from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_boolean import ResponseDTOBoolean
from ...types import UNSET, Response


def _get_kwargs(
    account_identifier: str,
    *,
    account_status: str,
    account_type: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountStatus"] = account_status

    params["accountType"] = account_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/accounts/license/update/{account_identifier}".format(
            account_identifier=quote(str(account_identifier), safe=""),
        ),
        "params": params,
    }

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
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_status: str,
    account_type: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """License update from UI

    Args:
        account_identifier (str):
        account_status (str):
        account_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        account_status=account_status,
        account_type=account_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_status: str,
    account_type: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """License update from UI

    Args:
        account_identifier (str):
        account_status (str):
        account_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return sync_detailed(
        account_identifier=account_identifier,
        client=client,
        account_status=account_status,
        account_type=account_type,
    ).parsed


async def asyncio_detailed(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_status: str,
    account_type: str,
) -> Response[Error | Failure | ResponseDTOBoolean]:
    """License update from UI

    Args:
        account_identifier (str):
        account_status (str):
        account_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOBoolean]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        account_status=account_status,
        account_type=account_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    account_status: str,
    account_type: str,
) -> Error | Failure | ResponseDTOBoolean | None:
    """License update from UI

    Args:
        account_identifier (str):
        account_status (str):
        account_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOBoolean
    """

    return (
        await asyncio_detailed(
            account_identifier=account_identifier,
            client=client,
            account_status=account_status,
            account_type=account_type,
        )
    ).parsed

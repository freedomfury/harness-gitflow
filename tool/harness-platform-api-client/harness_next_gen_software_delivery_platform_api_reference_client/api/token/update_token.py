from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_token import ResponseDTOToken
from ...models.token import Token
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: Token | Unset = UNSET,
    account_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/token/{identifier}".format(
            identifier=quote(str(identifier), safe=""),
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
) -> Error | Failure | ResponseDTOToken:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOToken.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: Token | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOToken]:
    """Update a Token

     Updates a Token for the given API Key Type.

    Args:
        identifier (str):
        account_identifier (str):
        body (Token | Unset): This has the API Key Token details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOToken]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: Token | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOToken | None:
    """Update a Token

     Updates a Token for the given API Key Type.

    Args:
        identifier (str):
        account_identifier (str):
        body (Token | Unset): This has the API Key Token details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOToken
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: Token | Unset = UNSET,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOToken]:
    """Update a Token

     Updates a Token for the given API Key Type.

    Args:
        identifier (str):
        account_identifier (str):
        body (Token | Unset): This has the API Key Token details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOToken]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: Token | Unset = UNSET,
    account_identifier: str,
) -> Error | Failure | ResponseDTOToken | None:
    """Update a Token

     Updates a Token for the given API Key Type.

    Args:
        identifier (str):
        account_identifier (str):
        body (Token | Unset): This has the API Key Token details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOToken
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
        )
    ).parsed

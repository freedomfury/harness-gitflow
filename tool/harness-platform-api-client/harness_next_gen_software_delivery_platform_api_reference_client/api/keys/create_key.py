from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.key import Key
from ...models.response_dto_string import ResponseDTOString
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Key,
    account_identifier: str,
    key_scheme: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["keyScheme"] = key_scheme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOString:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOString.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Key,
    account_identifier: str,
    key_scheme: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Create Key

     Creates a SSH or PGP Key. Use query param keyScheme=ssh (default) or keyScheme=pgp. Defaults to SSH
    when keyScheme is not passed.

    Args:
        account_identifier (str):
        key_scheme (str | Unset):
        body (Key): This has the Key details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        key_scheme=key_scheme,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: Key,
    account_identifier: str,
    key_scheme: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Create Key

     Creates a SSH or PGP Key. Use query param keyScheme=ssh (default) or keyScheme=pgp. Defaults to SSH
    when keyScheme is not passed.

    Args:
        account_identifier (str):
        key_scheme (str | Unset):
        body (Key): This has the Key details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return sync_detailed(
        client=client,
        body=body,
        account_identifier=account_identifier,
        key_scheme=key_scheme,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Key,
    account_identifier: str,
    key_scheme: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOString]:
    """Create Key

     Creates a SSH or PGP Key. Use query param keyScheme=ssh (default) or keyScheme=pgp. Defaults to SSH
    when keyScheme is not passed.

    Args:
        account_identifier (str):
        key_scheme (str | Unset):
        body (Key): This has the Key details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOString]
    """

    kwargs = _get_kwargs(
        body=body,
        account_identifier=account_identifier,
        key_scheme=key_scheme,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Key,
    account_identifier: str,
    key_scheme: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOString | None:
    """Create Key

     Creates a SSH or PGP Key. Use query param keyScheme=ssh (default) or keyScheme=pgp. Defaults to SSH
    when keyScheme is not passed.

    Args:
        account_identifier (str):
        key_scheme (str | Unset):
        body (Key): This has the Key details defined in Harness.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOString
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            account_identifier=account_identifier,
            key_scheme=key_scheme,
        )
    ).parsed

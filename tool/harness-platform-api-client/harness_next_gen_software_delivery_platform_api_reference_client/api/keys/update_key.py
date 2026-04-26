from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_key import ResponseDTOKey
from ...models.update_public_key_request import UpdatePublicKeyRequest
from ...types import UNSET, Response


def _get_kwargs(
    identifier: str,
    *,
    body: UpdatePublicKeyRequest,
    account_identifier: str,
    parent_identifier: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["parentIdentifier"] = parent_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/keys/{identifier}".format(
            identifier=quote(str(identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOKey:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOKey.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOKey]:
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
    body: UpdatePublicKeyRequest,
    account_identifier: str,
    parent_identifier: str,
) -> Response[Error | Failure | ResponseDTOKey]:
    """Update a Key

     Updates a Key's validity period or revocation status. For COMPROMISED revocation of PGP keys, the
    code-api service is notified first.

    Args:
        identifier (str):
        account_identifier (str):
        parent_identifier (str):
        body (UpdatePublicKeyRequest): Request to update public key (SSH/PGP) validity or
            revocation status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOKey]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePublicKeyRequest,
    account_identifier: str,
    parent_identifier: str,
) -> Error | Failure | ResponseDTOKey | None:
    """Update a Key

     Updates a Key's validity period or revocation status. For COMPROMISED revocation of PGP keys, the
    code-api service is notified first.

    Args:
        identifier (str):
        account_identifier (str):
        parent_identifier (str):
        body (UpdatePublicKeyRequest): Request to update public key (SSH/PGP) validity or
            revocation status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOKey
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePublicKeyRequest,
    account_identifier: str,
    parent_identifier: str,
) -> Response[Error | Failure | ResponseDTOKey]:
    """Update a Key

     Updates a Key's validity period or revocation status. For COMPROMISED revocation of PGP keys, the
    code-api service is notified first.

    Args:
        identifier (str):
        account_identifier (str):
        parent_identifier (str):
        body (UpdatePublicKeyRequest): Request to update public key (SSH/PGP) validity or
            revocation status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOKey]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        account_identifier=account_identifier,
        parent_identifier=parent_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePublicKeyRequest,
    account_identifier: str,
    parent_identifier: str,
) -> Error | Failure | ResponseDTOKey | None:
    """Update a Key

     Updates a Key's validity period or revocation status. For COMPROMISED revocation of PGP keys, the
    code-api service is notified first.

    Args:
        identifier (str):
        account_identifier (str):
        parent_identifier (str):
        body (UpdatePublicKeyRequest): Request to update public key (SSH/PGP) validity or
            revocation status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOKey
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
            account_identifier=account_identifier,
            parent_identifier=parent_identifier,
        )
    ).parsed

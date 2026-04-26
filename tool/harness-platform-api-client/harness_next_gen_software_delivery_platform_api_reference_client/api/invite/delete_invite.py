from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_optional_invite import ResponseDTOOptionalInvite
from ...types import UNSET, Response


def _get_kwargs(
    invite_id: str,
    *,
    account_identifier: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/invites/{invite_id}".format(
            invite_id=quote(str(invite_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOOptionalInvite:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOOptionalInvite.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOOptionalInvite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOOptionalInvite]:
    """Delete Invite

     Delete an Invite by Identifier

    Args:
        invite_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOptionalInvite]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        account_identifier=account_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOOptionalInvite | None:
    """Delete Invite

     Delete an Invite by Identifier

    Args:
        invite_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOptionalInvite
    """

    return sync_detailed(
        invite_id=invite_id,
        client=client,
        account_identifier=account_identifier,
    ).parsed


async def asyncio_detailed(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Response[Error | Failure | ResponseDTOOptionalInvite]:
    """Delete Invite

     Delete an Invite by Identifier

    Args:
        invite_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOOptionalInvite]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        account_identifier=account_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
) -> Error | Failure | ResponseDTOOptionalInvite | None:
    """Delete Invite

     Delete an Invite by Identifier

    Args:
        invite_id (str):
        account_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOOptionalInvite
    """

    return (
        await asyncio_detailed(
            invite_id=invite_id,
            client=client,
            account_identifier=account_identifier,
        )
    ).parsed

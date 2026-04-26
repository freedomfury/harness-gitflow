from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.failure import Failure
from ...models.response_dto_invite import ResponseDTOInvite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    invite_id: str | Unset = UNSET,
    jwttoken: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["inviteId"] = invite_id

    params["jwttoken"] = jwttoken

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/invites/invite",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Failure | ResponseDTOInvite:
    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    response_default = ResponseDTOInvite.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Failure | ResponseDTOInvite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    invite_id: str | Unset = UNSET,
    jwttoken: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOInvite]:
    """Get Invite

     Gets an Invite by either Invite Id or JwtToken

    Args:
        account_identifier (str):
        invite_id (str | Unset):
        jwttoken (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInvite]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        invite_id=invite_id,
        jwttoken=jwttoken,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    invite_id: str | Unset = UNSET,
    jwttoken: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOInvite | None:
    """Get Invite

     Gets an Invite by either Invite Id or JwtToken

    Args:
        account_identifier (str):
        invite_id (str | Unset):
        jwttoken (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInvite
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        invite_id=invite_id,
        jwttoken=jwttoken,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    invite_id: str | Unset = UNSET,
    jwttoken: str | Unset = UNSET,
) -> Response[Error | Failure | ResponseDTOInvite]:
    """Get Invite

     Gets an Invite by either Invite Id or JwtToken

    Args:
        account_identifier (str):
        invite_id (str | Unset):
        jwttoken (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Failure | ResponseDTOInvite]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        invite_id=invite_id,
        jwttoken=jwttoken,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    invite_id: str | Unset = UNSET,
    jwttoken: str | Unset = UNSET,
) -> Error | Failure | ResponseDTOInvite | None:
    """Get Invite

     Gets an Invite by either Invite Id or JwtToken

    Args:
        account_identifier (str):
        invite_id (str | Unset):
        jwttoken (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Failure | ResponseDTOInvite
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            invite_id=invite_id,
            jwttoken=jwttoken,
        )
    ).parsed

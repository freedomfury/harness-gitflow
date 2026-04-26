from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegate_token_details import DelegateTokenDetails
from ...models.error import Error
from ...models.failure import Failure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    token_name: str,
    revoke_after: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountIdentifier"] = account_identifier

    params["orgIdentifier"] = org_identifier

    params["projectIdentifier"] = project_identifier

    params["tokenName"] = token_name

    params["revokeAfter"] = revoke_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/delegate-token-ng",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DelegateTokenDetails | Error | Failure | None:
    if response.status_code == 200:
        response_200 = DelegateTokenDetails.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Failure.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DelegateTokenDetails | Error | Failure]:
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
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    token_name: str,
    revoke_after: int | Unset = UNSET,
) -> Response[DelegateTokenDetails | Error | Failure]:
    """Creates Delegate Token.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        token_name (str):
        revoke_after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTokenDetails | Error | Failure]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        token_name=token_name,
        revoke_after=revoke_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    token_name: str,
    revoke_after: int | Unset = UNSET,
) -> DelegateTokenDetails | Error | Failure | None:
    """Creates Delegate Token.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        token_name (str):
        revoke_after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTokenDetails | Error | Failure
    """

    return sync_detailed(
        client=client,
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        token_name=token_name,
        revoke_after=revoke_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    token_name: str,
    revoke_after: int | Unset = UNSET,
) -> Response[DelegateTokenDetails | Error | Failure]:
    """Creates Delegate Token.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        token_name (str):
        revoke_after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegateTokenDetails | Error | Failure]
    """

    kwargs = _get_kwargs(
        account_identifier=account_identifier,
        org_identifier=org_identifier,
        project_identifier=project_identifier,
        token_name=token_name,
        revoke_after=revoke_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_identifier: str,
    org_identifier: str | Unset = UNSET,
    project_identifier: str | Unset = UNSET,
    token_name: str,
    revoke_after: int | Unset = UNSET,
) -> DelegateTokenDetails | Error | Failure | None:
    """Creates Delegate Token.

    Args:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        token_name (str):
        revoke_after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegateTokenDetails | Error | Failure
    """

    return (
        await asyncio_detailed(
            client=client,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            token_name=token_name,
            revoke_after=revoke_after,
        )
    ).parsed
